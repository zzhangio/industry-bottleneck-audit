# Method Protocol

## 1. Case Identity

Record the full object before scoring:

```text
Score(node | Y, Q, Omega, t)
```

- `Y`: qualified system output that customers, operators, or regulators actually accept.
- `Q`: function transmitted by the node, such as qualified die, memory bandwidth, legality, measurement confidence, or deployable service.
- `Omega`: product family, geography, customer qualification, design-freeze state, operating regime, and exclusions.
- `t`: observation date and evidence cutoff.

Different `Y`, `Q`, or `Omega` means a different case even when the industry label is unchanged.

### Split Broad Industry Labels First

Before drawing one industry graph, build a short classification table by delivered function, product or process family, supply mode, geography, qualification state, and customer segment. Analyze materially different rows as separate cases. Do not average them into an unweighted “industry bargaining power” score.

Distinguish two kinds of movement:

- **Strict zoom:** child nodes still explain the same parent `Y`; their functions compose into the same parent `Q`.
- **Bridge case:** the analysis crosses into another system output, such as moving from an input service to the customer's finished output. Create a separate case and claim IDs, then connect the cases with an auditable remote-influence path.

## 2. Node Record

For each candidate node record:

| Field | Audit question |
|---|---|
| `node_id` | Is the identifier stable across future snapshots? |
| `Q_i` | What usable function crosses this node? |
| `K/R/H` | What is selected, how well is the function preserved, and what conditions recover it? |
| `W_eff` | How many qualified, available, economical, substitutable paths exist now? |
| `C_type` | Is concentration in suppliers, region, equipment, material, IP, qualification, policy, customers, or data? |
| `A_i` | How much downstream activity becomes possible after passage? |
| `F_i` | What must be redesigned, requalified, migrated, or relearned to switch? |
| `Gate` | Does this node impose a pass/reject, qualification, capacity, or liability threshold? What releases it? |
| `Leverage` | Does a small improvement here amplify throughput, quality, scope, or coordination across many downstream paths? |
| `activation_dependency` | Which complementary capability, demand increase, or qualification change makes this node relatively binding? |
| `owner` | Which company, department, institution, or coalition controls it? |
| `validator` | Who can accept or reject the output? |
| `state` | Is it simulated, qualified, deployed, approved, or otherwise mature? |

Use effective width rather than nominal supply:

```text
W_eff = sum(capacity * yield * qualification * availability * substitutability)
```

When individually broad components must satisfy an AND relationship, inspect qualified combinations:

```text
W_cluster = sum(compatible * qualified * available * economical * object_maturity)
```

The formulae are decomposition prompts. `object_maturity` means the real candidate path has reached the required simulated, qualified, deployed, clinical, approved, or analogous state. It never means how much evidence the researcher has found. Unknown source coverage stays unknown and must not make the real system appear narrower. Do not invent precision when inputs are ordinal or unavailable.

Stop decomposing when a node is independently replaceable or verifiable, is material to a decision or minimum cut, and has a plausible observable. Merge finer details that neither change substitution/validation nor improve a testable decision. When terminology overlaps, record an inclusion/exclusion table before assigning nodes.

## 3. Structural Classification

- `direct_cone`: few physical or technical paths carry much downstream function.
- `hidden_cone`: apparent supplier breadth hides concentrated equipment, material, IP, data, or qualification.
- `institutional_cone`: permission, standards, liability, procurement, or regulation controls passage.
- `feedback_cone`: failure data and iteration loops accumulate at a controller.
- `emergent_cluster_cone`: components are broad but qualified combinations are sparse.
- `cyclical_narrowness`: inventory or capital cycles temporarily narrow supply.
- `divergent_network`: several routes remain material and constraints diverge by segment or geography.
- `non_cone_network`: multiple viable paths remain and no stable controller is visible.
- `unresolved`: available evidence cannot yet locate or rule out a defensible cut.

Classify the mechanism before discussing a company proxy.

### Gate And Leverage Roles

Do not force every bottleneck into one scalar. Record two orthogonal node roles:

- **Gate:** passage is materially withheld until a threshold, qualification, permission, capacity, or responsibility condition is met. Evidence should name the pass/reject rule, queue, release condition, and decision holder.
- **Leverage:** a bounded improvement at the node propagates into disproportionately broad downstream throughput, quality, scope, or coordination. Evidence should name the amplification path and downstream observable.

