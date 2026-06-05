#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
report_generator.py

Generate a final markdown report from all pipeline outputs.
Combines: structured data, weakness scores, and manual analysis prompts.
"""

import json
import sys
from datetime import datetime

def generate_report(structured_data: dict, weakness_scores: dict, user_notes: str = "") -> str:
    """Generate a full markdown report."""

    metadata = structured_data.get("metadata", {})
    turns = structured_data.get("turns", [])
    summary = structured_data.get("summary", {})

    report = f"""# 沟通成长报告

> **生成时间：** {datetime.now().strftime("%Y-%m-%d %H:%M")}  
> **对话来源：** {metadata.get("source_type", "unknown")}  
> **关系类型：** {metadata.get("relationship", "unknown")}  
> **权力动态：** {metadata.get("power_dynamic", "unclear")}  
> **对话目标：** {metadata.get("goal", "未指定")}  
> **总轮次：** {metadata.get("total_turns", len(turns))}

---

## 01 对话拆解

"""

    for turn in turns:
        report += f"""### Turn {turn["turn_id"]}: {turn["speaker"]}

**原文：** {turn.get("cleaned_text", "")}

"""
        if turn.get("softening"):
            report += f"**⚠️ 弱化检测：** 发现 {len(turn['softening'])} 处弱化表达
"
            for s in turn["softening"]:
                report += f"- `{s['matched']}` （严重程度：{s['severity']}）
"
            report += "
"

        if turn.get("emotional"):
            report += f"**🔥 情绪标记：** 发现 {len(turn['emotional'])} 处情绪信号
"
            for e in turn["emotional"]:
                report += f"- 类型：`{e['type']}` （严重程度：{e['severity']}）
"
            report += "
"

        if turn.get("notes"):
            report += f"**💡 备注：** {'；'.join(turn['notes'])}

"

        report += "---

"

    # Weakness classification
    report += """## 02 缺陷分类

"""

    if weakness_scores.get("findings"):
        for i, finding in enumerate(weakness_scores["findings"], 1):
            report += f"""### 缺陷 #{i}: {finding['category']}

**严重程度：** {finding['severity'].upper()}  
**评分：** {finding['score']:.1f}  
**涉及轮次：** Turn {finding['turn_id']}

**原文：**
> {finding['evidence']}

**问题诊断：**
{finding['details']}

---

"""
    else:
        report += "本次对话未检测到明显缺陷。

"

    # Health status
    health = weakness_scores.get("health_status", "unknown")
    health_emoji = {"critical": "🔴", "major_concerns": "🟠", "moderate": "🟡", "healthy": "🟢"}
    report += f"""## 03 健康评估

**总体状态：** {health_emoji.get(health, "⚪")} {health}

**总评分：** {weakness_scores.get('total_score', 0):.1f}

**分类评分：**
"""

    for cat, score in weakness_scores.get("category_scores", {}).items():
        if score > 0:
            report += f"- {cat}: {score:.1f}
"

    report += f"""
**关键关注：**
"""
    for concern in summary.get("key_concerns", []):
        report += f"- {concern}
"

    if not summary.get("key_concerns"):
        report += "- 无明显问题
"

    report += """
---

## 04 方法论修正（请结合 P4 提示词使用）

> 本部分需要人工分析。请运行 P4-Methodological-Rewriter 提示词，输入上述缺陷清单，获取逐条修正方案。

---

## 05 模式识别（请结合 P5 提示词使用）

> 本部分需要多段对话数据。请积累 3-5 次对话分析后，运行 P5-Pattern-Miner 提示词，获取跨对话模式报告。

---

## 06 成长计划（请结合 P6 提示词使用）

> 本部分需要 P3-P5 的完整输出。请运行 P6-Growth-Planner 提示词，获取可执行的成长计划。

---

"""

    if user_notes:
        report += f"""## 用户备注

{user_notes}

---

"""

    report += """## 附录：使用说明

1. 将本报告与原始对话一起提交给 AI 分析师
2. 按顺序运行 P2 → P3 → P4 → P5 → P6 提示词
3. 每次对话后更新本报告，追踪长期趋势

> **记住：沟通不是天赋，是手艺。手艺可以练。**
"""

    return report

def main():
    if len(sys.argv) < 3:
        print("Usage: python report_generator.py <structured_json> <weakness_json> [user_notes]")
        sys.exit(1)

    structured_file = sys.argv[1]
    weakness_file = sys.argv[2]
    user_notes = sys.argv[3] if len(sys.argv) > 3 else ""

    with open(structured_file, "r", encoding="utf-8") as f:
        structured_data = json.load(f)

    with open(weakness_file, "r", encoding="utf-8") as f:
        weakness_scores = json.load(f)

    report = generate_report(structured_data, weakness_scores, user_notes)
    print(report)

if __name__ == "__main__":
    main()
