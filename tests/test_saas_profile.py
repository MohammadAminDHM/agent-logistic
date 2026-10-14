import json
import re

import pytest

from smartera_agentkit.cli import main, PROFILE_SKILLS


def snapshot(root):
    return {str(p.relative_to(root)): (p.read_bytes(), p.stat().st_mtime_ns)
            for p in root.rglob('*') if p.is_file()}


def test_saas_preview_is_read_only_for_missing_and_existing_targets(tmp_path):
    missing = tmp_path / 'not created'
    assert main(['init', str(missing), '--profile', 'saas', '--dry-run']) == 0
    assert not missing.exists()
    assert main(['init', str(tmp_path)]) == 0
    before = snapshot(tmp_path)
    assert main(['add', 'profile', 'saas', str(tmp_path), '--dry-run']) == 0
    assert snapshot(tmp_path) == before


def test_saas_installs_dependencies_and_preserves_existing_project(tmp_path):
    # Spec Kit artifacts and customer source remain owned by the project.
    for name, contents in {
        'AGENTS.md': b'# User rules\r\nKeep this section.\r\n',
        '.specify/memory/constitution.md': b'Existing project principles\n',
        'specs/001-feature/spec.md': b'Original canonical feature contract\n',
        'package.json': b'{"private":true}\n',
        'app.py': b'print("customer code")\n',
    }.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(contents)
    before = snapshot(tmp_path)
    assert main(['init', str(tmp_path), '--profile', 'saas']) == 0
    after = snapshot(tmp_path)
    for name in before:
        if name != 'AGENTS.md':
            assert after[name] == before[name]
    assert (tmp_path / 'AGENTS.md').read_bytes().startswith(before['AGENTS.md'][0])
    manifest = json.loads((tmp_path / '.agent/agentkit-manifest.json').read_text('utf-8'))
    assert set(PROFILE_SKILLS['saas']) <= set(manifest['skills'])
    assert '.specify/memory/constitution.md' not in manifest['files']
    assert 'specs/001-feature/spec.md' not in manifest['files']
    assert (tmp_path / '.agent/context/SAAS.md').is_file()
    assert main(['doctor', str(tmp_path)]) == 0
    installed = snapshot(tmp_path)
    assert main(['init', str(tmp_path), '--profile', 'saas']) == 0
    assert main(['add', 'profile', 'saas', str(tmp_path)]) == 0
    assert main(['doctor', str(tmp_path)]) == 0
    assert snapshot(tmp_path) == installed


@pytest.mark.parametrize('profiles', [('saas', 'local-ai'), ('local-ai', 'saas')])
def test_profiles_combine_deterministically(tmp_path, profiles):
    left, right = tmp_path / 'left', tmp_path / 'right'
    assert main(['init', str(left), '--project-name', 'Demo',
                 '--profile', profiles[0], '--profile', profiles[1]]) == 0
    assert main(['init', str(right), '--project-name', 'Demo',
                 '--profile', profiles[1], '--profile', profiles[0]]) == 0
    assert {k: v[0] for k, v in snapshot(left).items()} == {
        k: v[0] for k, v in snapshot(right).items()}
    for skill in (*PROFILE_SKILLS['saas'], 'gpu-inference-debug'):
        assert (left / f'.agents/skills/{skill}/SKILL.md').is_file()
    assert main(['doctor', str(left)]) == 0


def test_saas_add_preserves_user_docs_and_detects_block_conflict(tmp_path):
    assert main(['init', str(tmp_path)]) == 0
    doc = tmp_path / '.agent/context/SAAS.md'
    doc.write_bytes(b'User-owned SaaS facts\r\n')
    stat = doc.stat().st_mtime_ns
    assert main(['add', 'profile', 'saas', str(tmp_path)]) == 0
    assert doc.read_bytes() == b'User-owned SaaS facts\r\n'
    assert doc.stat().st_mtime_ns == stat
    manifest = json.loads((tmp_path / '.agent/agentkit-manifest.json').read_text('utf-8'))
    assert '.agent/context/SAAS.md' not in manifest['files']
    instructions = tmp_path / 'AGENTS.md'
    instructions.write_bytes(instructions.read_bytes().replace(b'For SaaS delivery', b'Edited SaaS rules'))
    before = snapshot(tmp_path)
    assert main(['add', 'profile', 'local-ai', str(tmp_path)]) == 3
    assert snapshot(tmp_path) == before


def test_doctor_checks_saas_documents_and_profile_dependencies(tmp_path):
    assert main(['init', str(tmp_path), '--profile', 'saas']) == 0
    doc = tmp_path / '.agent/workflows/TOOLS.md'
    doc.unlink()
    assert main(['doctor', str(tmp_path)]) == 4
    assert main(['init', str(tmp_path), '--profile', 'saas']) == 0
    manifest_path = tmp_path / '.agent/agentkit-manifest.json'
    manifest = json.loads(manifest_path.read_text('utf-8'))
    manifest['skills'].remove('saas-feature-delivery')
    manifest_path.write_text(json.dumps(manifest), encoding='utf-8')
    assert main(['doctor', str(tmp_path)]) == 4


def test_strict_doctor_reports_unresolved_saas_facts(tmp_path, capsys):
    assert main(['init', str(tmp_path), '--profile', 'saas']) == 0
    capsys.readouterr()
    before = snapshot(tmp_path)
    assert main(['doctor', str(tmp_path), '--strict', '--json']) == 4
    report = json.loads(capsys.readouterr().out)
    assert any('incomplete profile facts: .agent/context/SAAS.md' in w for w in report['warnings'])
    assert snapshot(tmp_path) == before


def test_new_skills_can_be_added_without_saas_profile(tmp_path):
    assert main(['init', str(tmp_path)]) == 0
    for skill in PROFILE_SKILLS['saas']:
        assert main(['add', 'skill', skill, str(tmp_path)]) == 0
    assert not (tmp_path / '.agent/context/SAAS.md').exists()
    assert main(['doctor', str(tmp_path)]) == 0


def test_default_init_does_not_enable_saas(tmp_path):
    assert main(['init', str(tmp_path)]) == 0
    assert not (tmp_path / '.agent/context/SAAS.md').exists()
    assert not (tmp_path / '.agent/workflows').exists()
    assert b'For SaaS delivery' not in (tmp_path / 'AGENTS.md').read_bytes()


def test_saas_scaffold_needs_no_external_executables_and_routes_narrowly(tmp_path, monkeypatch):
    monkeypatch.setenv('PATH', '')
    assert main(['init', str(tmp_path), '--profile', 'saas']) == 0
    assert main(['doctor', str(tmp_path)]) == 0
    assert len((tmp_path / 'AGENTS.md').read_bytes()) <= 2048
    for doc in (tmp_path / '.agent').rglob('*.md'):
        for relative in re.findall(r'`(\.agent/[^`\n]+\.md)`', doc.read_text('utf-8')):
            assert (tmp_path / relative).is_file(), f'Broken internal route in {doc}: {relative}'
