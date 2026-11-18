# Temporal Validation: Sealed Splits And Incremental Updates

Use this module when the objective is to distinguish a static structural story from a dynamic mechanism. It uses the existing canonical fields `events`, `snapshots`, `hypotheses`, and `predictions`; do not add a core schema field merely to run the test.

## 1. Two Different Tests

### Sealed time split

A sealed split tests whether information available at `t0` was sufficient to predict later structural evidence at `t1`. Freeze the source packet, evaluator prompt, boundary, prediction artifact, and hashes before opening the reveal packet.

### Incremental evidence update

An incremental update tests whether one new fact changes a prior hypothesis in the expected way. Preserve the previous claim and version; classify the update as `strengthen`, `weaken`, `condition`, `refine`, `falsify`, `no_change`, or `rebuild_required`.

The same later source may be used in both tests, but the records answer different questions. The sealed split grades forecasting; the incremental update grades belief revision discipline.

## 2. Freeze The Information Set

Record:

```text
information_set_id, source_ids, publication_date, event_date,
effective_date, accessed_at, t0_cutoff, Y/Q/Omega,
prompt_hash, source_packet_hash, evaluator_model
```

Exclude undated dynamic documentation unless an archived or versioned record establishes its `t0` state. A later page describing an earlier event belongs in the reveal set unless its earlier contents are independently frozen.

### Historical packet construction gate

For a **formal sealed split**, build the t0 packet before starting the evaluator.
The evaluator must not use live web search, search snippets, current pages, live
URL extraction, related-link navigation, or an archive page whose surrounding
chrome can contain later outcomes. Date filters and exact old-looking URLs are
insufficient because search indexes, redirects, metadata, recommendations, and
page furniture are current.

Use this sequence:

1. Define source-selection rules from `Y/Q/Omega/t0` before inspecting reveal
   outcomes: allowed source classes, date rule, minimum coverage, exclusions,
   and stopping rule.
2. A packet builder retrieves candidate documents. Keep the original bytes or
   an archived snapshot, and verify title, issuer, publication date, document
   identity, and body completeness.
3. Separate the historical body from current navigation, recommendations,
   related links, comments, ads, dynamic metadata, and later annotations. Never
   silently repair or paraphrase the body.
4. Store raw and body-only artifacts locally. Record a manifest with source ID,
   original URL, archive/version identity, publication and event dates, capture
   date, inclusion/exclusion reason, body boundaries, raw hash, normalized-body
   hash, and every redaction or conversion operation.
5. Freeze and hash the packet manifest and evaluator prompt. Give the evaluator
   read-only access to that packet and its permitted skill references only.
6. A missing or failed document remains missing. Do not let the evaluator search
   for a substitute, because discovery itself can reveal outcomes.
7. Freeze and hash the prediction artifact before opening the t1 reveal packet.

Prefer static official PDFs, filings, statutes, archived snapshots, and
content-addressed local copies. A current page that truthfully recounts an early
event is still a reveal-period source unless its t0 version is independently
frozen.

For an ordinary historical reconstruction that is **not** being scored as a
sealed forecast, live research may still be used with publication-date and
version checks. Label it retrospective and do not claim temporal isolation.

### Leakage adjudication and rerun rule

Treat exposure to any later outcome, retrospective summary, search snippet,
current related link, answer key, sibling result, or prior conclusion as
contamination even when it was not cited. Record:

```text
contamination_status, exposed_item, exposure_time, route,
whether_used, affected_artifact, disposition
```

Do not erase the run or downgrade the incident to a citation issue. Retain it as
a failed isolation artifact. If a clean score is still required, start a new
agent with fresh context and a corrected local packet; do not continue the same
agent after asking it to ignore what it saw. A body-only packet can cure page
chrome for a future run, but it cannot retroactively unsee leakage.

The evaluator receives only the `t0` packet and the skill protocol. It must not read the current report, later sources, baseline answer, or expected outcome.

### Canonical evidence dependencies and later verification

A sealed hypothesis version's `evidence_ids` identifies the supporting information
for that version, not an ever-growing list of later verification material.
A snapshot includes its own evidence, the evidence of its listed claims and nodes,
and the evidence of the **exact** `(hypothesis_id, hypothesis_version)` referenced
by each listed claim. Publication dates are checked against that snapshot's
`evidence_cutoff`; unknown dates produce a warning rather than fabricated certainty.

Preserve old claims and hypothesis versions. Record subsequent verification in a
dated event and, when revising the hypothesis or its supporting evidence, a new
hypothesis version and claim ID. A later snapshot can reference that new claim.
A `no_change` event may retain the prior version and keep later verification in
the event's `source_ids`, without rewriting the old version's supporting evidence.
Do not pull all events or the newest hypothesis version into an older snapshot.

Future prediction windows, review triggers and `registered/not_due` hypotheses
remain valid. A speculative inference may have no supporting evidence yet.
Unreferenced future sources and later snapshots may coexist with an earlier
snapshot in the same bundle; there is no global ban on dates after `case.as_of`.
The date check addresses a sealed historical information set, not whether a
forecast is true or due. A later access date alone does not establish leakage;
publication dates and source-version provenance still require human scrutiny.

## 3. Register Dynamic Predictions

For each predicted mechanism, write the full path:

```text
event or capability delta
-> directly relaxed node
-> released quantity
-> adoption gate
-> qualified output response
-> successor constraint
-> rights or rent-capture response
```

