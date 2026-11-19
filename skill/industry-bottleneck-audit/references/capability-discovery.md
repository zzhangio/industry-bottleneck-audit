# Open-World Capability Discovery

Use this pass when the user names a new model, technology, policy, cost change, or scientific capability and asks broadly what it could loosen or restructure. The purpose is to discover material candidate task families before a bounded industry audit. It favors recall while keeping evidence status and transfer limits visible.

This pass does not itself prove an industry bottleneck, adoption, bargaining power, or vendor capture.

## 1. Freeze The Capability, Not The Marketing Category

Record the smallest demonstrated delta:

```text
event anchor
observed input -> observed output or action
available tools, scaffold, controller, data, and human correction
quality, latency, cost, repetitions, and failure boundary
evidence cutoff and maturity
```

Decompose the system result before assigning credit. Separate at least:

- perception and state estimation;
- representation translation or grounding;
- planning, search, and decomposition;
- code, tool, or action composition;
- memory and within-episode correction;
- specialist solver, policy, controller, or actuator execution;
- acceptance, safety, and responsibility.

A benchmark or demo establishes only the primitives the setup actually exposes. Do not attribute inverse kinematics, collision avoidance, low-level control, a VLA policy, or a simulator's privileged state to the general model when those remain in the scaffold.

## 2. Identify The Bridge Primitive

State the domain-independent capability that may travel beyond the anchor example. It should be more precise than a model label and more general than an industry noun.

Examples:

```text
visual state -> grounded high-level action -> feedback-guided replanning
natural-language intent -> editable structured artifact -> deterministic checker
weakly structured evidence -> ranked decision -> auditable exception handling
```

Then name the old translation burden it could relax: bespoke interface engineering, task-specific data collection, specialist scripting, manual representation conversion, coordination, search, or another bounded function. Also identify complements that were previously uneconomical or too fragmented to matter but could become usable after that burden falls.

## 3. Scan A Capability Surface

Cross the bridge primitive against different operating regimes rather than brainstorming industry names from memory.

### State and representation

- structured digital state or API;
- visual digital interface;
- editable spatial or simulated world;
- observed physical world;
- contact-rich, deformable, hidden, or partially observed state.

### Action interface

- text, decision, or file output;
- GUI actions;
- code and software tools;
- high-level physical primitives or end-effector goals;
- continuous low-level actuation.

### Feedback and consequence

- open-loop or one-shot;
- intermittent inspect-and-correct;
- fast closed loop;
- precise contact and force control;
- safety-, liability-, or regulation-critical acceptance.

### Learning and adaptation burden

- no task adaptation;
- prompting, examples, or explicit memory;
- reusable skills or tool wrappers;
- task-specific fine-tuning or VLA/policy training;
- embodiment calibration and physical data collection.

Place each candidate task family in this surface. Search empty but plausible cells explicitly. The purpose is to reveal adjacencies such as a visual tool-using model crossing from GUI operation into robot high-level control, while also exposing where continuous dynamics or safety break the analogy.

### Structural direction scan

For each material cell, check four directions rather than assuming the event only replaces an incumbent:

| Direction | Discovery question |
|---|---|
| `relax` | Which existing task, handoff, cost, or gate becomes broader? |
| `activate` | Which dormant complement becomes valuable because the surrounding system is now feasible or larger? |
| `converge` | Does a common state, interface, standard, harness, or qualification path reduce pairwise customization? |
| `expand_or_prune` | Does latent demand create new residual constraints, or does a stronger substitute eliminate low-value uses and concentrate the remaining market? |

The same event can operate in opposite directions across task regimes. Preserve both paths until a bounded case resolves them.

## 4. Build A Candidate Ledger Before Ranking

For every discovered task family record:

| Field | Question |
|---|---|
| `candidate_task` | What bounded function might transfer? |
| `old_translation_burden` | Which scarce integration, training, interface, or expert step existed before? |
| `shared_bridge_primitive` | Which demonstrated capability travels from the anchor case? |
| `extra_requirements` | What new state, interface, latency, precision, or qualification is required? |
| `transfer_evidence` | Demonstrated, adjacent evidence, analogy only, or contrary evidence? |
| `potentially_relaxed_node` | Which old node may widen? |
| `successor_constraint` | What likely binds next? |
| `activated_complement` | Which previously weak or uneconomical complement may become material? |
| `convergence_mechanism` | What shared representation, interface, module, standard, or acceptance path could reduce fragmentation? |
| `topology_transition` | Relaxation, migration, network convergence, cluster formation, market pruning, no structural change, or unresolved? |
| `structural_reach` | Could this alter only unit labor, or also entry, organization, rights, volume, and rent? |
| `case_freeze_needed` | What `Y/Q/Omega/t` must be audited next? |

