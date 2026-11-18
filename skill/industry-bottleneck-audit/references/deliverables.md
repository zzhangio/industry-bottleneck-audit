# Deliverables And Update Contract

## 0. Quick Scan Decision Card

Quick mode uses [quick-scan.md](quick-scan.md). It is one bounded judgment with one canonical journey, not a shortened canonical audit bundle. Lead with the memory sentence and control picture; keep internal route names, scores, exhaustive topology, and formal prediction machinery out of the first-pass artifact.

If the user explicitly requests a full, deep, auditable, or formal artifact, enter the full deliverables below directly. If work began as a quick scan, upgrade only when the scan records a concrete unresolved dependency that could change the bounded decision. Do not ask the user to choose among internal technical routes.

## 1. Shared Audit Bundle And Claim Ledger

Both expression routes must be generated from one canonical audit bundle. The bundle retains case identity, nodes, edges, sources, rights, company mappings, hypotheses, events, snapshots, predictions, and views. At minimum each claim retains:

| Field | Purpose |
|---|---|
| `claim_id` | Stable link between prose, diagram, evidence, and later snapshots. |
| `plain_claim` | One-sentence statement understandable without model notation. |
| `technical_claim` | Precise mechanism with `Y/Q/Omega/t`. |
| `status` | anchored / conditional / speculative / broken / stale. |
| `evidence_ids` | Sources supporting each factual edge. |
| `unknowns` | What public evidence cannot establish. |
| `falsifier` | Observable event that lowers or removes the claim. |
| `review_trigger` | Date or technical, supply, policy, or customer event requiring reassessment. |
| `hypothesis_id/version` | Dated causal baseline from which a later evidence update is measured. |

Do not maintain a separate “simple facts” dataset. Plain language is a view over the audit ledger.

Use [../schemas/audit-bundle.schema.json](../schemas/audit-bundle.schema.json) for reusable or versioned work and run `scripts/validate_audit_bundle.py` before publication. Markdown may remain the primary human artifact, but it cannot become a competing source of node, claim, company, or prediction state.

## 2. Technical Audit Route

Default structure:

1. **Decision summary:** bounded case, system output, core `Q`, structure type, current activation, and largest unknown.
2. **Functional topology:** flow of functions, alternatives, feedback loops, acceptance gates, and system boundary.
3. **Candidate-node table:** effective width, concentration type, qualification, time constant, substitutes, and owner.
4. **Minimum cut:** single-node or compatible-cluster explanation, with intervention logic.
5. **Definition/validation rights:** value definition, encoding, acceptance, modification, feedback ownership, and responsibility.
6. **Bottleneck and capture:** `B_struct/B_now/P_joint/P_own/P_cycle/P_now/E`, with prose before scores.
7. **Remote influence paths:** numbered mechanism chains, counterforces, lags, observables, and falsifiers.
8. **Cycle test:** prices, inventory, utilization, lead times, capex, qualification, and product mix.
9. **Scale and organizational balance:** before/after qualified volume, labor per unit, total labor/headcount, role and wage mix, organization/site count, unit economics, rebound, and where released capacity moved.
10. **Portfolio economics when applicable:** success distribution, failed-attempt cost, discovery/acquisition cost, channel take, and feedback reuse.
11. **Company mapping:** company and department only where organizational evidence permits; distinguish strong, partial, coalition, and no clean match.
12. **Evidence ledger and next review:** `[F]/[I]/[U]`, source IDs, cutoff date, leading indicators, and triggers.

## 3. Nontechnical Decision Route

Lead with a concrete control picture, not internal scores:

```text
What customers need
-> who or what must make it acceptable
-> who is waiting for that approval or output
-> what a substitute would force the system to redo
-> who can retain money or decision power
```

The first view must also show `currently supportable` and `not yet known`. Do not hide uncertainty in a technical appendix or turn an unresolved study into a smooth company story.

Answer these questions in ordinary language:

