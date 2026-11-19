---
name: industry-bottleneck-audit
description: Quickly screen or fully audit an industry, company, or technology for functional bottlenecks, bargaining power, structural change, and falsifiable update triggers. Use for first-look industry questions and for auditable deep research; not for generic market-size summaries or automatic investment scoring.
---

# Industry Bottleneck Audit

Find where qualified system output is actually narrowed, who controls that narrowing, and whether the controller can retain bargaining power. The user chooses only **quick** or **full** when they care to; do not ask them to classify the case as industry-first, technology-first, dynamic, or company-capture.

## Choose One Depth

Honor an explicit depth request. Start **Full Audit** directly, without a preliminary quick artifact, when the user asks for a deep/auditable report or the requested deliverable itself requires formal validation, a reusable dataset, versioned reconstruction, or conflict resolution. Otherwise use **Quick Scan** by default for a first look, new idea, comparison, one-evidence update, or exploratory company question.

If depth is ambiguous, start quick. State the chosen depth in one short phrase and proceed. Do not present a menu. A quick scan may recommend a full audit, but it must finish its own bounded judgment first rather than silently expanding.

## Audience Rendering

For chat answers, reports, presentations, interactive visuals, or any artifact intended for direct human review, read [references/human-review-compression.md](references/human-review-compression.md) and derive a compressed review view from the same claims and evidence. Human-facing output must make the qualified output, current cut, bypass, successor constraint, and largest unknown visible without requiring the reviewer to reconstruct them from a broad table or repeated conditional prose.

Machine-native artifacts such as canonical bundles, claim ledgers, evidence packets, agent handoffs, and validator inputs may skip the human compression pass when no human review is requested. Preserve their stable IDs and full structure. If a machine-native artifact is later shown to a person, render a compressed view over it; do not edit the underlying evidence or create a second conclusion store for presentation.

## Discovery Before Case Freeze

When the user asks an open-ended question such as “what bottlenecks does this new capability loosen?” or “which industries could this affect?”, do not freeze one industry case yet. Read [references/capability-discovery.md](references/capability-discovery.md), freeze the demonstrated capability shock, and run the open-world discovery pass first. Its job is candidate recall across task domains, including non-obvious adjacencies and blocked controls; it is not yet an industry verdict.

Only after the capability surface and candidate task families are visible should the analysis select material candidates and freeze a separate `Y/Q/Omega/t` case for each one. Do not describe the resulting list as exhaustive unless a declared search universe and saturation test support that claim.

## Event Topology Lens

For any material technology, policy, cost, interface, or capability event, do not ask only which existing bottleneck it relaxes. Apply four directions before freezing the final candidate set:

1. **Substitution or relaxation:** which old node, handoff, or qualification burden widens or disappears?
2. **Complement activation:** which previously non-binding, uneconomical, or low-value complement becomes relatively important because another capability widened?
3. **Interface convergence:** can a shared representation, standard, harness, or qualification path replace many pairwise integrations and turn a fragmented network into a sparse compatible cluster?
4. **Demand expansion or pruning:** does the event activate latent tasks and expose a residual constraint, or does it remove low-value uses and concentrate value in a narrower task set?

When prior project cases are available, run a **negative-case resurrection scan** over relevant conclusions previously classified as `non_cone_network`, `divergent_network`, or `unresolved`. Reopen only cases connected by an edge-level mechanism; do not convert a thematic resemblance into a structural update.

Record the topology direction explicitly. In addition to relaxation and migration, allow a fragmented network to begin converging, an emergent cluster to form, or a market to be pruned while value density rises. Keep current observation separate from a conditional transition: a shared interface demo is not yet adoption, qualification, or vendor rent.

For a capability event, also ask whether the affected workflow can complete a usable learning loop. A local node can widen without producing visible industry change when feedback is slow, hidden inside one organization, difficult to attribute, or blocked by later qualification gates. Read [references/closed-loop-propagation.md](references/closed-loop-propagation.md) when the question concerns diffusion speed, iteration, why a local breakthrough has or has not propagated, or why similar capability shocks produce different structural effects across industries.

## Shared Case Freeze

Before collecting company names, freeze:

```text
Case = (qualified system output Y, transferred function Q,
        product/geography/qualification boundary Omega, observation date t)
```

If `Y` or `Q` is ambiguous, say so. For an open-ended technology-discovery question, this ambiguity is a reason to complete the discovery pass before case freeze, not a reason to guess one industry boundary. Do not manufacture a bottleneck from importance, difficulty, market size, concentration, or a high margin alone.

## Quick Scan