Use `none / low / medium / high / unknown` only as auditable ordinal labels. They are not probabilities and must include mechanisms and observables. Typical combinations are:

| Gate | Leverage | Interpretation |
|---|---|---|
| high | high | The node both releases passage and amplifies a wide system; inspect joint control and capture carefully. |
| high | low | A permission, signoff, final acceptance, or liability checkpoint with veto power but little productive amplification. |
| low | high | An optimizer, reusable interface, design method, or coordination layer that expands output without exclusive passage control. |
| low/none | low/none | An ordinary complement; importance alone does not make it a bottleneck. |

A node may change role over time. Memory capacity can be a Gate when a workload does not fit and a Leverage point when bandwidth determines accelerator utilization. Record the dated role, not an eternal label.

Most importantly, identify **relative activation**:

```text
complement widens or demand rises -> flow reaches lagging node
                                 -> Gate activates or Leverage value increases
                                 -> successor constraint or rights shift becomes observable
```

Gate/Leverage does not replace `B_struct`, `B_now`, or `P`. `B` asks whether qualified system output is constrained; Gate/Leverage explains how; `P` asks who can retain value.

## 4. Judgment Axes

Keep these axes separate:

| Axis | Meaning |
|---|---|
| `B_struct` | Bottleneck strength if demand reaches the node's effective structural limit. |
| `B_now` | Degree to which the constraint is active at the cutoff date. |
| `P_joint` | Control exercised by the full complementary cut set. |
| `P_own` | Rent the target owner can retain after bargaining and risk allocation. |
| `P_cycle` | Persistence of capture across an inventory/capex cycle. |
| `P_now` | Current capture under present supply and contracts. |
| `E` | Confidence in the research conclusion. |
| `G_compat` | Density of qualified compatible combinations. |
| `M_object` | Maturity of the industry's object or qualified path. Legacy case files may call this `M_evidence`; it is not research confidence. |
| `Gate/Leverage` | Human-auditable mechanism roles explaining threshold control and downstream amplification; never combine them into the `B/P/E` score. |

Scoring is optional. Use anchored ordinal scores from 0 to 5 only when they clarify comparison inside a fixed case. Apply the `P` anchors separately and explain what control, retained rent, or persistence supports each axis. Never compute an overall score.

| Score | `B_struct` structural anchor | `B_now` activation anchor | `P` capture anchor | `E` evidence anchor |
|---:|---|---|---|---|
| 0 | No relevant structural dependence | Inactive; no measurable output constraint | No identifiable leverage or retained rent | No auditable basis for a conclusion |
| 1 | Weak indirect dependence with easy bypasses | Large slack and no meaningful allocation or delay | Incidental, brief, or immaterial influence | Mostly conjecture |
| 2 | Local structural constraint with practical substitutes | Intermittent or localized pressure | Project-level or short-cycle capture | Case evidence with major gaps |
| 3 | Important to one product family or qualified path | Measurably limits a product, region, or customer class | Repeatable leverage, offset by buyers or cycle | Two evidence types, material blind spots remain |
| 4 | Most viable paths would require the node or cluster | Sustained broad pressure with difficult near-term substitution | Persistently shapes price, contract, or roadmap | Primary and independent evidence broadly agree |
| 5 | Near-single point in the structural minimum cut if demand reaches it | Dominant binding limit on current qualified output | Sustained control of the key path with weak substitutes | Multi-source causal chain and contrary cases tested |

In schema `1.0-draft.1`, use an integer anchor, or a tagged `point`, `range`, `unknown`, or `not_applicable` object with an explanation. Legacy `null` remains accepted during migration but conflates unknown with not applicable. Decimal pseudo-precision is invalid. `E` measures confidence in the stated verdict, not whether that verdict is positive: a well-demonstrated broken hypothesis can have high `E`.

## 5. Three Gates

### Object And Topology Gate

Can the study state `S -> N -> D`, `Y`, and `Q`? Can removing or relaxing `N` plausibly change qualified output? If not, classify the factor as important context rather than a cone.

### Causality And Activation Gate

Distinguish a structural limit from inventory rebuilding, supply discipline, a demand pulse, or a regional outage. Seek utilization, yield, qualification, lead time, allocation, product mix, and substitution evidence rather than price alone.

### Capture And Evidence Gate

