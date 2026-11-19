# Visual Preview Module

Use this module when the user asks to preview, compare, present, or visually audit a result. The visual is a view over the same claims and evidence as the written analysis; it must not introduce a second conclusion store.

Apply [human-review-compression.md](human-review-compression.md) before laying out a human-facing visual. The full graph may remain available interactively, but the first view must use the compressed decision path rather than rendering every machine-readable node at equal weight.

## Routing

- **Quick Scan:** include one compact control picture in the Markdown result. Prefer Mermaid when the preview surface supports it. Show the main functional journey, one bypass or counterforce, the likely successor constraint, and one audit exit. Do not create a canonical bundle solely to draw a quick result.
- **Full Audit or versioned case:** validate the canonical audit bundle, then render the standalone interactive HTML with `scripts/render_audit_visual.py`.
- **Evidence-event update:** preserve the prior snapshot and show the new fact, changed edge or node, unchanged constraints, expected next change, and verification trigger. Do not redraw a forecast as an observed topology change.
- **Technology-first discovery:** show the demonstrated capability shock separately from candidate industries. Draw a before/after path only for a frozen candidate case.

Generate an HTML artifact when the user explicitly asks for a visual, when the report will be revisited over time, or when clicking through evidence materially improves auditability. Do not generate one automatically for a small chat-only answer.

## Visual Acceptance

Before publishing a standalone HTML visual:

1. Freeze the validated data, focal hierarchy, and claim/evidence boundaries.
2. Check the rendered view against the data. Presentation changes must not silently alter `Y/Q/Omega`, claim text, epistemic status, stable IDs, evidence links, company mapping, falsifiers, or observed-versus-forecast status.
3. Test browser interaction, keyboard access, mobile layout, and overflow. Record the artifact/version, checks performed, disposition, and remaining limitations in the delivery note.
4. Mark unperformed checks as pending. If material checks remain incomplete, deliver a clearly labeled draft rather than claiming acceptance.

These checks are model-independent. Public output needs an accurate acceptance summary, not internal authoring prompts or iteration transcripts.

## Focal Hierarchy Before Layout

Choose the focal output before arranging levels. Do not mix supply-chain distance, technical abstraction, company ownership, and acceptance authority on one flat plane.

### Semiconductor-to-AI upstream view

When the visual question concerns semiconductors, compute infrastructure, memory, packaging, networking, power, or their effect on frontier AI, use the AI model or qualified model capability as the declared **focal total waist** for this project view:

```text
far upstream / slow physical base
materials, energy, equipment and process-enabling capability
-> wafer process, design enablement and fabrication
-> die, memory, package, network and system integration
-> compute cluster / cloud execution
-> AI model training, inference or accepted capability  [focal total waist]
-> product deployment, task acceptance and user/environment feedback
```

- Arrange upstream layers by functional distance from the AI-model waist: the farther the required transformation or qualification chain, the higher the layer.
- Treat “AI model as total waist” as the declared analytical lens, not proof that one model vendor is a monopoly or that every semiconductor node currently binds.
- Show a semiconductor node as an active or latent sub-waist only when its qualified output and bridge into model capability are explicit.
- Do not place optional downstream applications, upstream materials, EDA checks, and model capability at the same hierarchy merely because all are important.
- Preserve zoom-in: each upstream sub-waist may have its own local loop, while the parent loop closes only when model capability or accepted deployment responds.

### Product-delivery and non-AI-parent views

For downstream applications such as AI short drama, or for industries whose qualified output is not an AI model, retain the product-delivery topology:

```text
real demand -> production/decision workflow -> acceptance/distribution
-> realized outcome -> feedback to the next product cycle
```

Do not force semiconductor-style vertical distance onto these cases. Place nodes by their role in delivering and accepting the frozen `Y`.

### Cross-company or cross-industry loops

Draw a cross-boundary loop only when the loop is auditable. Its visible label or drill-down must identify:

```text
evidence producer
-> transmitted evidence/state
-> actor with modification right
-> final acceptor
-> returned result or failure signal
-> bridge condition and natural lag
```

A return arrow without these fields is decoration, not a validated loop. Distinguish local private loops from parent-industry loops and mark the cross-company interface where local learning becomes accepted output.

## Primary View

The first viewport should answer:

```text
What qualified output is being produced?
-> what currently narrows or accepts it?
-> what bypass exists?
-> where does the constraint move if released?
-> what would falsify the picture?
```

Default emphasis:

- highlight the current minimum cut;
- distinguish observed, inferred, conditional, and speculative edges without relying on color alone;
- label arrows with the transmitted object;
- show company names only where the bundle supports a company-node mapping;
- keep scores and technical notation in drill-down details;
- keep the largest unknown and evidence cutoff visible.

Clicking a node should reveal its plain function, owner, qualification, Gate role, optional Leverage role, release condition, substitutes, evidence, unknowns, and company mappings. Claims expose their evidence, falsifier, and review trigger. Sources remain directly reachable.

## Quick Mermaid Pattern

Adapt labels to the actual case and keep the graph small:

```mermaid
flowchart LR
    A[Real demand] -->|required function| B[Candidate constraint]
    B -->|qualified output| C[Accepted delivery]
    X[Substitute or counterforce] -.-> B
    B -->|if released| D[Successor constraint]
    B -.->|falsifier / review trigger| Z[Audit exit]
```

Mermaid is a communication view, not evidence. Attach claim IDs or a short evidence table immediately below it when the result is meant to be audited.

## Full HTML Renderer

Run from the skill directory or provide absolute paths:

```powershell
python scripts/validate_audit_bundle.py examples/minimal-audit-bundle.json
python scripts/render_audit_visual.py examples/minimal-audit-bundle.json output/audit-preview.html
```

The renderer is dependency-free and embeds the input bundle into one local HTML file. It provides:

- interactive functional topology;
- plain/technical detail toggle;
- minimum-cut and alternative-path emphasis;
- claims, timeline/predictions, company mapping, and source tabs;
- node-level evidence, unknowns, falsifiers, and review triggers;
- responsive desktop and mobile layouts.

The renderer does not validate facts or repair an invalid bundle. Validate the JSON first. If the graph contains many nodes, preserve the full interactive artifact but also publish one smaller editorial view that contains only the decision-changing path.

## Snapshot Compatibility

Keep stable `node_id`, `edge_id`, and `claim_id` values across reruns. A later visual may add or retire nodes, but comparison mode must not silently reuse an old ID for a different function. If `Y/Q/Omega` changes materially, create a new case rather than presenting it as an ordinary snapshot update.

## Acceptance Check

- The first viewport identifies the output, minimum cut, largest unknown, and evidence cutoff.
- Every visible factual node or edge traces to IDs in the bundle.
- Conditional and speculative paths are visibly labeled.
- The visual states what remains unknown and what would change the judgment.
- Company capture is not implied by node importance alone.
- Mobile text does not overlap, and the topology remains usable without hover.
- The delivery note identifies the reviewed artifact/version, checks performed, disposition, and remaining limitations.
