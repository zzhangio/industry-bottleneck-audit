# Publishing workflow

Publish this preview as a new repository. Do not change the visibility of the private research repository.

## 1. Review locally

Review `DEMO-CONTRACT.md`, the two case cards, and every file selected for release. The current public owner is `zzhangio`; update clone URLs if the repository later moves.

Run:

```powershell
.\scripts\prepublish-check.ps1 `
  -PrivateDenylist ..\..\research-governance\private-export-denylist.txt
```

The denylist remains outside this public repository. The script also requires an exact `scripts/public-files.allowlist` and checks forbidden artifact names in Git history. Then inspect the file list manually. A clean scan cannot determine copyright, private research value, reconstructability, or whether a holdout has been contaminated.

## 2. Create a new private staging repository

From this directory:

```powershell
git init -b main
git add .
git commit -m "Publish industry bottleneck audit beta"
gh repo create zzhangio/industry-bottleneck-audit --private --source . --remote origin --push
```

Open the repository, verify Markdown links and the file tree, enable Issues and Discussions, and ask one trusted friend to clone the private staging repository first.

## 3. Final public review

Before changing visibility:

- confirm no `.env`, keys, browser state, absolute local paths, private labels, or sealed/holdout artifacts exist anywhere in Git history;
- confirm the public package does not identify private cases, holdouts, answer structure, failed searches, ablation traces, or cross-case negative-knowledge ledgers;
- confirm third-party content is linked and summarized rather than copied;
- run a fresh install and both example prompts;
- verify the license and copyright holder text;
- verify the public README does not claim broad validation;
- decide whether the maintainer email or security contact should be public.

Once a repository has been public, deleting a file does not retract clones, forks, or earlier commit objects.

## 4. Make it public

```powershell
gh repo edit zzhangio/industry-bottleneck-audit `
  --visibility public `
  --accept-visibility-change-consequences
```

Add repository topics such as `codex-skill`, `industry-analysis`, `technology-strategy`, and `bottleneck-analysis` through GitHub settings.

## 5. Tag the reviewed beta

```powershell
git tag -a v0.1.0 -m "Public beta"
git push origin v0.1.0
gh release create v0.1.0 --title "Industry Bottleneck Audit v0.1.0" --generate-notes
```

Do not tag the current review draft until the user has approved its meaning and contents.

## 6. Invite useful feedback

Give each friend one link and one request: bring a real case not used in the examples, run Quick Scan without maintainer coaching, and submit the structured feedback form. Ask explicitly for failed or unresolved cases. Ten diverse trials are more informative than many reactions to the README.

Use issues for reproducible defects, Discussions for new use cases and conceptual questions, and pull requests for scoped changes. Record which public version produced every shared output.

