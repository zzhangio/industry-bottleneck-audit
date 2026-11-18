# Technology Shock To Structure Protocol

Use this protocol when a new technology or capability is known but its most important industry effects are not. The objective is not to produce a broad beneficiary list. It is to predict where the technology can change effective width, minimum cuts, validation rights, organizational boundaries, and bargaining power.

## 1. Freeze The Shock

Record:

```text
Technology shock T = (demonstrated capability delta dQ,
                      maturity and deployment boundary M,
                      resource and interface requirements H,
                      evidence cutoff t)
```

Keep three layers separate:

- `[H] stipulated`: a hypothetical or user-supplied scenario accepted for conditional analysis, not claimed as externally verified.
- `[F] demonstrated`: observed under named conditions with a source and baseline.
- `[I] transferable`: inference that the result can enter a real workflow or another domain.
- `[U] roadmap`: vendor claim, inaccessible result, or untested future capability.

Do not use a benchmark gain without its task, quality threshold, cost basis, latency, scale, failure rate, and human correction burden. Distinguish capability release from affordable and qualified deployment.

For benchmark-led news, freeze a comparability ledger before carrying the result into the topology: evaluator and funding/provenance, model and dataset versions, the tasks actually shared by every compared system, metric and aggregation, prompt/harness and tool allowances, cost denominator, latency statistic and test region, repeated runs or confidence interval, and whether a matched independent replication exists. Do not count an unopposed modality as a head-to-head win, treat one benchmark's peak score as general accuracy, or let a vendor suite outrank a matched independent suite without an explicit reason.

Use a maturity ladder rather than the word “available” alone:

```text
announced -> demonstrated -> purchasable -> pilot_integrated
          -> qualified_deployment -> scaled_operation
```

`purchasable` proves access to a product or service, not production uptime, workflow integration, qualification, positive unit economics, or repeated deployment.

### 1.1 Freeze The Unit Of Analysis

Do not silently substitute a company or product for the technology shock. Build a functional equivalence map first:

| Layer | Definition | Purpose |
|---|---|---|
| `event_anchor` | The named release, company, paper, regulation, or price event that made the change visible. | Dates the shock and supplies concrete evidence. |
| `core_class` | Implementations that can replace the same bounded task under the same output and quality contract. | The main unit for testing structural relaxation. |
| `adjacent_class` | Narrower or partial implementations that prove one primitive but not the full capability. | Supplies mechanism evidence without overgeneralization. |
| `incumbent_substitutes` | Existing general-purpose, manual, deterministic, or integrated ways to perform the task. | Defines the real price ceiling and counterforce. |
| `excluded_tasks` | Tasks lacking the required boundary, interface, quality, or responsibility conditions. | Prevents category inflation. |

Use the following order:

```text
named event -> capability primitive -> functional equivalence class
            -> old node's effective width -> task/volume migration
            -> successor constraint and rights -> vendor capture
```

The primary technology-level question is whether the class changes the old topology. The secondary company-level question is which implementation captures value. A growing set of substitutes may be positive evidence for `old_cone_relaxed` and negative evidence for any one vendor's `P_capture`; these are not contradictory findings.

Track class-level observables rather than relying on one supplier's revenue:

- share of qualified tasks or volume migrating from the incumbent path;
- number and diversity of interchangeable implementations;
- quality, latency, cost, and failure burden at a fixed acceptance threshold;
- switching, calibration, integration, and monitoring costs;
- whether contracts, organization, responsibility, or feedback ownership change;
- whether the incumbent absorbs the capability and eliminates the need for a separate category.

## 2. Capability Delta Card

Describe direction, magnitude range, boundary, and evidence for each relevant primitive:

| Primitive | Questions |
|---|---|
| Unit cost and capital intensity | Which paid input becomes cheaper, and at what utilization? |
| Cycle time and latency | Which wait or coordination loop shortens? |
| Quality floor and ceiling | Does ordinary output become acceptable, or only the frontier improve? |
| Scale and replicability | Can one qualified result be copied cheaply and consistently? |
| Skill and labor composition | Which expertise is removed, amplified, or moved to review? |
| Physical dependency | Are sites, materials, logistics, instruments, or people bypassed? |
| Modifiability and switching | Can users revise output or change providers without restarting? |
| Verifiability and failure visibility | Is acceptance easier, or are errors cheaper to create but harder to detect? |
| Resource demand | Which compute, memory, energy, data, materials, or complements increase? |
| Rights, liability, and data | Who owns inputs, outputs, responsibility, and feedback after adoption? |

The technology must alter at least one primitive materially before a structural scan is warranted.

### 2.1 Capability Scope And Adoption Position

When the shock affects labor, management, coordination, or organizational boundaries, do not infer organizational replacement directly from task capability. Read [organizational-adoption.md](organizational-adoption.md) and record:

