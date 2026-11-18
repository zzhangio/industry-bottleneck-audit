# Installation and use

## Codex installation

Windows:

```powershell
.\skill\industry-bottleneck-audit\scripts\install_skill.ps1
```

The script copies the skill to `%USERPROFILE%\.codex\skills\industry-bottleneck-audit`, excludes Python caches, verifies SHA-256 hashes, and is idempotent.

macOS or Linux:

```bash
mkdir -p ~/.codex/skills/industry-bottleneck-audit
cp -R skill/industry-bottleneck-audit/. ~/.codex/skills/industry-bottleneck-audit/
```

Start a new task after installation so the skill is discovered.

## Use without installation

An agent that can read local files may be told:

```text
Use the skill at skill/industry-bottleneck-audit/SKILL.md to analyze this case.
Read only the references needed by the selected depth.
```

Other agent products may not implement Codex skill discovery, but the Markdown instructions, references, schema, and validators remain portable.

## Optional dependencies

Quick Scan needs no Python package. Full Audit bundle validation requires:

```bash
python -m pip install -r skill/industry-bottleneck-audit/requirements.txt
```

No web-search credential is included. Use an available search provider or a user-supplied source packet and record what was actually used.