Ask whether the node owner controls qualification, switching tempo, failure feedback, contracts, or the next specification. Check customer concentration, capital burden, cancellation rights, regulation, and complement owners before assigning rent.

## 6. Definition And Validation Rights

Map four rights separately:

1. **Value definition:** who knows which failure is costly enough to solve?
2. **Constraint encoding:** who translates value into rules, specifications, process windows, interfaces, or tests?
3. **Acceptance/validation:** who owns the evidence and responsibility to declare the output usable?
4. **Modification:** who can change the design, process, model, or next specification after failure?

Durable bargaining power becomes more plausible when one actor closes several rights with reusable cross-customer feedback. It weakens when each project restarts, data belongs to the buyer, or final validation sits elsewhere.

For each actor, record the form of power rather than only one `P` score:

| Actor | Price/terms | Allocation | Specification | Qualification/acceptance | Modification | Risk burden | Feedback ownership |
|---|---|---|---|---|---|---|---|

This matrix shows where power is distributed and prevents a contract advantage from being mistaken for technical control.

## 7. Remote Influence Ledger

For any distant node claimed to strengthen or weaken the local case, create a stable `claim_id` and record:

```text
origin -> edge-by-edge mechanism -> local node -> observable result
```

Required fields: transmitted quantity, sign, assumptions, evidence per edge, counterforces, lag, observables, falsifier, review trigger, and status (`anchored`, `conditional`, `speculative`, `broken`, or `stale`). The weakest critical edge limits the path's status.

- `anchored`: every critical edge has direct or primary support and no unresolved contrary evidence overturns the path.
- `conditional`: the mechanism is observed, but one or more named assumptions determine whether it reaches the local node.
- `speculative`: at least one critical edge is inference-only or lacks an observable.
- `broken`: a stated falsifier has occurred or a required edge no longer holds.
- `stale`: the review date or trigger passed without a current evidence refresh.

## 8. Zoom Consistency

Zoom in until nodes are independently replaceable or verifiable. Mark links as serial, parallel, AND-qualified, or feedback. Then zoom out and test:

- Does the child graph still explain the same `Y`?
- Can child functions compose into the parent `Q`?
- Are alternatives and side paths preserved?
- Can a parent minimum cut be rebuilt?
- Is a narrow parent actually caused by sparse qualified combinations?
- Are `P_joint` and `P_own` still distinct?
- Did the time regime or evidence maturity change?

If reconstruction fails, change the parent conclusion. Do not force score continuity.

A local cone changes the parent judgment only when it constrains a material share of the same parent `Y`, lies on a required path, or makes the parent qualified-combination matrix sparse. Record the affected output share or path class when measurable; otherwise state it qualitatively and keep the parent effect conditional.

## 9. Evidence Discipline

- `[H]`: stipulated hypothetical or scenario input supplied for forward analysis; internally valid for the scenario but not externally verified evidence.
- `[F]`: directly supported by the cited source.
- `[I]`: inference from facts and the model.
- `[U]`: unknown, conflicting, inaccessible, or not disclosed.

Never use `[H]` to raise evidence confidence for the real world. A later source may convert the same proposition into `[F]`, but retain the original scenario record.

For current industry claims, use the best current evidence available to the task and set an evidence cutoff. This may come from browsing or from a supplied, traceable evidence package. Prefer official statistics, regulators, standards bodies, technical papers, company filings, product documentation, and customer disclosures. Use commercial estimates only with their scope and limitations visible. Every strong concentration, active-shortage, monopoly, or company-capture claim needs traceable evidence and a falsifier.

When the available material is stale, incomplete, untraceable, or insufficient for the claim, produce only a scoping artifact. It may contain case boundaries, candidate paths, hypotheses, unknowns, and a source plan, but it must leave unsupported current activation and capture judgments as `[U]` and state that the completion gate has not been passed.

## 10. Hypothesis And Incremental Evidence Updates

Use this mode for any material new fact: a technical release, qualification result, capacity announcement, shipment or order signal, price move, regulation, contract, customer behavior, accident, failure, or contrary case. The update unit is a versioned hypothesis, not a paragraph of revised prose.

### Baseline Hypothesis Record

Before applying the new evidence, recover or create:

