---
name: product-design-image-template
description: Create, explain, and operationalize reusable Product Design image templates from a user-supplied PNG reference. Use when a user wants a reusable visual generation template, asks how image templates work, or wants to turn a reference image into a repeatable design workflow.
metadata:
  short-description: Build reusable Product Design image templates from PNG references
---

# Product Design Image Template

Create a reusable visual recipe from a user-supplied PNG reference. The result must tell another agent what to preserve, what may vary, when to use the template, what inputs are required, and how to verify that generated results still belong to the intended design system.

## Scope and stopping conditions

- This skill creates a template specification and, when the Template Creator capability is available, registers or exports that template through the available creator workflow.
- Do not claim that a template was registered, published, installed, or made available to Product Design unless the relevant tool returns a successful result.
- Do not begin visual generation or implementation before the reference image has been uploaded or a readable local image path has been provided.
- Do not infer visual properties from a filename. Inspect the actual image.
- If the reference cannot be inspected, stop and report the access gap.
- If the intended product surface, audience, or reuse behavior is materially ambiguous, ask a short interview before finalizing the template. Do not ask questions whose answers would not change the template.

## First response

When the user asks for a new image template, first explain in plain language that a template is a reusable visual recipe composed of:

- a visual reference;
- stable attributes that remain consistent;
- variable attributes that can change;
- invocation and usage guidance;
- negative constraints;
- output dimensions and quality requirements;
- validation checks.

Then ask the user to upload the PNG reference. Briefly explain that the image will be inspected directly and that a short interview may follow if the intended use is not evident from the reference.

Do not generate concepts, build code, or create a final template before the reference is available.

## Reference inspection

Inspect the PNG directly and record only evidence visible in the image. Classify findings as `OBSERVED`, `DERIVED`, or `UNKNOWN`.

Capture:

- surface type: mobile, tablet, desktop, dashboard, landing page, modal, panel, widget, or other;
- dimensions and aspect ratio;
- layout regions, alignment, hierarchy, and whitespace;
- typography roles, approximate scale, weight, and line length;
- color relationships and contrast intent;
- imagery, illustration, texture, icon, and logo treatment;
- component patterns and grouping logic;
- density, restraint, material language, and visual emphasis;
- visible interaction or state cues;
- motion cues only when the image provides evidence for them.

Do not invent hidden flows, responsive behavior, editable content, brand rules, or interaction states. Mark those items `UNKNOWN` until the user supplies them.

## Minimum interview

Ask only the questions needed to resolve material ambiguity. Prefer a compact interview covering:

1. What product or surface should this template generate?
2. Should the reference preserve its layout, or only its visual language?
3. What must remain fixed across uses?
4. What should be replaceable: content, imagery, audience, device, feature set, or call to action?
5. What output dimensions and fidelity are required?
6. Is the template for exploration, production-quality mockups, or image-to-code handoff?

If the user has already answered a question, do not ask it again. If a safe default exists and does not change the architecture, state the default and continue.

## Template construction

Build the template as a reusable contract with these sections:

### Identity

- name: lowercase, hyphenated, action-oriented;
- purpose: one sentence;
- activation criteria: requests that should invoke it;
- exclusions: requests that should not invoke it;
- status: `draft`, `candidate`, `validated`, or `unverified`.

### Visual invariants

List the design properties that must remain stable. Each invariant must include a reason, for example:

| Invariant | Requirement | Reason | Evidence |
|---|---|---|---|
| Hierarchy | Preserve one dominant task and one primary action | Protects the source's focus | `OBSERVED` |
| Spacing | Preserve generous grouping rhythm | Maintains legibility and calm | `OBSERVED` |
| Surface treatment | Use borders only when spacing and grouping are insufficient | Preserves restraint | `DERIVED` |

Do not elevate an aesthetic preference to a hard invariant unless the reference or user explicitly supports it.

### Variables

Define replaceable inputs with names, types, defaults, and constraints:

| Variable | Type | Required | Default | Constraint |
|---|---|---:|---|---|
| `product_surface` | enum/string | yes | `desktop web app` | Must identify the intended surface |
| `audience` | string | yes | none | Must name the primary user |
| `primary_goal` | string | yes | none | One focused user outcome |
| `content_theme` | string | no | source-aligned | Must not change hierarchy |
| `reference_assets` | image list | no | source-aligned | Must match the established art direction |
| `target_dimensions` | dimensions | yes | source aspect ratio | Never stretch or squash the composition |

### Usage prompt

Provide a copy-ready prompt or structured invocation that includes:

- the product, audience, surface, and goal;
- the target dimensions;
- the stable visual invariants;
- the allowed variables;
- the reference image attachment requirement;
- accessibility and legibility requirements;
- the negative constraints;
- the expected output and fidelity level.

When a visual reference is available, attach the actual image. Do not replace the attachment with a text-only description.

### Negative constraints

Include only constraints supported by the reference, user brief, or Product Design quality requirements. Typical constraints may include:

- do not add feature-inventory UI merely to fill space;
- do not create cards inside cards or make every row a card;
- do not invent product features, metrics, tabs, filters, or navigation;
- do not use generic placeholders where the reference implies custom imagery;
- do not distort, stretch, or crop the source composition without authorization;
- do not use inaccessible contrast, unreadable type, or clipped content;
- do not replace real icons or imagery with emoji, text glyphs, or improvised decorative shapes;
- do not imply a production-ready interaction or responsive state that was not validated.

### Output contract

State:

- required viewport and aspect ratio;
- number of outputs, if applicable;
- whether outputs are exploratory, reference-quality, or implementation-bound;
- required states or variants;
- asset and typography expectations;
- whether the approved reference is the visual source of truth;
- what the output does not prove.

## Validation

Validate the template with at least two realistic prompts: one close to the source and one that changes an allowed variable. Check:

- the visual hierarchy remains intact;
- variable substitution does not invent unrelated features;
- composition fits the requested dimensions without distortion;
- typography remains readable;
- contrast and interaction cues remain accessible;
- the result stays within the source's visual language;
- unknowns remain labeled rather than silently filled in;
- the output can be handed to a human or image-to-code workflow with its provenance intact.

If image generation is available, generate exactly the number of variants requested by the active Product Design workflow. Stop for user selection when the workflow requires a visual target before implementation.

## Receipt

Return a concise artifact receipt:

```markdown
## Product Design Image Template Receipt

- Template: `...`
- Status: `draft | candidate | validated | unverified`
- Reference: `filename or attachment identifier`
- Intended surface: `...`
- Intended user: `...`
- Primary goal: `...`
- Stable invariants: `...`
- Variables: `...`
- Output contract: `...`
- Validation performed: `...`
- Remaining unknowns: `...`
- Registration/export result: `confirmed | unavailable | failed`
- Reopen condition: `...`
```

Keep the distinction between the template specification, the source image, generated outputs, and any registered Product Design artifact. A generated image is not proof that the template has been registered; a registered template is not proof of visual fidelity until it has been exercised against representative inputs.

