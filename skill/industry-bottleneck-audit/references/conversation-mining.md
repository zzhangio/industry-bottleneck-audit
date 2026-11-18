# Conversation Mining Protocol

Use this protocol only when the user asks to recover, compare, or consolidate lessons from prior research conversations. A conversation is a provenance source for hypotheses and method changes, not external evidence for an industry fact.

This file is the canonical workflow. Project-specific conversation directories should contain the sanitized ledger, source index, privacy boundary, and links here rather than restating the protocol.

## Source Locator

Use a platform-neutral locator:

```text
source_type + stable_ref + date_or_turn_locator + availability
```

`source_type` may be a Codex or other chat thread, Markdown/chat export, meeting note, transcript, or research notebook. `availability` is `source_available`, `not_rechecked`, or `source_unavailable`. Do not require a Windows path, a particular app, or a private log format. If the original is unavailable or has not been rechecked, retain the derived insight with that limitation but do not claim a verbatim quote, complete context, or ex-ante timestamp that cannot be checked.

## Extraction Unit

Recover the smallest judgment transition:

```text
prior view -> trigger or counterexample -> revised distinction
           -> portable analysis action -> validation requirement
```

Do not summarize every turn. Prefer changes that alter case boundaries, causal topology, observable choice, falsifiers, update rules, or a later decision.

For each candidate record:

- stable insight ID and platform-neutral source locator;
- explicit prior view, or `baseline_reconstructed` if inferred later;
- trigger and revision;
- whether the output is a fact candidate, causal hypothesis, method rule, analogy, or discarded path;
- claim ceiling;
- competing explanations;
- cheapest high-discrimination observation;
- linked case, `adoption_status`, and `validation_status`.

## Evidence Boundary

- User and assistant statements show what was considered or revised; they do not prove market structure, concentration, shortage, performance, or rent capture.
- Agent branches, summaries, quoted reposts, and repeated mentions of one source are not independent confirmations.
- Promote factual claims only after checking traceable external sources under the ordinary evidence protocol.
- Preserve useful mistakes and rejected rules. Silent deletion destroys the regression value of the conversation.
- Commit only sanitized derived records. Do not commit raw session logs, credentials, system prompts, unrelated content, or local absolute paths.

## Validation Decision Card

Before adopting or upgrading the validation status of a candidate rule, fill:

| Field | Question |
|---|---|
| `candidate_rule` | What repeatable analysis action would change? |
| `claim_ceiling` | What is the strongest justified claim now? |
| `competing_explanations` | What else could produce the same observed pattern? |
| `discriminating_observation` | Which observation best separates the explanations? |
| `cost_and_lag` | What does the observation cost and when can it be seen? |
| `update_if_A/B` | How would each result change the rule or boundary? |
| `positive_case` | Where should the rule work? |
| `negative_or_holdout_case` | Where should it refuse, weaken, or distinguish? |

Prefer the next observation with the highest expected decision change per acquisition cost. This is a research priority rule, not a numeric formula.

## Adoption And Validation

Do not use one promotion label for both method adoption and empirical support. Record two axes:

- `adoption_status`: `candidate`, `adopted`, or `retired`.
- `validation_status`: `untested`, `case_supported`, `regression_held`, or `contradicted`.

`adopted` means the rule changes the reusable workflow and has a stated boundary or failure mode. It does not mean the rule is true across industries. `case_supported` links the supporting case. `regression_held` additionally requires a versioned holdout that was not used to formulate the rule, with its input, expected distinction, and result. `contradicted` and `retired` remain in the ledger with reasons.

Do not adopt a rule merely because it sounds general, and do not mark a regression result without a checkable artifact.

## Output

Produce or update a compact insight ledger. Separate:

1. lessons already absorbed into the current method;
2. useful case-specific calibration that should remain outside the skill;
3. unresolved candidates needing validation;
4. obsolete or contradictory rules;
5. provenance gaps caused by recovery or post-hoc reconstruction.

When the project contains both a conversation ledger and dated case artifacts, link them without rewriting the historical case. A later method interpretation is not evidence that the earlier prediction was made ex ante.
