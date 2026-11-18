# Public disclosure boundary

This repository is a curated product surface, not a mirror of the private research archive that produced it.

## Included

- stable Skill instructions and deterministic validators needed to use them;
- generic invariants that do not depend on a hidden case identity;
- small synthetic fixtures and deliberately declassified teaching cases;
- public source links, original summaries, installation notes, and contribution interfaces.

## Excluded by default

- raw evaluation runs, failed prompts, answer keys, reviewer disagreements, and contamination records;
- holdout identities, sealed packet structure, expected failure modes, and unpublished evaluation results;
- detailed ablation traces, unsuccessful source paths, and internal scoring ledgers;
- private cross-case synthesis that has not matured into a domain-independent rule;
- personal research, career analysis, proprietary material, authentication state, and local paths;
- the private repository's Git history.

Public source availability does not make the private selection, connection, counterexample structure, or failure history public. A general rule may be released without releasing the private cases that taught it.

## One-way release rule

Changes flow from private research into a separately reviewed public package. Public feedback returns as a candidate observation, not as an automatic edit to the private system of record.

Every release must pass:

1. the exact public-file allowlist;
2. credential and local-path scanning;
3. a maintainer-supplied private denylist scan when available;
4. current-tree and Git-history checks for forbidden private artifact names;
5. manual semantic review, because automated scans cannot recognize valuable negative knowledge or reconstructability.

Deleting a public file does not retract clones, forks, caches, or earlier commit objects. When uncertain, keep the material private.