Read [references/quick-scan.md](references/quick-scan.md). Treat the output as a decision demo: one defensible judgment made visible, with a literal memory sentence, one canonical causal journey, evidence limits, and a surviving objection.

The quick scan should normally:

1. Lock the audience decision, question, scope, and non-goals. Treat any early takeaway as a provisional hypothesis; finalize or replace the memory sentence and claim ceiling only after checking evidence and the strongest objection.
2. Draw one functional chain from need to accepted output; include the strongest substitute or bypass.
3. Identify the candidate bottleneck, its current activation, and the likely successor constraint if it relaxes. For a change event, also check complement activation, interface convergence, latent-demand expansion, and market pruning.
4. Separate system dependence from owner capture. Name a company only when the mapping is supportable.
5. Show what is sourced `[F]`, inferred `[I]`, and unknown `[U]`.
6. Check the denominator, unit, state, and dates of any decision-changing number, then run one dedicated counterexample or competing-explanation search when search is available.
7. End with a falsifier, review trigger, and a clear reason to stop or upgrade. If the request supplies one new fact, preserve the dated prior judgment and use the compact evidence-update contract in the quick reference.

Do not build a canonical JSON bundle, exhaustive source catalog, universal score, or formal sealed prediction in quick mode. A valid result may be `cone`, `emergent_cluster_cone`, `cyclical_narrowness`, `non_cone_network`, or `unresolved`.

## Full Audit

Choose the analytical route internally and load only the references it needs:

- For an existing industry or supply chain, use [references/method.md](references/method.md).
- For a new capability or technology shock, use [references/technology-shock.md](references/technology-shock.md).
- For an open-ended technology shock whose affected industries or tasks are not yet known, first use [references/capability-discovery.md](references/capability-discovery.md), then apply the technology-shock protocol separately to the selected candidates.
- When AI, automation, or another capability may change jobs, management layers, firm boundaries, or task jurisdiction, also use [references/organizational-adoption.md](references/organizational-adoption.md).
- For formation, relaxation, migration, or a dated rerun, use [references/dynamics.md](references/dynamics.md).
- For the propagation of a capability change through action, accepted output, feedback, attribution, and reinvestment, use [references/closed-loop-propagation.md](references/closed-loop-propagation.md). Apply it at both the local subloop and parent-industry loop when their clocks differ materially.
- For one new evidence event, preserve the prior hypothesis and use the update protocol in [references/method.md](references/method.md).
- For user-authorized conversation sources, use [references/conversation-mining.md](references/conversation-mining.md); dialogue supplies provenance and hypotheses, not external industry facts.
- For a named company's bargaining power, first locate the system constraint, then use [references/company-capture.md](references/company-capture.md).
- For a sealed time split or formal temporal validation, use [references/temporal-validation.md](references/temporal-validation.md).
- For reports, visuals, snapshots, and expression routes, use [references/deliverables.md](references/deliverables.md).
- When the user asks for a preview, interactive diagram, visual comparison, or a reusable case view, also read [references/visualization.md](references/visualization.md). Quick scans use a compact control picture; full/versioned audits render a standalone HTML view from the validated canonical bundle. Every standalone HTML visual must be checked for evidence parity and tested in a browser for interaction, responsive layout, and readability. The primary agent retains control of facts, topology, claim IDs, and evidence boundaries.

Do not expose these as choices the user must make. Do not mix their evidentiary status: a technology scan is a forecast, a product launch is not adoption, and a customer case is not industry structure or vendor rent.

In a full audit:

1. Split coarse labels until nodes can be independently substituted, qualified, expanded, or rejected.
2. Identify the minimum cut or sparse qualified combination using effective paths, not nominal vendor count or announced capacity.
3. Record whether each material node acts as a **Gate** (pass/reject threshold), a **Leverage** point (small change amplifies broad downstream output), both, or neither. Keep both roles separate from bottleneck activation and owner capture.
4. Separate `B_struct`, `B_now`, `P_joint`, `P_own`, `P_cycle`, `P_now`, and evidence confidence `E`.
5. Locate value definition, constraint encoding, delegation, acceptance, modification, appeal, responsibility, and feedback rights.
6. Trace remote effects edge by edge with transmitted quantity, assumption, counterforce, lag, observable, falsifier, and review trigger.
7. For a claimed technology shock, identify the shortest loop that can learn from the changed node and the parent loop that must close before industry structure visibly changes. Keep operator learning capacity separate from outside-observer visibility.
8. Reconstruct the parent conclusion after zooming in. Revise it if the child graph removes the cut, or if a new shared interface raises compatibility enough for a formerly divergent network to form an emergent cluster.
9. Preserve publication, event, effective, and observation dates; mark `[F]`, `[I]`, and `[U]`.
10. Produce technical and nontechnical views from the same claim ledger.
11. For any claimed relaxation, automation, or rights migration, reconcile scale before and after: output volume, unit labor, total labor or headcount, role mix, organization count, unit cost, and where released capacity was absorbed. Do not infer workforce contraction from lower labor per unit, or system growth from higher throughput alone.
12. In a formal sealed historical split, the t0 evaluator reads only a prebuilt local packet whose bodies, dates, boundaries, and hashes were frozen before the run. Live search, snippets, current page chrome, exact-URL extraction, and later retrospectives are not sealed inputs. Preserve contaminated attempts and rerun in a fresh context.

