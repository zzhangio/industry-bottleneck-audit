# Company Capture And Bargaining-Power Protocol

Use this module only after the system output, functional bottleneck, and qualification boundary are defined. It answers whether a named company or department controls the relevant constraint and can retain value. It does not infer company power from industry importance, supplier concentration, technical prestige, gross margin, or stock performance alone.

## 1. Freeze The Company Exposure

Record:

```text
Company exposure = (company C, segment or department S,
                    controlled node/edge N, system output Y,
                    boundary Omega, observation date t)
```

Do not use the consolidated company when only one segment touches the bottleneck. State revenue exposure, customer set, geography, product generation, and qualification status when public evidence permits. If the organization-to-node mapping is not supportable, use `no_clean_match`.

## 2. Separate Four Questions

1. **System dependence:** Would qualified output fall, slow, or require redesign if this node disappeared?
2. **Company control:** Does the named company control that node, or merely participate in a coalition?
3. **Rent retention:** Can it turn control into price, allocation, contract, data, modification, or boundary-expansion power?
4. **Equity transmission:** Is the exposure material after customer power, capex, cyclicality, segment mix, and competition?

The first three belong to the bottleneck audit. The fourth is a separate financial-research handoff, not an automatic investment conclusion.

## 3. Company Mapping Ladder

| Label | Minimum evidence |
|---|---|
| `strong_match` | The company controls the relevant qualified output or acceptance gate, alternatives are demonstrably costly or slow, and the control maps to a named segment or department. |
| `partial_match` | The company supplies a material input but shares the cut set, lacks final acceptance, or faces credible qualified substitutes. |
| `coalition` | No single company controls the path; compatibility, qualification, or responsibility is jointly held. |
| `no_clean_match` | The mechanism is real but public evidence cannot map it to a named company or organization. |

Never upgrade a mapping because the company is a market leader. Never downgrade a structural bottleneck merely because its rent is divided among a coalition.

## 4. Rights And Contract Matrix

For each named actor, record observable control rather than a generic moat score:

| Right or lever | Audit question | Strong evidence |
|---|---|---|
| Price and terms | Can the actor change price, minimum commitments, cancellation terms, or service scope? | Contracts, repeated price realization, take-or-pay, non-cancellable backlog. |
| Allocation | Who decides which customer receives scarce qualified output? | Allocation notices, reserved capacity, priority tiers, customer prepayments. |
| Specification | Who defines the performance envelope or accepted interface? | Standards role, design rules, platform requirements, product roadmap dependence. |
| Acceptance | Who can approve or reject the output? | Certification, AVL, sign-off, regulatory, platform, or customer qualification authority. |
| Modification | Who can change the design after failure without restarting qualification? | Tool/recipe ownership, change-control rights, field-update rights, requalification burden. |
| Responsibility | Who bears warranty, compliance, safety, or operational loss? | Contract liability, regulatory duty, warranty reserve, indemnity, recall responsibility. |
| Feedback | Who receives failures and can reuse them across customers or generations? | Installed-base telemetry, return analysis, silicon correlation, claims history, workflow outcomes. |

The actor with the highest number of rights is not automatically strongest. Weight rights by whether they sit on the frozen minimum cut and whether customers can redesign, sponsor a second source, vertically integrate, or wait.

## 5. Joint Power Versus Own Capture

Keep these distinct:

```text
P_joint = bargaining power of the qualified combination or coalition
P_own   = share of that power retained by the named company
```

Explain the wedge using:

- customer concentration and procurement leverage;
- dependence on complementary suppliers;
- shared IP, standards, or qualification rights;
- capital intensity, utilization risk, and depreciation;
- second-source sponsorship or vertical integration;
- regulatory or contractual limits on pricing;
- cyclicality and inventory exposure;
- whether failure data and modification rights remain with the customer.

A high `B_struct` with low `P_own` is a valid and important result.

## 6. Economic Transmission Test

Use financial evidence only after the mechanism is named. Reconcile:

```text
structural control
-> observable commercial lever
-> segment revenue/price/mix or contract effect
-> costs, capex, working capital, and risk absorption
-> retained operating economics
```

Useful observables include repeated price realization across cycles, gross-margin resilience relative to mix, backlog quality, non-cancellable commitments, customer prepayments, qualification-linked design wins, service attach, renewal, allocation, switching events, and segment returns on incremental capital.

Weak evidence includes one shortage-quarter price increase, consolidated gross margin without segment attribution, management use of “leading,” market-cap appreciation, analyst target prices, and revenue growth caused only by end-market demand.

## 7. AI And Boundary Expansion

When AI is part of the thesis, ask both directions:

```text
Does AI lower the company's design, search, validation, or service cost?
Does the same AI lower the customer's self-build, substitution, or switching cost?
```

Boundary expansion is supportable only when the company combines AI with an asset competitors cannot cheaply obtain, such as proprietary failure feedback, accepted workflow position, modification rights, customer state, distribution, or responsibility. Generic AI adoption is not evidence of increasing bargaining power.

## 8. Company Record

For each material company mapping, retain:

| Field | Content |
|---|---|
| `company_id` | Stable company or organization identifier. |
| `segment_department` | The unit that actually touches the node. |
| `node_ids` | Controlled nodes or edges in the audit bundle. |
| `mapping_label` | strong_match / partial_match / coalition / no_clean_match. |
| `rights` | Price, allocation, specification, acceptance, modification, responsibility, feedback. |
| `commercial_lever` | Observable mechanism by which control affects terms or economics. |
| `customer_counterpower` | Concentration, redesign, dual-source, waiting, vertical integration. |
| `P_joint/P_own/P_cycle/P_now` | Conditional ordinal assessments with prose anchors. |
| `segment_materiality` | What is known and unknown about financial exposure. |
| `evidence_ids` | Fact-level source links. |
| `falsifier` | Event that weakens company control or retention. |
| `review_trigger` | Date, qualification, contract, competitor, regulation, or architecture event. |

## 9. Falsifiers

At least one falsifier must attack company capture rather than system importance. Examples:

- a second source qualifies without redesign or loss of accepted performance;
- the customer changes allocation or terms despite the supposed constraint;
- a standard removes proprietary compatibility or requalification burden;
- margins collapse after supply normalizes while the node remains technically important;
- customers internalize the function or retain modification and feedback rights;
- a new architecture bypasses the controlled node;
- the relevant segment is too small for the company-level thesis.

## 10. Minimum Company Deliverable

Provide:

1. A one-sentence node-to-company mapping with boundary and date.
2. The rights and contract matrix.
3. `P_joint` versus `P_own`, including customer counterpower.
4. One commercial transmission chain and one alternative explanation.
5. Segment materiality with explicit unknowns.
6. A company-capture falsifier and review trigger.

Do not label a company as a bottleneck when the evidence supports only an important product, a concentrated market, or a strong current cycle.
