import json
from smartera_agentkit.cli import main


def test_init_dry_run_no_writes(tmp_path):
    root=tmp_path/'not-created'
    assert main(['init',str(root),'--dry-run'])==0
    assert not root.exists()


def test_init_repeat_preserves_mtimes(tmp_path):
    assert main(['init',str(tmp_path),'--project-name','Demo'])==0
    doc=tmp_path/'AGENTS.md'
    manifest=tmp_path/'.agent/agentkit-manifest.json'
    contents=[doc.read_bytes(),manifest.read_bytes()]
    mtimes=[doc.stat().st_mtime_ns,manifest.stat().st_mtime_ns]
    assert main(['init',str(tmp_path)])==0
    assert contents==[doc.read_bytes(),manifest.read_bytes()]
    assert mtimes==[doc.stat().st_mtime_ns,manifest.stat().st_mtime_ns]
    assert main(['doctor',str(tmp_path)])==0


def test_existing_agents_keeps_user_text(tmp_path):
    p=tmp_path/'AGENTS.md'
    p.write_bytes(b'# My instructions\r\nDo not delete.\r\n')
    assert main(['init',str(tmp_path)])==0
    assert p.read_bytes().startswith(b'# My instructions\r\nDo not delete.\r\n')
    assert main(['init',str(tmp_path),'--profile','local-ai'])==0
    assert p.read_bytes().startswith(b'# My instructions\r\nDo not delete.\r\n')
    assert (tmp_path/'.agent/context/LOCAL_AI.md').is_file()
    assert main(['doctor',str(tmp_path)])==0


def test_unowned_file_preserved(tmp_path):
    doc=tmp_path/'.agent/PROJECT.md'
    doc.parent.mkdir(parents=True)
    doc.write_text('custom docs')
    assert main(['init',str(tmp_path)])==0
    assert doc.read_text()=='custom docs'
    m=json.loads((tmp_path/'.agent/agentkit-manifest.json').read_text())
    assert '.agent/PROJECT.md' not in m['files']


def test_conflict_preflight_no_partial_changes(tmp_path):
    p=tmp_path/'AGENTS.md'
    p.write_text('<!-- smartera-agentkit:begin -->\ninvalid')
    assert main(['init',str(tmp_path)])==3
    assert not (tmp_path/'.agent/agentkit-manifest.json').exists()


def test_add_skill(tmp_path):
    assert main(['init',str(tmp_path)])==0
    assert main(['add','skill','gpu-inference-debug',str(tmp_path)])==0
    assert main(['add','skill','gpu-inference-debug',str(tmp_path)])==0
    assert (tmp_path/'.agents/skills/gpu-inference-debug/SKILL.md').is_file()


def test_symlink_refusal(tmp_path):
    outside=tmp_path/'outside'
    outside.mkdir()
    target=tmp_path/'target'
    target.mkdir()
    (target/'.agent').symlink_to(outside,target_is_directory=True)
    assert main(['init',str(target)])==3
    assert not list(outside.iterdir())