- What is the real delivered product, rather than the industry's broad label?
- What currently prevents more accepted output?
- Is the obstacle capacity, yield, compatibility, permission, evidence, responsibility, or demand?
- Which identifiable organization can delay or release the flow?
- Who has final acceptance power?
- Can buyers redesign, dual-source, migrate, or wait?
- Does the constrained party keep the rent, or do customers and complementary suppliers absorb it?
- What observable change would alter the conclusion?
- Did the old function shrink only per transaction, or also in total employment and spending?
- Which department, occupation, vendor, customer, or downstream node absorbed the released work and increased in scale?

When the request asks for “where bargaining power sits,” include a compact actor matrix covering price/terms, allocation, specification, acceptance, modification rights, risk burden, and feedback ownership. A different actor may lead each column.

Keep formulas, symbolic fields, and full scoring outside the first-view diagram. A detail panel or linked appendix may expose them by `claim_id`.

### Company Mapping Labels

- `strong_match`: a named organization controls the relevant output or acceptance gate and the relationship is publicly supportable.
- `partial_match`: the company participates materially but shares the cut set or lacks final validation.
- `coalition`: no single company owns the compatible path.
- `no_clean_match`: the mechanism is real but public evidence does not support a company-level attribution.

Do not turn “unique supplier,” “tool of record,” or “industry leader” into a current capacity-shortage or profit claim without separate evidence.

## 4. Technology-First Scan Route

Use this route when the technology is known before the affected industry or company. Default structure:

1. **Shock card:** demonstrated capability delta, baseline, maturity, boundary, resource needs, and evidence cutoff.
2. **Function inventory:** tasks exposed to the changed primitive before assigning industry labels.
3. **Candidate screen:** structural overlap, exposed share, adoption and qualification friction, complement slack, demand elasticity, rights shift, capture, and evidence.
4. **Pre/post topology:** old minimum cut or distributed network, insertion mechanism, relaxed node, activated complement, convergence mechanism, supported successor state, and counterforces.
5. **Power migration:** definition, validation, modification, responsibility, feedback, and contract changes.
6. **Horizon forecast:** dated near/medium/long predictions, leading observables, and falsifiers.
7. **Control case:** one plausible industry or function where the technology should not materially alter structure.
8. **Company mapping:** only after the functional forecast; separate supplier, adopter, complement owner, validator, and distributor.

The nontechnical first view should read:

```text
What the technology can now do
-> which expensive or scarce job it changes
-> where that job matters
-> which old obstacle becomes easier
-> whether and where released flow meets another limit
-> whose decisions or data become more important
```

## 5. Visual Contract

Implementation and routing details live in [visualization.md](visualization.md). Use its standalone renderer for a full or versioned audit; keep an ordinary Quick Scan to one small control picture unless the user explicitly requests an HTML artifact.

The primary visual should emphasize a small number of auditable facts:

- solid nodes for observed products, processes, qualifications, or organizations;
- conditional nodes with stable claim IDs;
- dashed counterforces for substitution, efficiency, standards, or new supply;
- an audit exit showing the observable, falsifier, and review trigger;
- company/department names only when the mapping is supportable.

Each main arrow names the transmitted object in ordinary language. Color and line width may show emphasis but cannot carry the only meaning. Keep model scores in a secondary table or drill-down.

For interactive output, clicking a node should reveal: plain explanation, role in the functional chain, who waits, validator, company match, confirmed facts, unknowns, falsifiers, sources, and current-versus-prior change.

For a technology-first scan, show the before and predicted-after paths side by side. Visually distinguish the directly relaxed node, newly viable complements, shared interfaces or acceptance paths, the supported successor state, unchanged hard gates, and speculative edges. The successor may be one constraint, a convergence candidate, a formed emergent cluster, distributed limits, none visible in the horizon, or unknown. Never use one arrow labeled “disruption” in place of the propagation chain.

## 6. Snapshot And Evidence-Event Contract

Published snapshots are append-only. Keep stable node and claim IDs. Each snapshot records:

```text
snapshot_id, as_of, evidence_cutoff, system_boundary,
node presence, topology role, certainty, activation pressure,
organization composition, scale-balance record, evidence_ids, and review note
```

On reassessment, compare before rewriting prose:

- node added or retired;
- topology or minimum-cut migration;
- pressure tightened or eased;
- supplier/organization composition changed;
- qualified volume, unit labor, total headcount, role mix, or organization count changed;
- released capacity was absorbed by a named successor, rebound demand, margin, or remained idle;
- evidence certainty changed;
- system boundary changed, requiring a new case rather than a silent overwrite.

