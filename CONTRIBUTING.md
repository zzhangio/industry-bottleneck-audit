# Contributing

The most useful contribution is a traceable case where the method helped, failed, or selected the wrong boundary.

## Before opening an issue

1. Remove confidential company information and personal data.
2. Record the skill version, model, date, evidence cutoff, and search access.
3. Preserve the original prompt and output.
4. Say whether the failure concerns method, boundary, evidence, tools, or human rendering.
5. Include the strongest omitted node, edge, bypass, or counterexample you can name.

Do not submit copyrighted report bodies, API keys, browser sessions, or private datasets. Link to public sources and summarize them in your own words.

Treat every GitHub issue, discussion, and pull request as permanently public. Do not submit private evaluation design, hidden case identities, answer keys, detailed failed-run traces, or internal cross-case research. The maintainers may preserve a richer failure record privately and publish only a de-identified invariant or completed case.

## Pull requests

Keep changes narrow. A new universal rule should fix a repeated cross-domain failure or protect an important invariant. Domain-specific details normally belong in an example or reference, not in the core `SKILL.md`.

Run the checks in [docs/PUBLISHING.md](docs/PUBLISHING.md) before opening a pull request.