Keep a candidate even when the likely result is `no_structural_change`; it may be a useful blocked control.

## 5. Search For Mechanisms And Surprises

Do not search only for the event name plus the user's named industry. Search combinations of the bridge primitive and task regime, including terms such as direct policy, zero-shot control, without fine-tuning, tool use, visual feedback, physical in-context learning, closed loop, structured artifact, acceptance, and failure.

Use three evidence passes:

1. **Anchor verification:** establish what the named event actually demonstrated and what scaffold supplied.
2. **Adjacency search:** look for the same bridge primitive in different state/action regimes.
3. **Boundary search:** seek precision failures, latency, safety, qualification, human correction, and cases where a specialist component remains necessary.

Add a fourth pass when prior cases or a case registry exist:

4. **Negative-case resurrection:** search relevant prior `non_cone_network`, `divergent_network`, and `unresolved` cases for an edge-level mechanism by which the new capability changes feasibility, compatibility, qualification, or demand. Record unchanged cases as controls; do not reopen unrelated cases by keyword.

At least one candidate should come from outside the event's marketing category, and at least one plausible candidate should be retained as a low-impact or blocked control. These are coverage tests, not quotas for padding the answer.

## 6. Rank Structural Reach, Not Novelty

Prioritize candidates where the old burden was scarce, repeated, and positioned on many delivery paths; the bridge primitive is supported under comparable conditions; and a change could alter entry, task jurisdiction, organization, volume, or bargaining power. A visually impressive demo with little exposed cost or an unchanged acceptance gate may rank below an ordinary-looking interface change repeated across millions of workflows.

Keep these judgments separate:

```text
capability transfer plausibility
old-node relaxation magnitude
complement activation magnitude
interface convergence plausibility
successor constraint severity
adoption and qualification burden
system-level structural reach
technology-owner capture
```

## 7. Stop And Hand Off To Audits

Open-world discovery cannot prove exhaustiveness. State the declared search surface and use a stopping rule. A reasonable stop is reached when:

- every material state/action regime has been checked or marked not applicable;
- an independent omission challenge produces no new high-materiality bridge primitive or task family;
- a further search round adds only duplicates, weaker examples, or tasks already represented by an existing family;
- the leading candidates and at least one blocked control have enough evidence to freeze separate cases.

Apply a depth-specific budget internally; do not ask the user to select another mode:

- **Quick discovery:** publish at most three ranked task or industry candidates plus one blocked/low-impact control. Cover the material capability regimes, run one explicit omitted-domain challenge, and stop when the next search pass adds no new high-materiality bridge primitive. Apply a compact technology-shock path only to the leading candidate; leave the others as dated hypotheses with observables and falsifiers. Do not silently expand into several full audits.
- **Full discovery:** use the complete stopping rule above, retain the coverage matrix and candidate ledger, and freeze separate `Y/Q/Omega/t` cases for every material candidate selected for audit.

Publish three frontiers:

1. `demonstrated transfer`;
2. `plausible adjacency requiring a bounded audit`;
3. `blocked or unsupported transfer`.

For any convergence claim, also state whether it is only a `convergence_candidate`, an observed compatible cluster, or a qualified operating cluster. Cross-sensor or cross-task transfer in a laboratory can establish a candidate, not an industry waist.

Then select the material candidates. In quick mode, freeze one leading case and return the rest as a shortlist; in full mode, freeze `Y/Q/Omega/t` separately for each selected case. Use [technology-shock.md](technology-shock.md) at the corresponding depth. Do not collapse their acceptance thresholds into one generalized claim.

## 8. Common Failure This Module Prevents

```text
named demo: 3D modeling
premature case freeze: 3D content industry
missed bridge primitive: visual state grounding + tool/action composition + feedback correction
missed adjacency: high-level robot manipulation
remaining boundary: spatial observability, latency, precision contact, low-level control, safety, and physical acceptance
```

The correction is not to add robotics to every 3D report. It is to discover the bridge primitive before choosing which industry reports deserve to exist.
