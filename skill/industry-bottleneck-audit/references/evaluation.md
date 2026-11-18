# Reproducibility And Release Evaluation

Use this protocol to test the skill itself. Do not grade an audit by whether it repeats the maintainer's preferred company conclusion or exact ordinal score. Grade whether it preserves the method's invariants, evidence boundaries, topology, and falsifiability.

## 1. Evaluation Layers

Run four distinct tests:

1. **Schema validation:** required fields, IDs, references, dates, and score ranges are machine-valid.
2. **Invariant validation:** concentration is not equated with a bottleneck; `B` and `P` remain separate; alternatives, unknowns, and falsifiers exist.
3. **Blind reproducibility:** an agent without project history analyzes the same bounded case from the skill and public evidence.
4. **Temporal validation:** a frozen historical evidence set produces predictions that are compared with later evidence.

Passing schema validation alone does not establish analytical quality.

## 2. Blind-Test Isolation

A blind evaluator receives only:

- the installed skill and relevant references;
- a fresh case prompt with `as_of` and research permissions;
- public source access for an ordinary blind current-state run, or a body-only
  local source packet for a formal sealed historical split;
- a dedicated output directory.

Do not provide prior reports, expected bottlenecks, suspected failure modes, baseline scores, or maintainers' conclusions. Record model, reasoning effort, prompt, allowed files, files actually read, search provider, evidence cutoff, and output hashes. If a test agent reads the answer key, mark the run contaminated rather than interpreting agreement as reproducibility.

For a sealed historical split, disable live discovery for the t0 evaluator.
Record raw and normalized packet hashes, body boundaries, packet-builder identity,
selection rules, and every filesystem path actually read. A publication filter,
an exact URL allowlist, or an instruction to ignore later snippets does not make
live web access sealed. If later material appears anywhere in the returned page
or tool output, retain the failed run and replace it with a fresh-context rerun
over a corrected local packet.

### Search-tool execution integrity

A delegated agent must receive the research skill and the selected search skill as explicit inputs. Record the configured command, provider, call count, failures, retries, and whether any fallback was used. When a search call fails because the execution sandbox blocks network access, retry the identical provider command with the narrow permission required by that command before classifying the provider as unavailable. Do not alter proxy, credentials, or provider configuration as part of an evaluation.

Keep a structurally valid but evidence-empty run as `tool_blocked`, not as a completed industry result. The agent should preserve unknowns and fail the research completion gate. If a clean permission-enabled retry is run, retain both artifacts: the first tests failure honesty, while the second tests substantive reproducibility. Never overwrite or silently upgrade the first run.

## 3. Reproducibility Rubric

Compare direction and topology, not prose overlap. Score each item `pass`, `partial`, `fail`, or `not_applicable`:

| Dimension | Pass condition |
|---|---|
| Case identity | `Y/Q/Omega/t` are explicit and materially compatible with the prompt. |
| Granularity | Broad labels are split until nodes can be substituted, qualified, expanded, or rejected independently. |
| Minimum cut | The claimed cut or cluster is connected to accepted output by an edge-level mechanism. |
| Alternatives | At least one credible substitute or counterforce is represented. |
| Effective width | Qualified paths are distinguished from nominal supplier count or capacity. |
| Activation | Structural potential and current activation are not conflated. |
| Event symmetry | A material change event checks substitution, complement activation, interface convergence, and demand expansion/pruning rather than assuming one direction. |
| Topology transition | The report states the baseline class, conditional/observed destination class, mechanism, maturity, and falsifier. |
| Negative-case resurrection | Relevant prior non-cone or unresolved cases are revisited by an edge-level mechanism; unrelated cases are not reopened by keyword. |
| Capture | `P_joint` and named-company `P_own` are separated. |
| Rights | Definition, encoding, acceptance, modification, responsibility, and feedback are located or marked unknown. |
| Zoom consistency | The child graph reconstructs or explicitly overturns the parent conclusion. |
| Evidence | Facts trace to sources; inference and unknowns remain visible. |
| Falsifiability | Major claims have observable invalidating results and review triggers. |
| Expression parity | Technical and nontechnical views use the same claim IDs and do not add unsupported company claims. |

Two reports may pass while choosing adjacent boundaries. Treat a boundary difference as analytical disagreement only if both claim to answer the same `Y/Q/Omega/t`.

## 4. Agreement Measures

Do not use lexical similarity. Record:

- exact or compatible case-boundary agreement;
- structural-class agreement;
- overlap of minimum-cut node functions, allowing different labels;
- direction agreement for `B_struct`, `B_now`, `P_joint`, and `P_own`;
- agreement on the main acceptance right and strongest counterforce;
- overlap of largest unknowns and falsifiers;
- unsupported factual claims and unresolved citations per report.

An ordinal score difference of one band is not automatically a failure when the prose anchor and uncertainty range overlap. A report fails reproducibility when it reverses the topology or rights direction without naming a different boundary or contrary evidence.

## 5. Sealed Time-Split Test

To test prediction without waiting for calendar time:

1. Select a historical case with meaningful later structural evidence.
2. Build a source packet whose publication and effective dates end at `t0`.
3. Have the evaluator register relaxed nodes, successor constraints, actor effects, horizons, observables, and falsifiers.
4. Freeze and hash the prediction artifact.
5. Reveal evidence from `t1 > t0` without changing the original boundary.
6. Classify each prediction as supported, weakened, falsified, boundary changed, not due, or attribution unresolved.
7. Penalize post-hoc escape conditions that were not registered at `t0`.

Step 2 passes only when the packet bodies themselves are local and frozen before
the evaluator starts. URLs, snippets, date-filtered searches, and current
archive pages are packet-construction inputs, not evaluator inputs.

