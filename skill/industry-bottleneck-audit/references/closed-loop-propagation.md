# Closed-Loop Propagation

Use this reference when a technology clearly improves one task but its industry-level effect is uncertain, delayed, hidden, or very different across sectors. It adds a learning-loop lens to the bottleneck topology; it does not replace the functional cut, rights, capture, or evidence analysis.

## Core Distinction

A capability shock changes industry structure only after a usable loop can close:

```text
capability change
-> changed action or unit economics
-> accepted output
-> deployment or distribution
-> outcome feedback
-> attribution to the changed action
-> rule, capital, workflow, or model update
-> next iteration
```

Separate three claims:

1. **Capability:** the new method can perform or cheapen a task.
2. **Local learning:** an operator can use feedback to improve the next attempt.
3. **Structural propagation:** the improvement crosses later gates and changes qualified output, allocation, organization, bargaining power, or the successor constraint.

Do not infer the third from the first. A fast private loop can be nearly invisible to an outside analyst. A slow parent loop can contain fast, valuable subloops.

## Freeze Two Loop Boundaries

For each material event, define:

```text
Local loop = the shortest action -> feedback -> update cycle that includes the changed node.
Parent loop = the cycle that must close before the frozen industry output Y or rights topology changes.
```

Record the interface that connects them. If no evidence shows that local learning crosses this bridge, report `locally_closed_parent_unproven` rather than industry transformation.

Examples of bridge conditions include accepted platform delivery, customer qualification, tape-out, yield ramp, regulatory approval, contract renewal, or budget reallocation.

## Measure Before Scoring

Prefer direct quantities with ranges and denominators:

| Field | Preferred measurement |
|---|---|
| `cycle_time` | elapsed time from changed action to usable feedback |
| `required_gates` | count and identity of independent acceptance or qualification gates |
| `organization_boundaries` | independent organizations that must transfer state or approve passage |
| `iteration_cost` | comparable cash, compute, labor, physical sample, or opportunity cost per loop |
| `feedback_coverage` | share of attempts receiving outcome labels usable for the next iteration |
| `attributed_outcome_share` | share of outcome variation credibly attributable to the changed action, with method stated |
| `deployment_share` | share of qualified output actually using the changed path |
| `reinvestment_rate` | share of savings or gains returned to further adoption, capacity, or experimentation |
| `bridge_conversion` | share of locally improved attempts that cross the parent-loop interface |

If these are unavailable, mark them `[U]`; do not replace a missing denominator with a market-size forecast or a vendor anecdote.

## Ordinal Profile

When direct quantities are incomplete, score eight dimensions from 1 to 5. A high value always means easier loop closure and propagation.

| Code | Dimension | 1 | 3 | 5 |
|---|---|---|---|---|
| `V` | feedback velocity | years / rare cycles | weeks to months | minutes to days |
| `O` | operator feedback observability | sparse or inaccessible | partial proxy | direct outcome telemetry |
| `A` | credit assignability | outcome highly confounded | controlled comparison possible with effort | direct randomized or deterministic attribution |
| `C` | control continuity | many independent owners | a few negotiated handoffs | one operator controls action, feedback, and update |
| `X` | experiment reversibility and affordability | irreversible / very costly | bounded pilot | cheap, repeatable, reversible |
| `I` | interface compatibility | output requires redesign or requalification | adapter and validation needed | drops into an accepted interface |
| `Q` | reward-signal quality | delayed, gameable, or weakly related to value | useful proxy | accepted output or realized value directly observed |
| `S` | successor slack | next gate immediately absorbs the gain | partial room | downstream can absorb substantially more qualified flow |

Also record `O_ext`, the outside analyst's observability, separately from `O`. Never lower the operator's learning capacity merely because public financial reporting is sparse, and never treat a visible dashboard as proof of correct attribution.

## Optional Summary Index

The profile is primary. If a compact comparison is useful, calculate:

```text
LCI = 100 * geometric_mean(V/5, O/5, A/5, C/5, X/5, I/5, Q/5, S/5)
```

`LCI` means **loop-closure readiness under the frozen boundary**, not expected revenue, social value, technological importance, or investment return.

Rules:

- Publish all eight inputs beside the index.
- Use ranges when a material dimension is uncertain; propagate the lower and upper values.
- Compare versions of one case more confidently than unrelated industries.
- Do not interpret a five-point step as equal interval measurement.
- Keep evidence confidence and `O_ext` outside the formula.
- Do not rank owner capture with `LCI`; run the rights and company-capture analysis separately.
- A high local `LCI` with a low parent `LCI` predicts fast local learning but delayed or weak visible industry change.

For a multi-case CSV using `local_profile`, `local_lci`, `parent_profile`, and `parent_lci`, validate the arithmetic with:

```text
python scripts/validate_loop_profiles.py <case-manifest.csv>
```

## RL And Control-Language Boundary

The analogy to reinforcement learning is useful for action, reward, credit assignment, exploration cost, and policy update. An industry is not one optimizing agent: rewards differ across firms, state is private, actions may be strategic, and institutions can veto technically rewarding behavior. Translate the analogy back into named actors, rights, liabilities, and transmitted objects.

## Required Dynamic Output

For a material capability event, report:

1. local loop and parent loop;
2. the bridge between them;
3. direct quantities and missing denominators;
4. `V/O/A/C/X/I/Q/S`, with evidence tags;
5. `O_ext` and the public observables an analyst can actually monitor;
6. local and parent `LCI` only when useful;
7. the next gate likely to absorb released flow;
8. a falsifier: local performance improves but bridge conversion, qualified output, or successor activation does not respond after the natural lag.

For human-facing output, show the loops as nested paths. Put the changed node, feedback return, bridge gate, and successor constraint in the first view; leave the full metric ledger in details.
