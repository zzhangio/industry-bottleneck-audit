# Dynamic Bottleneck And Falsification Protocol

Use this reference when the user asks how a bottleneck formed, whether it is loosening, what a new event changes, how power migrates over time, or whether an earlier conclusion was falsified.

Do not use it merely to add a timeline to a static market summary. The objective is a dated causal test.

When the dynamic question is why a capability improvement propagates quickly in one industry but remains local, delayed, or publicly invisible in another, also use [closed-loop-propagation.md](closed-loop-propagation.md). Preserve both the shortest local learning loop and the parent industry loop; they may have different clocks, owners, observability, and successor constraints.

## 1. Preserve The Baseline

Start from a versioned claim:

```text
H_v = (qualified output Y, transferred function Q,
       boundary Omega, observation date t0,
       candidate bottleneck N, mechanism M,
       evidence state, expected review date)
```

Never overwrite the old claim with the new conclusion. Record whether later evidence:

- `supported`
- `strengthened`
- `weakened`
- `falsified`
- `conditioned`
- `boundary_changed`
- `not_due`
- `stale`
- `rebuild_required`
- `no_change`

`boundary_changed` is not a synonym for falsification. It is valid only when the product, function, geography, qualification regime, architecture, or evidence state genuinely changed. A boundary invented after prediction failure is a post-hoc rescue and should weaken the claim.

## 2. Reconstruct The Dynamic Chain

Use human-auditable stages rather than a composite dynamics score:

```text
formation -> hardening -> activation -> capture
          -> counterforce -> relief/bypass
          -> recomposition -> successor constraint
```

For an event-driven rerun, add a topology-state check:

```text
existing cone -> relaxed / migrated / recomposed
distributed network -> still distributed / convergence candidate / formed cluster
wide market -> expanded / pruned with value concentrated / unchanged
```

Ask at each stage:

| Stage | Required question |
|---|---|
| Formation | What repeated demand, technical dependency, rule, or coordination problem first narrowed the path? |
| Hardening | Which installed assets, qualifications, data, contracts, interfaces, habits, or liabilities became costly to reproduce? |
| Activation | What demand, disruption, or policy event made the structural constraint bind now? |
| Capture | Which owner can retain price, margin, contract, allocation, roadmap, or modification rights? |
| Counterforce | Who benefits from opening the waist, and through expansion, standards, substitution, integration, or policy? |
| Relief | Did qualified effective width increase, or did only announced capacity and vendor count increase? |
| Recomposition | Was the function removed, or moved into a new combination of nodes? |
| Successor | Where does released flow arrive next, and what evidence would show that node tightening? |

When the baseline was not a cone, replace “relief” with: what made previously incompatible paths more reusable, economically feasible, or jointly qualified? A dynamic audit must be able to detect cone formation as well as cone dissolution.

## 3. Distinguish Three Kinds Of Change

```text
Cyclical relief
= the same qualified path gains supply or loses demand;
  price, utilization, allocation, or lead time normalizes.

Structural relaxation
= independently qualified substitute paths increase;
  the old node loses veto or switching control.

Structural recomposition
= the function remains necessary but a new architecture,
  standard, organization, or validation chain carries it.

Structural convergence
= a previously fragmented network gains a reusable shared state,
  interface, module, standard, or acceptance path; compatibility and
  qualification concentrate even if physical implementations remain diverse.
```

Do not infer structural relaxation from capex, construction, prototypes, nominal compatibility, a standards announcement, or one successful demonstration. Require evidence that usable paths increased under the frozen case boundary.

Do not infer structural convergence from a representation demo alone. Track cross-path transfer loss, onboarding time, calibration/retraining burden, reusable qualified modules, repeated adopters, interface share, and whether switching or acceptance rights actually moved.

## 4. Register A Causal Response Test

For each important bottleneck claim, register:

```text
Hypothesis:
  Under Omega at t0, N is an active constraint on Y through mechanism M.

Relief event E:
  A concrete intervention or external change that should relax N.

Expected response:
  Within lag L, qualified output Y should increase,
  or predicted successor S should tighten.

Falsifier:
  E occurred, but neither Y nor S responded after L,
  while demand and preregistered controls remained compatible.
```

The `Y increases OR successor activates` rule prevents a common error: when one member of a joint cut is relaxed, another member may immediately bind and hide the output increase. Successor activation supports the original bottleneck mechanism but disproves any claim that relaxing it was sufficient by itself.

Also separate two tests:

- **Bottleneck test:** did relaxing the node change qualified flow or activate a successor?
- **Capture test:** did the node owner retain measurable rent or control?

A node may pass the first and fail the second.

## 5. Freeze Time Constants Before Looking At Outcomes

Use mechanism-specific clocks. Do not use one review interval for every industry.

Possible clocks include:

- demand adoption or inventory correction
- construction and equipment installation
- process yield ramp
- supplier or customer qualification
- software or interface migration
- contract renewal
- policy, permitting, or regulatory review
- clinical maturation or long-term safety follow-up
- organizational hiring and tacit-knowledge formation

Record a range and the event that starts the clock. Until the natural lag expires, use `not_due`, not support or falsification.

## 6. Audit Boundary Stability

The case definition is a modeling choice, but its adequacy is testable. Apply five checks:

1. **Product split:** do allegedly interchangeable products have different functions, qualifications, prices, or failure modes?
2. **Geography split:** are regulation, grid, logistics, sovereignty, or customer approval making supply nonfungible?
3. **Maturity split:** are simulation, prototype, qualified, deployed, approved, and adopted paths being mixed?
4. **Architecture split:** did a new design remove the dependency or only move it to a complement?
5. **Aggregation stress:** does zooming in reveal divergent cycles or minimum cuts that make the parent average misleading?

