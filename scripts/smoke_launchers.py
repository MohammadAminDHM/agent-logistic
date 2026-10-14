"""Smoke-test built uvx/npx artifacts from outside the source checkout."""
from pathlib import Path
import argparse
import os
import shutil
import subprocess
import tempfile


def run(command, cwd, expected=0):
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    # Use a defined encoding for redirected Python output on Windows.
    env["PYTHONUTF8"] = "1"
    result = subprocess.run(command, cwd=cwd, env=env, capture_output=True, text=True,
                            encoding="utf-8", timeout=120)
    if result.returncode != expected:
        raise AssertionError(f"{command!r}: exit {result.returncode}\n{result.stdout}\n{result.stderr}")
    return result.stdout


def snapshot(root):
    return {str(p.relative_to(root)): (p.read_bytes(), p.stat().st_mtime_ns)
            for p in root.rglob("*") if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--wheel', type=Path, help='Wheel artifact to verify')
    parser.add_argument('--wheel-only', action='store_true', help='Skip npm checks')
    parser.add_argument('--python', help='Python version for uvx (for CI matrix)')
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    wheel = (args.wheel or repo / "dist/smartera_agentkit-0.1.0.dev2-py3-none-any.whl").resolve()
    archive = repo / "dist/smartera-agentkit-0.1.0-dev.2.tgz"
    assert wheel.is_file(), "Build wheel first"
    uvx = shutil.which("uvx")
    npx = shutil.which("npx.cmd" if os.name == "nt" else "npx")
    assert uvx, "uvx must be on PATH"
    python_option = ['--python', args.python] if args.python else []
    launchers = {
        "uvx-wheel": [uvx, *python_option, "--from", str(wheel), "smartera-agentkit"],
    }
    if not args.wheel_only:
        assert npx and archive.is_file(), "Build npm archive and ensure npx is on PATH"
        launchers.update({
            "npx-archive": [npx, "--yes", "--package", str(archive), "smartera-agentkit"],
            "npx-checkout": [npx, "--yes", "--package", str(repo), "smartera-agentkit"],
        })
    with tempfile.TemporaryDirectory(prefix="agentkit-launchers-") as temp:
        cwd = Path(temp)
        for name, command in launchers.items():
            assert "init" in run([*command, "--help"], cwd)
            assert "local-ai" in run([*command, "list"], cwd)
            assert "saas" in run([*command, "list"], cwd)
            target = cwd / f"{name} project \u03a9"
            run([*command, "init", str(target), "--profile", "saas", "--dry-run"], cwd)
            assert not target.exists(), "Dry-run created its target"
            target.mkdir()
            original = b"# User instructions\r\nPreserve these bytes.\r\n"
            (target / "AGENTS.md").write_bytes(original)
            (target / "package.json").write_text('{"private":true}\n')
            run([*command, "init", "--profile", "local-ai", "--profile", "saas"], target)
            assert (target / "AGENTS.md").read_bytes().startswith(original)
            assert (target / ".agent/context/LOCAL_AI.md").is_file()
            assert (target / ".agent/.gitignore").is_file()
            assert (target / ".agent/workflows/TOOLS.md").is_file()
            assert (target / ".agent/context/SAAS.md").is_file()
            for skill in ('token-budget-workflow', 'codebase-graph-navigation', 'saas-feature-delivery'):
                assert (target / f'.agents/skills/{skill}/SKILL.md').is_file()
            before = snapshot(target)
            run([*command, "init", "--profile", "saas", "--profile", "local-ai"], target)
            assert snapshot(target) == before, "Repeated init changed bytes or mtimes"
            run([*command, "doctor"], target)
            assert snapshot(target) == before, "Doctor wrote target files"
            run([*command, "init", "--profile", "unknown"], target, expected=2)
            assert snapshot(target) == before, "Invalid invocation changed the target"
            print(f"PASS {name}: help, list, dry-run, caller cwd, Unicode/spaces, preservation, repeat, doctor, exit code")
    if args.wheel_only:
        return
    # Check the launcher's actionable missing-uvx diagnostic without a shell.
    env = os.environ.copy()
    env["PATH"] = ""
    result = subprocess.run([shutil.which("node"), str(repo / "bin/smartera-agentkit.cjs"), "--help"],
                            env=env, capture_output=True, text=True)
    assert result.returncode == 1 and "uvx is required" in result.stderr
    print("PASS missing-uvx diagnostic")


if __name__ == "__main__":
    main()