Before freezing the prediction artifact, run the observability preflight in `temporal-validation.md`. A prediction may appropriately require private data, but the release evaluation must not be dominated by decisive observables that were never realistically obtainable. Register sourceability without inspecting later outcomes, and include at least one matured public or authorized test beyond capability/announcement evidence.

Use at least one negative or no-structural-change case. Otherwise the test rewards narrating every technology event as disruption.

## 6. Held-Out Generalization

A held-out case must not have shaped the current schema or examples. Keep it unread and unreferenced during skill revision. The test passes only if:

- no new core field is required to express the case;
- the agent can validly conclude `non_cone_network`, `cyclical_narrowness`, or unresolved;
- domain-specific detail fits in node, edge, evidence, qualification, rights, or prediction records;
- the completion gate is enforced rather than bypassed for a polished narrative.

If a new domain repeatedly needs the same missing concept, add it only after adjudicating whether it is a true cross-domain invariant or a domain-specific reference module.

## 7. Two-Depth Trial Smoke Gate

Use this gate for the trial release that exposes only `Quick Scan` and `Full Audit`. It does not replace the version 1.0 release gate.

Run at least these routing and honesty checks:

| Prompt shape | Expected depth | Pass condition |
|---|---|---|
| First look at an industry, company, or technology | Quick Scan | Produces one bounded decision card without exposing internal route names or requiring the full canonical bundle. |
| Explicit request for a deep, auditable, or formal report | Full Audit | Enters the full workflow directly; it does not force a preliminary quick artifact. |
| New or poorly defined technology said to lower cost | Quick Scan | Marks the event as demonstrated `[F]` or stipulated `[H]`, states the comparison baseline, acceptable-output threshold, deployment maturity, and first unsupported transmission step. |
| New capability may make a fragmented complement viable | Quick Scan | Tests both substitution and complement activation, distinguishes a convergence candidate from a formed cluster, and names observable compatibility/adoption evidence. |
| One new fact updating an earlier case | Quick Scan update | Preserves the dated prior judgment, identifies the affected premise or edge, separates observed change from expected change, and states whether a full rebuild is required. |
| Search or source access is unavailable | Either depth | Returns a `tool_blocked` or evidence-insufficient result with decisive unknowns; it does not simulate completed research. |
| Decisive statistic with mixed dates, units, or populations | Quick Scan | States one measurement limit and does not equate capacity with output, completed cohorts with current applicants, or component price with system cost. |
| Plausible contrary case exists | Quick Scan | Records one dedicated counterevidence query, strongest result, source independence, and whether the result changed the boundary or verdict. |

Grade each artifact against its selected depth. Do not fail a Quick Scan merely because it omits the full topology, rights matrix, score stack, or versioned bundle. Do not relax the Full Audit completion gate because the two-depth interface is simpler. Explicit depth overrides default routing; internal domain protocols remain invisible to the user.

The trial is acceptable only when all listed checks pass or have a documented, non-critical limitation, and a clean reviewer finds no route that silently converts company-node mapping into retained bargaining power.

### Quick Comparative Evaluation

Operational smoke tests establish that the workflow can run; they do not show that it outperforms an ordinary analysis. For a comparative test, use fresh sessions with the same question, source-access boundary, time budget, and tool budget. Randomize or blind the evaluator to whether the answer used the skill. Include several domains and negative controls: no stable bottleneck, regional multi-gate systems, insufficient data, and a technology shock that remains stipulated rather than observed.

Grade factual accuracy, traceability, current activation, alternatives, structure-to-rent overreach, decision increment, time cost, and repeat-run variance. Do not score document length, terminology coverage, agreement with the maintainer, or presence of a predetermined winner. Retain failures and label a single application run `smoke_test`, never `validated_effect`. Keep any designated final holdout isolated until the applicable release gates permit it; the public package does not identify private holdouts.

## 8. Release Gate

Version 1.0 requires all of the following:

- the canonical audit bundle schema and semantic validator pass;
- at least three uncontaminated blind runs cover physical, digital/platform, and stochastic or regulated systems;
- at least two independent runs on one bounded case agree on topology and rights direction or produce an adjudicated, evidence-based disagreement;
- at least one sealed time-split test completes the full prediction-to-outcome cycle;
- that time split contains at least one matured, decision-relevant outcome that is adjudicable from a source class registered before reveal; a hash-correct split dominated by unavailable private evidence is a procedural pass only;
- at least one live evidence-event update preserves the prior hypothesis and separates observed from expected change;
- at least one event-driven blind run begins from a prior `non_cone_network`, `divergent_network`, or `unresolved` case and correctly distinguishes no change, convergence candidate, and formed cluster without being told which outcome to prefer;
- one held-out final validation completes without changing core schema fields;
- company capture is tested separately from system bottleneck strength;
- technical and nontechnical views trace to the same claim ledger;
- no unresolved critical validator error, citation break, or contaminated evaluation remains.

Do not require a universal weighted score, exhaustive industry coverage, stock recommendations, or real-time market data for 1.0.

## 9. Evaluation Record

Retain for every run:

```text
eval_id, started_at, model, reasoning_effort, prompt_hash,
skill_version_or_hash, allowed_inputs, files_read, search_provider,
evidence_cutoff, output_paths, validator_result, contamination_status,
search_calls, permission_retries, research_status, rubric_result,
disagreements, adjudication, and next_action
```

For sealed splits additionally record:

```text
packet_builder, source_selection_rule, packet_manifest_hash,
raw_artifact_hashes, normalized_body_hashes, body_boundaries,
live_discovery_disabled, exposed_items, rerun_of
```

Keep failed and contaminated runs. They are evidence about the skill, not disposable drafts.
