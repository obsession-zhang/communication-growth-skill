#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
input_sanitizer.py

Preprocess raw chat/call data into structured conversation format.
Supports: WeChat OCR, voice transcripts, email threads, mixed sources.
"""

import re
import json
import sys
from datetime import datetime
from typing import List, Dict

# ─── Config ─────────────────────────────────────────────────────────

SOFTENING_PREFIXES = [
    "那个", "就是", "其实", "说实话", "说白了", "怎么说呢",
    "不好意思", "打扰一下", "麻烦您", "想请问", "不知道",
    "可能", "也许", "大概", "稍微", "一点点", "能不能",
    "可不可以", "方不方便", "想问问", "想了解一下"
]

POWERLESS_PATTERNS = [
    r"不好意思[，,]?",
    r"打扰一下[，,]?",
    r"麻烦您[了]?[，,]?",
    r"想请问[，,]?",
    r"不知道方不方便[，,]?",
    r"能不能[，,]?",
    r"可不可以[，,]?",
    r"稍微[，,]?",
    r"也许[，,]?",
    r"可能[，,]?",
    r"那个[，,]?",
    r"就是[，,]?",
]

# ─── Core Functions ─────────────────────────────────────────────────

def clean_text(raw: str) -> str:
    """Remove noise while preserving meaning."""
    text = re.sub(r"\s+", " ", raw).strip()
    text = re.sub(r"([！!?？。，,])+", r"", text)
    return text

def detect_softening(text: str) -> List[Dict]:
    """Detect and flag all softening language."""
    findings = []
    for pattern in POWERLESS_PATTERNS:
        for match in re.finditer(pattern, text):
            findings.append({
                "type": "softening_prefix",
                "matched": match.group(),
                "position": (match.start(), match.end()),
                "severity": "high" if match.group() in ["不好意思", "打扰一下", "麻烦您"] else "medium"
            })
    return findings

def detect_emotional_leakage(text: str) -> List[Dict]:
    """Detect emotional markers in text."""
    findings = []
    if re.search(r"[！!]{2,}", text):
        findings.append({"type": "intensity_marker", "severity": "medium"})
    sarcasm_patterns = [r"呵呵", r"真棒", r"厉害了", r"您说得对", r"我懂了"]
    for p in sarcasm_patterns:
        if re.search(p, text):
            findings.append({"type": "sarcasm", "matched": p, "severity": "high"})
    pa_patterns = [r"随便你", r"你开心就好", r"我没意见", r"都行"]
    for p in pa_patterns:
        if re.search(p, text):
            findings.append({"type": "passive_aggressive", "matched": p, "severity": "medium"})
    return findings

def parse_wechat_ocr(text: str) -> List[Dict]:
    """Parse WeChat screenshot OCR text into turns."""
    turns = []
    lines = text.strip().split("\n")
    current_turn = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        time_name_match = re.match(r"(\d{1,2}[:\:]\d{2})\s+(\S+)(?:\s+(.*))?", line)
        if time_name_match:
            if current_turn:
                turns.append(current_turn)
            time, name, msg = time_name_match.groups()
            current_turn = {
                "timestamp": time,
                "speaker": name,
                "raw_text": msg or "",
                "medium": "text"
            }
        elif current_turn is not None:
            current_turn["raw_text"] += " " + line
        else:
            current_turn = {
                "timestamp": "unknown",
                "speaker": "unknown",
                "raw_text": line,
                "medium": "text"
            }
    if current_turn:
        turns.append(current_turn)
    for i, turn in enumerate(turns):
        turn["turn_id"] = i + 1
        turn["cleaned_text"] = clean_text(turn["raw_text"])
        turn["softening"] = detect_softening(turn["cleaned_text"])
        turn["emotional"] = detect_emotional_leakage(turn["cleaned_text"])
        turn["notes"] = []
        if turn["softening"]:
            count = len(turn["softening"])
            turn["notes"].append(f"检测到 {count} 处弱化表达")
        if turn["emotional"]:
            types = [e["type"] for e in turn["emotional"]]
            turn["notes"].append(f"情绪标记: {', '.join(types)}")
    return turns

def build_structured_output(turns, relationship="unknown", goal="", power_dynamic="unclear"):
    return {
        "metadata": {
            "source_type": "wechat_ocr",
            "participants": list(set(t["speaker"] for t in turns)),
            "relationship": relationship,
            "goal": goal,
            "power_dynamic": power_dynamic,
            "processed_at": datetime.now().isoformat(),
            "total_turns": len(turns)
        },
        "turns": turns,
        "summary": {
            "total_softening_instances": sum(len(t["softening"]) for t in turns),
            "total_emotional_markers": sum(len(t["emotional"]) for t in turns),
            "softening_by_speaker": {},
            "key_concerns": []
        }
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python input_sanitizer.py <input_file> [relationship] [goal] [power_dynamic]")
        sys.exit(1)
    input_file = sys.argv[1]
    relationship = sys.argv[2] if len(sys.argv) > 2 else "unknown"
    goal = sys.argv[3] if len(sys.argv) > 3 else ""
    power_dynamic = sys.argv[4] if len(sys.argv) > 4 else "unclear"
    with open(input_file, "r", encoding="utf-8") as f:
        raw_text = f.read()
    turns = parse_wechat_ocr(raw_text)
    output = build_structured_output(turns, relationship, goal, power_dynamic)
    softening_by_speaker = {}
    for t in turns:
        spk = t["speaker"]
        if spk not in softening_by_speaker:
            softening_by_speaker[spk] = 0
        softening_by_speaker[spk] += len(t["softening"])
    output["summary"]["softening_by_speaker"] = softening_by_speaker
    concerns = []
    if output["summary"]["total_softening_instances"] > 3:
        concerns.append(f"检测到 {output['summary']['total_softening_instances']} 处弱化表达，权力姿态可能偏低")
    if output["summary"]["total_emotional_markers"] > 0:
        concerns.append(f"检测到 {output['summary']['total_emotional_markers']} 处情绪标记，存在情绪泄漏风险")
    output["summary"]["key_concerns"] = concerns
    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
