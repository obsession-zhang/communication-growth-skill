#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weakness_scorer.py

Score and rank communication flaws from structured conversation data.
Generates a quantitative weakness report with severity rankings.
"""

import json
import sys
from typing import List, Dict

# ─── Scoring Config ────────────────────────────────────────────────

CATEGORY_WEIGHTS = {
    "softness_overload": 3.0,
    "emotional_hijack": 4.0,
    "structural_chaos": 2.5,
    "conflict_avoidance": 3.5,
    "over_explaining": 2.0,
    "under_asserting": 3.0,
    "tone_deafness": 2.5,
    "strategic_blindness": 4.5,
    "reciprocity_failure": 2.0,
    "boundary_collapse": 4.0,
}

SEVERITY_MULTIPLIERS = {
    "critical": 3.0,
    "major": 2.0,
    "minor": 1.0,
}

# ─── Scoring Logic ─────────────────────────────────────────────────

def score_conversation(data: Dict) -> Dict:
    """Score a single conversation for weaknesses."""
    turns = data.get("turns", [])
    scores = {cat: 0.0 for cat in CATEGORY_WEIGHTS}
    findings = []

    for turn in turns:
        # Score softening
        softening_count = len(turn.get("softening", []))
        if softening_count > 0:
            severity = "major" if softening_count >= 3 else "minor"
            score = softening_count * CATEGORY_WEIGHTS["softness_overload"] * SEVERITY_MULTIPLIERS[severity]
            scores["softness_overload"] += score
            findings.append({
                "turn_id": turn["turn_id"],
                "category": "softness_overload",
                "severity": severity,
                "score": score,
                "evidence": turn.get("cleaned_text", ""),
                "details": f"检测到 {softening_count} 处弱化表达"
            })

        # Score emotional leakage
        emotional_count = len(turn.get("emotional", []))
        if emotional_count > 0:
            has_sarcasm = any(e["type"] == "sarcasm" for e in turn.get("emotional", []))
            severity = "critical" if has_sarcasm else "major"
            score = emotional_count * CATEGORY_WEIGHTS["emotional_hijack"] * SEVERITY_MULTIPLIERS[severity]
            scores["emotional_hijack"] += score
            findings.append({
                "turn_id": turn["turn_id"],
                "category": "emotional_hijack",
                "severity": severity,
                "score": score,
                "evidence": turn.get("cleaned_text", ""),
                "details": f"检测到 {emotional_count} 处情绪标记"
            })

    # Calculate totals and rankings
    total_score = sum(scores.values())
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Determine overall health
    if total_score > 50:
        health = "critical"
    elif total_score > 25:
        health = "major_concerns"
    elif total_score > 10:
        health = "moderate"
    else:
        health = "healthy"

    return {
        "conversation_id": data.get("metadata", {}).get("processed_at", "unknown"),
        "total_score": round(total_score, 2),
        "health_status": health,
        "category_scores": {k: round(v, 2) for k, v in scores.items()},
        "ranked_categories": [{"category": k, "score": round(v, 2)} for k, v in ranked if v > 0],
        "findings": sorted(findings, key=lambda x: x["score"], reverse=True),
        "summary": generate_summary(scores, findings)
    }

def generate_summary(scores: Dict, findings: List[Dict]) -> str:
    """Generate a human-readable summary."""
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_issues = [k for k, v in ranked if v > 0][:3]

    if not top_issues:
        return "本次对话未检测到明显沟通缺陷。"

    summary = f"本次对话检测到 {len(findings)} 处问题，总评分 {sum(scores.values()):.1f}。"
    summary += f" 主要问题集中在：{', '.join(top_issues)}。"

    if "softness_overload" in top_issues:
        summary += " 权力姿态偏低，存在系统性弱化行为。"
    if "emotional_hijack" in top_issues:
        summary += " 情绪管理需要加强，存在泄漏风险。"
    if "strategic_blindness" in top_issues:
        summary += " 战略方向需要重新审视。"

    return summary

def compare_conversations(history: List[Dict]) -> Dict:
    """Compare multiple conversations to identify patterns."""
    if not history:
        return {"error": "No conversations to compare"}

    category_trends = {cat: [] for cat in CATEGORY_WEIGHTS}

    for conv in history:
        for cat, score in conv.get("category_scores", {}).items():
            category_trends[cat].append(score)

    patterns = []
    for cat, scores in category_trends.items():
        if len(scores) >= 2 and sum(scores) > 0:
            avg = sum(scores) / len(scores)
            if avg > 5:
                patterns.append({
                    "category": cat,
                    "average_score": round(avg, 2),
                    "frequency": len([s for s in scores if s > 0]),
                    "trend": "persistent" if all(s > 0 for s in scores) else "intermittent"
                })

    patterns.sort(key=lambda x: x["average_score"], reverse=True)

    return {
        "total_conversations": len(history),
        "persistent_patterns": patterns,
        "recommendation": f"优先修正：{patterns[0]['category']}" if patterns else "无明显重复模式"
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python weakness_scorer.py <structured_json_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    result = score_conversation(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