For reusable, comparative, or versioned work, maintain the canonical bundle defined by [schemas/audit-bundle.schema.json](schemas/audit-bundle.schema.json), then run:

```text
python -m pip install -r requirements.txt
python scripts/validate_audit_bundle.py <audit-bundle.json>
```

The validator runs the Draft 2020-12 schema and semantic cross-checks. PASS means the bundle satisfies the machine contract; it does not validate facts, causality, forecasts, or investment merit.

## Shared Invariants

- High concentration is structural evidence, not proof of an active bottleneck.
- Gate and Leverage are node roles, not synonyms for concentration, scarcity, bargaining power, or each other. A regulator may be a strong Gate with little private capture; a broadly available optimizer may be high Leverage without blocking passage.
- A node can become binding because complements widened around it. Record the upstream or downstream capability, demand, or qualification change that activates the constraint rather than treating narrowness as an intrinsic permanent property.
- A change event can create a bottleneck topology rather than merely move one. Distinguish `current_cone`, `convergence_candidate`, and `formed_cluster`; do not promote a candidate from capability evidence alone.
- Convergence normally occurs around a shared state, interface, module, standard, or acceptance path, not necessarily around one physical technology. Hardware diversity can coexist with interface-level concentration.
- A hard bottleneck does not imply high owner capture; customers, complements, contracts, regulation, and capital risk may absorb the rent.
- Current price is result evidence, not a substitute for the functional chain.
- Announced supply is not relief until compatible, qualified, available, and economical output increases.
- Efficiency may move, disperse, or remove a bottleneck. Record the supported successor state as a named constraint, distributed limits, none visible in the horizon, or unknown.
- A named product is an event anchor, not automatically the technology class or the rent winner.
- Missing evidence remains unknown. Do not fill it with a plausible company name or commercial market-size estimate.
- A later publication is not necessarily a later system event. Keep the dates separate.
- A smaller bottleneck is not necessarily a smaller system. Separate unit intensity, total activity, employment, role composition, organization count, and downstream rebound; record missing denominators as unknown.
- A falsifiable prediction is not automatically observable. Formal validation must preregister expected evidence access.
- A publication-date filter does not seal an information set. Current navigation, snippets, metadata, redirects, and retrospective pages can leak later outcomes even when the target article is old.
- Technical and nontechnical language may differ, but their claim boundary and evidence may not.

## Completion

A **quick scan** is complete when it has a bounded case, one canonical journey, a candidate bottleneck judgment, one bypass or counterforce, system-versus-owner capture separation, evidence limits, a measurement limit for decisive numbers, a traceable counterevidence pass when search is available, strongest objection, successor state or an explicit `unknown/none identified`, a falsifier/update trigger, and a stop-or-upgrade decision. Finding no cone is a successful result.

A **full audit or rebuild** is complete only when it additionally has qualified effective width, rights allocation, zoom reconstruction, dated evidence ledger, remote causal paths where material, technical/nontechnical parity, and the applicable route-specific gate. An open-ended capability-discovery run must also publish its capability decomposition, coverage matrix, candidate ledger, blocked controls, strongest omitted-domain challenge, and stopping rule before narrowing to audited cases. A bounded evidence-event patch may complete under its patch contract without rebuilding the full case; rebuild only when the new fact materially changes `Y/Q/Omega`, the minimum cut, or rights topology. Formal temporal work must also pass the observability preflight and the local-packet isolation gate; otherwise label the result procedural or contaminated rather than a clean forecasting test.

When evaluating or releasing the skill, use [references/evaluation.md](references/evaluation.md). Keep blind cases isolated, retain failed runs, and leave the final holdout untouched until the other release gates pass.

For delegated web research, attach this skill and the selected search skill explicitly. Retry one identical narrow-permission command after a network-sandbox failure when allowed. If evidence remains unavailable, return `tool_blocked` rather than a polished unsupported conclusion.