- `capability_scope`: task, job, team, function, firm, or unknown;
- `adoption_position`: beneath an existing worker, beside people as a delegated colleague, between organizational layers as a coordination/monitoring layer, outside the firm as a contractor or service, mixed, or unknown;
- `initiating_actor`: frontline worker, manager, executive, customer, regulator, vendor, or another named actor;
- context and integration burden;
- which delegation, acceptance, modification, appeal, responsibility, and feedback rights move or remain human;
- the observable that would distinguish capability augmentation from jurisdiction migration.

Broader scope is normally harder to build and qualify, yet it can be easier for senior adopters to insert because fewer workers must retrain or rebuild local workflows. Treat this as a conditional adoption asymmetry, not a universal law. Validation burden, physical tasks, tacit context, liability, and incumbent resistance may reverse it.

## 3. Discover Functions Before Industries

If the affected task or industry universe is not already bounded, first run [capability-discovery.md](capability-discovery.md). Do not let the event's marketing category define the search space: a model demonstrated in CAD may expose the same perception-to-action primitive in GUI operation, simulation, laboratory automation, or robotics.

Search for tasks whose current delivery depends on the primitive that changed. Useful exposure archetypes include:

- repeated high-cost production;
- scarce skilled coordination;
- long search, design, simulation, or iteration loops;
- physical presence or bespoke assets;
- expensive failure and slow experimentation;
- manual translation between representations or organizations;
- scarce measurement, qualification, or approval;
- concentrated distribution, attention, data, or feedback;
- high fixed cost with elastic latent demand.

Create a function inventory first, then map each function to industries and specific delivered outputs. A technology that can generate video may touch advertising variants, short dramas, product demonstrations, game previsualization, and training material for different reasons; do not treat “media” as one case.

For every selected function, record which capability primitive is shared with the anchor demonstration and which additional primitive, interface, acceptance threshold, or physical condition could break transfer. Similar words or media formats are not evidence of functional adjacency.

Include at least one plausible but low-impact control case. It tests whether the analysis is merely matching keywords. Common reasons for low impact are a small exposed cost share, strict liability, poor verifiability, low demand elasticity, or an unchanged complementary bottleneck.

## 4. Insertion And Counterfactual Test

For every candidate case, state:

```text
Before: upstream -> old constraint N0 -> qualified output Y
Shock:  T changes primitive p at node or edge e
After:  upstream -> widened/recomposed N0 -> successor state -> Y'
```

Classify the insertion mechanism:

- `replace`: removes an input, task, organization, or physical step;
- `augment`: raises throughput or quality while retaining the operator;
- `standardize`: converts tacit or bespoke work into a reusable interface;
- `make_legible`: improves measurement, prediction, audit, or acceptance;
- `expand_demand`: lowers price or raises quality enough to increase usage;
- `create_dependency`: adds a new required platform, resource, dataset, or approval.

Apply the event in both directions before choosing the main story:

```text
substitution path: event widens or removes an old node
complement path: event makes another node newly useful or binding
convergence path: event reduces many pairwise integrations into a shared interface
demand path: event expands feasible volume or prunes low-value uses
```

A technology can simultaneously substitute for a complement in coarse tasks and activate it in high-precision tasks. Split the task regimes rather than averaging the effects.

Recompute, do not merely relabel:

- `W_eff` at the directly affected node;
- whether a new minimum cut or sparse compatible cluster emerges, remains distributed, or is not yet identifiable;
- qualification and switching friction;
- throughput released into complements;
- definition, validation, modification, responsibility, and feedback rights;
- Gate/Leverage roles before and after the shock, including which widened complement activated the successor;
- `P_joint` of the new cut set and `P_own` of the technology owner.

For a fragmented baseline, also test whether integration complexity changes shape. A useful diagnostic is whether each sensor, supplier, or embodiment still requires a separate implementation for every task (`N x M` pairwise burden), or whether a shared representation/interface allows each side to connect once (`N + M` style burden). Treat this as an engineering hypothesis, not a literal complexity law, and validate it with onboarding time, transfer loss, calibration effort, reusable modules, and qualification evidence.

The most important effect often appears at `N1`, not at the node directly changed by the technology.

## 5. Propagation Gate

Use the following gates and record where evidence currently stops:

```text
capability demonstrated
-> workflow adopted
-> output qualified or accepted
-> unit economics changed
-> volume or demand responded
-> contracts and organization changed
-> bargaining power or rent shifted
```

Do not advance later stages from an earlier-stage source. A release or benchmark can support capability; pilots support workflow; recurring qualified output supports adoption; prices, mix, margins, contracts, hiring, closures, and ownership changes support structural transmission.

## 6. Candidate Screening Axes

Use separate ordinal ranges or prose; do not collapse them into a universal score. For comparable triage, use `0--3`, a range, or `[U]` on each axis:

```text
0 = absent, irrelevant, or contrary evidence
1 = weak/local exposure or major unresolved blockers
2 = material but conditional exposure with a plausible path
3 = direct and material exposure with few unresolved transmission gates
```