| Field | Meaning |
|---|---|
| `hypothesis_id` | Stable identifier across updates. |
| `version` | Append-only version number or dated version. |
| `claim_ids` | Claims and paths supported by this hypothesis. |
| `baseline_as_of` | Date of the prior state being tested. |
| `hypothesis` | Causal statement, not only a forecast. |
| `premises` | Conditions required for the mechanism to hold. |
| `expected_observables` | What should be seen if it is right. |
| `expected_lag` | Natural propagation time or range. |
| `counterforces` | Mechanisms that can absorb or reverse the effect. |
| `falsifier` | Observation that would materially reject it. |

If no dated baseline exists, label the exercise `baseline_reconstructed`; do not imply that the reconstructed view was genuinely held before the event.

### Evidence Event Record

Record the smallest event that can be independently checked:

```text
event_id, source_id, published_at, effective_at, observed_at,
direct_fact, affected_hypothesis_ids, affected_claim_ids,
update_target, update_relation, system_state_evidence, analyst_note
```

`update_target` is one or more of: `premise`, `causal_edge`, `parameter_or_range`, `counterforce`, `boundary`, `timing`, `outcome`, or `uncertainty`. `update_relation` is one of: `supports`, `weakens`, `falsifies`, `conditions`, `refines`, or `no_change`.

Do not force a score change. First state the prior and revised proposition in words. Change `B_struct`, `B_now`, `P`, or `E` only if the evidence bears directly on that axis. For example, a capacity announcement may lower expected future `B_now` while leaving current activation and structural qualification dependence unchanged.

### Four-Layer Change Test

Keep these layers separate:

1. **Information delta:** what is newly known and how reliable/direct it is.
2. **Belief delta:** which premise or mechanism should be revised now.
3. **Expected system delta:** nodes, edges, actors, prices, or rights expected to change, with sign, magnitude range, and lag.
4. **Observed system delta:** changes already measured; include attribution alternatives.

For technical or product releases, require a propagation chain before changing the industry verdict:

```text
capability release -> workflow adoption -> unit economics or qualification change
                   -> contract, volume, topology, or rent redistribution
```

For policy, supply, demand, or organizational events, adapt the first step but retain adoption/implementation, economic transmission, and capture stages. An announcement or benchmark normally supports only the first stage.

### Expected-Versus-Observed Register

Create one row per material predicted effect:

| Field | Audit question |
|---|---|
| `prediction_id` | Is the prediction stable and linked to an event and hypothesis version? |
| `target_node_or_actor` | Where should the effect appear? |
| `metric_or_observable` | What can be checked without reinterpretation? |
| `expected_direction` | Tighten, ease, migrate, appear, disappear, or recompose? |
| `expected_range` | What magnitude band is material, without false precision? |
| `horizon` | When should it become observable? |
| `dependency` | Which adoption, qualification, customer, or policy condition must occur first? |
| `observed_result` | What happened by the review date? |
| `attribution_status` | Consistent, ambiguous, contradicted, or not-yet-observable? |

At the review date, compare against the recorded expectation before reading the outcome narrative. Update the hypothesis version, retain misses, and distinguish a wrong direction from a correct direction with a wrong lag. A prediction that has not reached its natural lag is `not-yet-observable`, not confirmed or falsified.

### Materiality And Rebuild Rule

Use an incremental patch when the evidence changes one premise, edge, node state, timing assumption, or actor mapping without changing `Y/Q/Omega`. Create a full new snapshot when it changes the minimum cut, adds or retires a material node, reallocates definition/validation rights, changes the system boundary, or jointly alters several major claims. Create a new case when `Y`, `Q`, or `Omega` changes materially.

## 11. High-Variance Portfolio Industries

For content, games, drug candidates, exploration, venture portfolios, and other systems where many qualified attempts still fail commercially, add a portfolio layer. A technically accepted unit is not yet the economic `Y`.

Record at least:

```text
p_success / p_middle / p_fail
payoff distribution and tail concentration
unit production or development cost
discovery, acquisition, trial, or distribution cost
platform/channel take and revenue share
rights, compliance, and carrying cost
how failed attempts update the next attempt
```

Use expected contribution rather than the cost of one successful-looking unit:

```text
EV_portfolio = sum(probability_state * payoff_state)
               - production/development cost
               - discovery/distribution cost
               - rights/compliance/carrying cost
```

Then ask who observes outcome data, who can stop weak attempts early, and who can reuse failure feedback. Falling unit cost may widen production while making attention, trials, distribution, or validation more concentrated. Do not infer improving participant profits from rising output volume alone.