Register separately:

- capability prediction;
- adoption prediction;
- qualified-output or cost prediction;
- successor-constraint prediction;
- organization or rights prediction;
- scale and labor-balance prediction: output volume, labor per unit, total labor/headcount, role mix, and released-capacity destination;
- company-capture prediction.

Do not let evidence for an early link confirm a later link. A gateway listing can support accessibility without proving usage; a customer case can support local value creation without proving broad adoption or vendor rent.

For automation or workflow predictions, preregister whether the expected result is
unit-intensity reduction, total headcount reduction, role recomposition,
externalization, downstream expansion, or scale absorption. These are different
predictions. Record a comparable denominator and do not use industry revenue or
transaction growth as proof of employment growth at the relaxed node.

### Observability preflight

Falsifiability is not enough for a sealed evaluation. Before freezing the prompt, audit whether the registered outcome can actually be observed inside the reveal window without privileged access.

For every prediction, register:

```text
decisive observable
expected public or authorized source type
minimum denominator and maturity
availability date
observability class: public / authorized-private / unavailable-private
fallback public proxy, if any, with its own narrower claim and falsifier
```

Private production logs, contracts, reason-coded rejections, renewal cohorts, or matched cost ledgers may remain the correct scientific standard. Do not weaken them after reveal. But a retrospective release test cannot rely mainly on evidence that the evaluator had no realistic way to obtain. Pair private-only claims with separately scoped public observables; never let a proxy confirm the stronger private-data claim.

Before sealing a retrospective split:

- perform a sourceability check using only source categories and archive availability, not later outcomes;
- include at least one matured, decision-relevant prediction whose decisive observable is expected to be publicly or otherwise lawfully accessible by `t1`;
- cover more than an announcement clock: at least one public test should reach qualified adoption, structure, rights, or capture when the case claims those layers;
- keep a negative or low-impact control that is observable under the same evidence regime;
- record private-data dependence separately from forecast confidence.

If the reveal cannot test the decisive registered thresholds, classify the result as `testability_unresolved`. Preserve edge-level evidence, but award only a procedural pass; do not report forecast success merely because the direction looks plausible.

## 4. Cost-Shock Clock

For a unit-cost or latency shock, use at least four clocks:

| Clock | Observable | Typical interpretation |
|---|---|---|
| `L0 capability` | price, latency, interface, measured quality | The technical delta exists. |
| `L1 integration` | SDK, gateway, qualified workflow, migration time | The delta is accessible. |
| `L2 adoption` | sustained task share, active organizations, renewal | Organizations actually use it. |
| `L3 structure` | removed handoff, changed staffing/contract, new queue, shifted acceptance right | The industry topology changed. |
| `L4 capture` | retained price, margin, allocation, data or contract control | A named actor captures the change. |

At `L3`, pair the topology observation with a scale balance. A removed handoff
can coexist with higher total employment when lower unit cost expands volume, or
with unchanged apparent headcount when work is externalized to another actor.

Evidence at `L0-L1` must not be reported as `L3-L4`. State the natural lag and minimum sample needed for every clock.

## 5. Reveal And Adjudicate

Reveal later evidence in dated batches. For each prediction, classify:

- `supported`: the registered observable changed in the expected direction;
- `weakened`: evidence moves against the mechanism but is not decisive;
- `falsified`: the invalidating result occurred after the natural lag;
- `not_due`: the horizon or required maturity has not arrived;
- `boundary_changed`: `Y/Q/Omega` genuinely changed;
- `attribution_unresolved`: the outcome changed but the claimed mechanism is not identified.

Score edge by edge. A prediction can be supported at integration and `not_due` at organizational structure. Do not average these into one success score.

Penalize escape conditions introduced only after the reveal. If the original boundary was wrong, record `boundary_changed`; do not rewrite the old prediction.

## 6. Incremental Update Record

For one new event, retain:

```text
baseline_hypothesis_id/version
new_event_id and dates
direct fact established
affected premise or edge
update relation
observed change
expected next change and horizon
unchanged claims
falsifier or rebuild trigger
```

Use `no_change` when the event is already implied, outside the boundary, too early, or offset by a registered counterforce. Use `rebuild_required` only when the event changes the delivered output, functional object, qualification regime, or actor topology enough that the old case no longer answers the question.

For a recorded topology transition, bind the claim to distinct before and after snapshot IDs. The before date and evidence cutoff cannot be later than the after values. Two snapshots may share a calendar date when an event creates two separately sealed information states, but they must have different IDs and review notes; one snapshot cannot prove both sides of an observed transition. Trace transition evidence through its referenced claims and their exact hypothesis versions before applying the after-snapshot cutoff.

## 7. Minimum Deliverables

1. Frozen local `t0` source packet, body-boundary manifest, and evaluator prompt,
   with raw/body hashes and source-selection rules.
2. Prediction artifact plus SHA-256 hash.
3. Dated `t1` reveal packet kept inaccessible to the evaluator.
4. Edge-level outcome adjudication.
5. One incremental update preserving the prior hypothesis version.
6. A manifest recording isolation, model, files read, hashes, and any contamination.
7. An observability manifest showing which decisive outcomes were expected to be public, authorized-private, or unavailable-private at the reveal date.
8. A contamination record that identifies every exposed item or explicitly
   states that the evaluator had no live discovery path.

Keep negative outcomes. A result of “integration supported, structure not due” is more informative than declaring the technology either transformative or irrelevant.