Retired nodes remain visible in comparison mode. A missed review trigger marks a claim `stale`; it does not silently preserve the prior conclusion.

Snapshots can be triggered by a calendar or by an event. Use three compatible levels:

1. **Periodic snapshot:** regular reconstruction of the whole case, such as semiannual review.
2. **Evidence-event patch:** one new fact updates named hypothesis premises, causal edges, timing, uncertainty, nodes, or actors without silently replacing the baseline.
3. **Verification snapshot:** at the expected lag, compare recorded predictions with measured outcomes and attribution alternatives.

An evidence-event patch records:

```text
event_id, source_id, published_at, effective_at, observed_at,
prior_hypothesis_id/version, direct_fact, update_target, update_relation,
revised_hypothesis_version, observed_change_now, expected_changes,
counterforces, next_verification_at, and rebuild_required
```

Each expected change records a stable `prediction_id`, target node or actor, direction, magnitude range, dependency, horizon, observable, and invalidating result. Keep `observed_change_now` separate from `expected_changes`; a credible forecast is not a current topology change.

Use `rebuild_required = true` when the event may move the minimum cut, add or retire a material node, reallocate definition/validation rights, change `Y/Q/Omega`, or invalidate several linked claims. Otherwise publish the patch and defer a full rebuild to the next scheduled review.

### Compact Human-Readable Delta

For a single new item, the minimum useful output is:

| Before | New fact | What changes now | What should change next | When/how to verify |
|---|---|---|---|---|
| Prior dated hypothesis | Directly supported fact | Premise, mechanism, confidence, or current state | Named node/actor effect with direction and counterforce | Observable, horizon, falsifier, next review |

Also state `what did not change`. This prevents a locally important event from being narrated as a total industry regime shift.

## 7. Minimum Acceptance Checklist

For an initial or fully rebuilt case:

- The canonical audit bundle passes structural and cross-reference validation when the study is reusable, comparative, or versioned.
- The case states `Y/Q/Omega/t` and exclusions.
- The graph includes a substitute or counterforce.
- Qualified effective width is distinguished from nominal vendors or capacity.
- Structural and current bottlenecks are separate.
- `P_joint` and `P_own` are separate.
- Definition, encoding, validation, and modification rights are located.
- Material relaxation or automation claims include a comparable before/after scale balance, or explicitly record why output, labor, headcount, and organizational denominators are unavailable.
- Every major remote path has a stable claim ID and edge-level evidence.
- The zoomed child graph can reconstruct or explicitly overturn the parent judgment.
- Technical and nontechnical outputs trace to the same claim ledger.
- Sources, unknowns, falsifiers, cutoff date, and next review trigger are present.

For an evidence-event patch:

- The prior hypothesis version and its original date remain recoverable.
- The new direct fact is separated from interpretation and duplicate reporting.
- The update target and relation are explicit, including a justified `no_change` when applicable.
- Belief change, observed system change, and expected future change are not conflated.
- The patch says what did not change and whether a full rebuild is required.
- Each material prediction has a horizon, dependency, observable, and invalidating result.

For a formal sealed historical split:

- The t0 evaluator used a local body-only packet, not live search or URL extraction.
- Source-selection rules, raw and normalized hashes, body boundaries, and prompt hash were frozen before prediction.
- Later retrospectives, current chrome, snippets, redirects, and related links were excluded before evaluator access.
- Any exposure is retained as a contaminated run; a clean replacement uses a fresh context and records `rerun_of`.

For a technology-first scan:

- The output identifies itself as a scoping forecast or a researched current-state audit.
- Demonstrated capability, transferable inference, and roadmap claim are separated.
- Stipulated `[H]` scenarios are not presented as real-world evidence, and maturity uses the deployment ladder rather than “available” alone.
- Functions are screened before industries and companies.
- At least one pre/post minimum-cut path and one low-impact control case are present.
- The relaxed node and successor state are both recorded; a single successor constraint is not forced.
- Adoption, structural impact, and value capture remain separate judgments.
- Predictions have dates or horizons, leading observables, counterforces, and falsifiers.