Apply the generic anchor in the direction named by each axis. It organizes candidates; it does not turn a forecast into a measured probability.

| Axis | Meaning |
|---|---|
| `X_overlap` | How closely the changed primitive matches a current bottleneck or major cost. |
| `X_share` | Share of qualified output, time, cost, or risk exposed to the function. |
| `A_workflow` | Ease of integration into real operating and responsibility chains. |
| `A_qual` | Tractability of qualification, safety, regulation, and customer acceptance; high means a clearer/easier path. |
| `D_elastic` | Likelihood that lower cost or higher quality expands usage rather than only price competition. |
| `C_slack` | Capacity of complements to absorb released throughput before becoming the next constraint. |
| `R_shift` | Degree to which definition, validation, modification, or feedback rights move. |
| `P_capture` | Ability of the technology owner or adopter to retain value after diffusion and bargaining. |
| `E` | Evidence confidence for the stated forecast. |

A high-impact candidate has strong functional overlap and exposed share, a plausible adoption path, and a material pre/post topology change. High `P_capture` is not required: open or rapidly copied technology may transform structure while commoditizing its suppliers.

## 7. Structural Outcome Library

Use these as hypotheses, not automatic labels:

1. `old_cone_relaxed`: a previously scarce input or task becomes broad.
2. `cone_migrated_downstream`: released flow tightens distribution, validation, service, or demand.
3. `cone_migrated_upstream`: cheap execution raises the value of problem definition, design, or scarce inputs.
4. `new_complement_cone`: compute, energy, data, material, regulation, or human review becomes binding.
5. `cluster_recomposed`: individual components remain broad but the qualified combination changes.
6. `network_convergence_candidate`: a formerly divergent network gains a plausible shared state, interface, module, standard, or acceptance path, but qualified adoption is not yet established.
7. `emergent_cluster_formed`: reusable compatibility and qualification reduce effective paths to a sparse operating cluster even though individual components remain diverse.
8. `market_pruned_value_concentrated`: a stronger substitute removes low-value uses while remaining demand concentrates in harder tasks with higher value density.
9. `organizational_flattening`: a former intermediate deliverable or firm boundary is bypassed.
10. `rebound_amplification`: efficiency expands demand enough to increase total use of a complement.
11. `no_structural_change`: the technology improves a local metric but leaves the minimum cut and rights intact.

Do not label a network converged from a common representation paper or standards announcement alone. Look for cross-hardware or cross-provider reuse, lower integration and calibration burden, repeated adoption, qualified modules, and an observable change in switching or bargaining rights.

## 8. Prediction Register

For each material candidate, publish before outcomes are known:

| Field | Content |
|---|---|
| `prediction_id` | Stable identifier linked to the technology event and candidate case. |
| `candidate_Y/Omega` | Delivered output and boundary that may change. |
| `relaxed_node` | Existing node expected to widen or lose rights. |
| `successor_state` | Named constraint, distributed limits, no visible binding limit, or unknown; include why. |
| `topology_from/to` | Baseline structural class and the conditional or observed destination class. |
| `transition_mechanisms` | Which of relaxation, complement activation, interface convergence, demand expansion, or market pruning carries the change? |
| `shared_interface_or_state` | The reusable representation, interface, module, standard, or acceptance path, or `none/unknown`. |
| `actor_effect` | Who may gain or lose control, with capture kept conditional. |
| `mechanism` | Edge-by-edge transmitted quantity. |
| `horizon` | Near, medium, or long term with calendar dates where possible. |
| `leading_observable` | Workflow, qualification, cost, mix, volume, contract, or organization signal. |
| `counterforce` | What may absorb, delay, or reverse the effect. |
| `falsifier` | Evidence that would reject the direction or mechanism. |
| `status` | speculative / conditional / anchored / contradicted / not-yet-observable. |

Use at least two horizons when lags matter. A correct direction with the wrong timing remains a forecast error worth preserving.

## 9. Compact Output

The minimum human-readable technology scan is:

| Capability change | Exposed function | Candidate industry/output | Old constraint | Predicted successor state | Adoption gate | Horizon | Falsifier |
|---|---|---|---|---|---|---|---|

Then show one before/after path for the highest-priority candidate and one low-impact control case. Only after this should the analysis map named companies, distinguishing technology suppliers, adopters, complement owners, validators, and distribution controllers.

## 10. Example Pattern: Generative Video

```text
Observed capability delta:
lower cost and physical coordination per acceptable minute,
with remaining consistency and human-review limits

Exposed function:
repeatable short-form visual production

Candidate path:
script -> actors/locations/crew -> edited short drama -> platform test
becomes
script/assets -> model/workflow -> human acceptance -> platform test

Predicted structure:
physical production widens;
model controllability becomes a transitional local constraint;
attention, commercial validation, compliance, and feedback become relatively tighter
```

This pattern does not prove that every video industry changes similarly. High-liability, live-performance, prestige, or strongly embodied outputs may remain low-impact controls.