If a claim succeeds only by switching boundaries after the fact, mark it `weakened` or `falsified`. If an external event genuinely creates a new regime, close the old snapshot and open a new version.

## 7. Handle Stochastic And Regulated Systems

Some systems narrow flow through low transition probability rather than physical throughput. Examples include clinical development, complex safety certification, exploration, scientific discovery, and high-variance content markets.

Represent the path as evidence states:

```text
state j -> validation gate -> state j+1
```

Use the flow identity only as an audit aid:

```text
Flow(j -> j+1) = entrants at state j * transition rate at that gate
```

Rules:

- Compare transition rates only within compatible products, tasks, and maturity states.
- A large candidate count is not large effective width when most candidates have not crossed the relevant gate.
- One success can move one product to the next state without validating the parent platform.
- One failure can identify a local mechanism without disproving every alternative path.
- Claims about repeatability require multiple candidates, independent sponsors, sites, or cycles where feasible.
- Right-censor long observation periods. Pending follow-up is `not_due`, not missing success.
- Keep research confidence `E` separate from the system object's own maturity state.

## 8. Track Rights Migration

For every transition, record whether any of these rights moved:

- value-definition right
- constraint-encoding right
- acceptance or validation right
- allocation or distribution right
- modification right after failure
- liability and responsibility
- feedback-data ownership

Physical relief can reduce one supplier's scarcity while increasing the power of the actor that certifies alternatives, routes flow, or owns downstream feedback.

## 9. Reconcile Scale And Organizational Mass

A relaxed waist can shrink labor per case while the whole system grows enough to
increase total employment. It can also remove one queue while creating a larger
review, sales, compliance, data, distribution, or exception-handling layer. Do
not describe this as simple job destruction or system expansion without a
before/after balance.

For every material dynamic transition, compare the same boundary, unit, and
qualification state at `t0` and `t1`:

| Measure | Required distinction |
|---|---|
| Qualified output or case volume | Applications, units, accepted cases, transactions, or another denominator that composes into `Y`. |
| Unit labor intensity | Worker-hours or role-hours per comparable qualified output. |
| Total labor or headcount | Employment, FTE, contractor hours, or an explicit public proxy; do not derive it from unit labor alone. |
| Role and wage mix | Which jobs shrank, grew, moved to exception review, became more skilled, or were externalized. |
| Organization/site count | Whether work dispersed, consolidated, franchised, centralized, or moved into a platform. |
| Unit and total economics | Unit cost, total operating spend, revenue pool, compensation, or value added where comparable. |
| Queue and service level | Wait time, rejection backlog, geographic reach, or quality threshold. |
| Released-capacity destination | The next node, new demand, quality improvement, lower price, idle capacity, or owner margin. |
| Rebound or induced demand | Whether lower cost or latency expanded total use enough to offset unit savings. |

Use a flow decomposition as an audit aid, not an accounting identity when the
units are incompatible:

```text
total labor at node ~= qualified volume * labor per qualified unit
change in total labor = scale effect + unit-intensity effect + mix/boundary effect
```

Record all three effects. If employment data are available only for a broad
occupation or industry, state the coverage mismatch and do not attribute the
whole change to the bottleneck event. Distinguish employees from establishments,
licensed professionals, contractors, software seats, and transaction volume.

When direct headcount is private, preregister lawful proxies such as occupational
employment, payroll, branch/site count, processing time, cases per employee,
department expense, job postings, or disclosed restructuring. A proxy supports
only its narrower claim.

Classify the observed reallocation:

- `contraction`: total activity and labor at the function both fall;
- `productivity_release`: labor per unit falls and total labor falls or is redeployed;
- `scale_absorption`: unit labor falls but demand growth keeps total labor stable or higher;
- `downstream_expansion`: the old node shrinks while a named complement grows;
- `role_recomposition`: total labor is similar but task, skill, wage, or authority mix changes;
- `externalization`: work leaves the focal organization but persists in vendors, contractors, customers, or users;
- `unresolved`: comparable denominators are unavailable.

Do not force one label when several occur at different layers.

## 10. Hypothesis Ledger Schema

Use these fields for a longitudinal or event-driven case:

```text
claim_id
version
boundary
baseline_date
mechanism
current_status
trigger_event
event_date
topology_from
topology_to
transition_mechanisms
shared_interface_or_state
expected_observable
expected_direction
prediction_window
falsifier
escape_conditions
successor_constraint
rights_shift
scale_balance_expected
evidence_ids
next_review_trigger
```

Keep escape conditions short and preregistered. Do not add an exception merely because an observation was inconvenient.

## 11. Minimum Dynamic Deliverable

A useful dynamic rerun should contain:

1. the dated prior verdict;
2. formation and hardening genealogy;
3. current phase;
4. at least one credible counterforce or relief event;
5. the expected observable response and natural lag;
6. a successor constraint;
7. a separate rights or rent migration judgment;
8. explicit falsifier and boundary-change rule;
9. a versioned hypothesis ledger;
10. a before/after scale balance covering output, unit labor, total labor or headcount, role mix, and released-capacity destination, with unavailable measures explicit;
11. a short statement of what changed, did not change, and is still `not_due`.

For a material capability shock, add the local loop, parent loop, bridge condition, and outside-observer visibility. Do not call a local loop an industry transition until the bridge condition responds.

For the nontechnical route, translate this to:

```text
How did this control point arise?
Who must wait for it today?
What concrete event would open it?
What should visibly change afterward, and by when?
If that happens, who or what becomes the next constraint?
Who gains the right to approve, allocate, modify, or retain feedback?
Did the function become smaller per case, smaller in total, or larger because cheaper throughput expanded demand?
Which roles or adjacent nodes absorbed the released work, spending, or headcount?
```
