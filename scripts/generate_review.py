#!/usr/bin/env python3
"""Generate a conservative, explainable decision-review package from an observation envelope.

This generator does not claim autonomous aesthetic judgment. It converts observed evidence into a
structured review scaffold, exposes uncertainty, and leaves implementation and deployment authority false.
"""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def inferred_tokens(observations: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    tags = sorted({tag for item in observations for tag in item.get("tags", [])})
    kinds = sorted({item["kind"] for item in observations})
    return {
        "visual": {
            "observed_kinds": [kind for kind in kinds if kind in {"visual", "code", "accessibility", "performance"}],
            "candidate_tags": tags,
            "status": "requires-human-calibration"
        },
        "strategic": {
            "decision_pressure": "unknown-until-reviewed",
            "evidence_coverage": len(observations),
            "status": "hypothesis-not-fact"
        },
        "narrative": {
            "decision_prompt": "supplied-by-observer",
            "status": "requires-contextual-reading"
        }
    }


def build_review(envelope: dict[str, Any]) -> dict[str, Any]:
    repository = envelope["repository"]
    revision = envelope["revision"]
    observations = envelope["observations"]
    evidence = [
        {
            "id": item["id"],
            "kind": item["kind"],
            "source": item["source"],
            "observation": item["statement"],
            "confidence": item["confidence"]
        }
        for item in observations
    ]
    strongest = sorted(observations, key=lambda item: item["confidence"], reverse=True)[:3]
    review_id = f"{repository.replace('/', '--')}--{revision[:12]}"
    return {
        "review_id": review_id,
        "subject": {
            "repository": repository,
            "revision": revision,
            "decision": envelope["decision_prompt"]
        },
        "evidence": evidence,
        "tokens": inferred_tokens(observations),
        "strategies": [
            {
                "id": "preserve-and-clarify",
                "thesis": "Preserve the current design grammar while removing ambiguity and improving legibility.",
                "choices": ["retain recognizable system DNA", "reduce unresolved hierarchy", "prefer reversible changes"],
                "effects": ["lower implementation risk", "clearer evaluation baseline"],
                "risks": ["may underreach if the underlying strategy is wrong"],
                "opportunities": ["reveals whether refinement alone improves the result"],
                "tradeoffs": ["less novelty in exchange for diagnostic clarity"],
                "preserves": ["identity", "existing implementation investment"],
                "sacrifices": ["large directional change"]
            },
            {
                "id": "differentiate-deliberately",
                "thesis": "Strengthen the most specific qualities and remove generic conventions that weaken differentiation.",
                "choices": ["amplify evidence-backed distinctions", "transform references rather than imitate them", "make hierarchy intentional"],
                "effects": ["stronger memorability", "clearer point of view"],
                "risks": ["over-expression", "performance or accessibility regression if spectacle is uncontrolled"],
                "opportunities": ["greater brand and product distinction"],
                "tradeoffs": ["higher craft and validation cost"],
                "preserves": ["core intent"],
                "sacrifices": ["some familiarity and speed"]
            },
            {
                "id": "reduce-to-proof",
                "thesis": "Remove nonessential expression until the value proposition and interaction logic prove themselves.",
                "choices": ["minimize decorative load", "prioritize primary action and evidence", "defer unsupported complexity"],
                "effects": ["better causal learning", "lower operational burden"],
                "risks": ["may erase meaningful atmosphere or emotional value"],
                "opportunities": ["creates a clean baseline for later experiments"],
                "tradeoffs": ["less richness in exchange for stronger proof"],
                "preserves": ["utility", "measurement clarity"],
                "sacrifices": ["ornament", "immersive depth"]
            }
        ],
        "taste_review": {
            "coherence": 0,
            "specificity": 0,
            "proportion": 0,
            "restraint": 0,
            "contextual_fit": 0,
            "craft": 0,
            "disciplined_surprise": 0,
            "anti_taste_findings": ["Not scored automatically; human calibration is required before recommendation."],
            "dissent": "A reviewer should challenge whether the proposed distinctions are genuinely specific or merely stylistic intensity."
        },
        "defense": {
            "central_claim": "The evidence supports review, but not autonomous approval.",
            "strongest_evidence": [item["statement"] for item in strongest],
            "strongest_objection": "The evidence envelope may omit visitor behavior, visual captures, or business context needed for a defensible choice.",
            "response": "Treat the generated package as a decision scaffold and acquire the missing evidence before implementation.",
            "boundary_conditions": ["read-only observation", "no customer-data access", "no implementation or deployment authority"],
            "failure_signal": "A recommendation cannot be traced to cited observations or requires facts absent from the envelope.",
            "mind_change_evidence": "New user evidence, visual evidence, performance data, or a credible competing strategy that better preserves intent with lower risk."
        },
        "bottom_line": {
            "disposition": "defer",
            "recommendation": "Complete human taste calibration and strategy comparison before authorizing implementation.",
            "confidence": 0.5,
            "upside": "The repository now has a reproducible decision scaffold tied to evidence.",
            "downside": "Automated scaffolding can sound more certain than the available evidence warrants.",
            "effort": "low for review generation; variable for evidence completion",
            "reversibility": "high because the workflow is observational and issue-based",
            "cost_of_delay": "limited until a concrete decision deadline is identified",
            "cost_of_error": "potential style drift, wasted implementation, or conversion harm",
            "next_evidence": "Add representative screenshots, route intent, audience context, and measurable current-state behavior."
        },
        "authority": {
            "read_only": True,
            "implementation_authorized": False,
            "deployment_authorized": False
        }
    }


def markdown(review: dict[str, Any]) -> str:
    subject = review["subject"]
    bottom = review["bottom_line"]
    lines = [
        f"# Decision Review: {subject['repository']}",
        "",
        f"Revision: `{subject['revision']}`",
        "",
        f"Decision under review: {subject['decision']}",
        "",
        "## Bottom line",
        "",
        f"Disposition: **{bottom['disposition']}**",
        "",
        bottom["recommendation"],
        "",
        f"Confidence: {bottom['confidence']:.0%}",
        "",
        "## Decision architecture",
        ""
    ]
    for strategy in review["strategies"]:
        lines.extend([
            f"### {strategy['id']}",
            "",
            strategy["thesis"],
            "",
            f"Preserves: {', '.join(strategy['preserves'])}",
            "",
            f"Sacrifices: {', '.join(strategy['sacrifices'])}",
            "",
            f"Principal risk: {strategy['risks'][0]}",
            "",
            f"Principal opportunity: {strategy['opportunities'][0]}",
            ""
        ])
    lines.extend([
        "## Taste calibration status",
        "",
        "Taste scores are intentionally unassigned. Coherence, specificity, proportion, restraint, contextual fit, craft, and disciplined surprise require a human reading of the visual and strategic context.",
        "",
        "## Authority boundary",
        "",
        "This review is observational. It does not authorize implementation or deployment.",
        ""
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    envelope = load_json(args.input)
    review = build_review(envelope)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "decision-review.json").write_text(json.dumps(review, indent=2) + "\n", encoding="utf-8")
    (args.output_dir / "REVIEW.md").write_text(markdown(review), encoding="utf-8")
    provenance = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": os.getenv("GITHUB_WORKFLOW_REF", "scripts/generate_review.py"),
        "source_repository": envelope["repository"],
        "source_revision": envelope["revision"],
        "authority": "read-only"
    }
    (args.output_dir / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
