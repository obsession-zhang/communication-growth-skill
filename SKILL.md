# Communication Growth Skill

A skill for analyzing chat logs and call transcripts to identify communication weaknesses, provide actionable feedback, and build a growth plan — with zero tolerance for people-pleasing, full embrace of healthy conflict, and relentless objective rationality.

## Metadata

| Field | Value |
|-------|-------|
| **Name** | communication-growth-skill |
| **Version** | 1.0.0 |
| **Author** | @obsession-zhang |
| **License** | MIT |
| **Language** | zh-CN (primary) |
| **Tags** | communication, self-improvement, conflict, emotional-intelligence, chat-analysis |

## Purpose

Most people never review their own communication. They repeat the same patterns: being too nice, avoiding conflict, rambling when they should be direct, or getting emotional when they should stay calm. This skill turns raw conversation data (chat logs, call transcripts) into a brutally honest, methodologically sound growth report.

**Core Philosophy:**
- **No people-pleasing.** Being liked is not the goal. Being effective is.
- **Conflict is data.** Avoiding conflict is a communication failure, not a virtue.
- **Objective over emotional.** Judge words by their strategic value, not their emotional comfort.
- **Methodology over vibes.** Every critique must come with a concrete alternative, not just a feeling.

## Input

- **Chat logs:** Screenshots, text exports, or pasted conversations (WeChat, Slack, WhatsApp, email threads, etc.)
- **Call transcripts:** Speech-to-text outputs, manual transcripts, or AI-generated summaries of voice/video calls
- **Context (optional):** Relationship type (colleague, boss, partner, family, stranger), goal of the conversation, power dynamic, cultural background

## Output

A structured communication audit report containing:

1. **Conversation Deconstruction** — Turn-by-turn analysis of what was actually said vs. what should have been said
2. **Weakness Taxonomy** — Categorized flaws (emotional leakage, structural chaos, excessive softness, unnecessary conflict, missed leverage, etc.)
3. **Methodological Corrections** — For each flaw: the exact original text, the problem diagnosis, and the rewritten optimal response with reasoning
4. **Pattern Recognition** — Recurring themes across multiple conversations
5. **Growth Plan** — Prioritized action items with practice drills

## Usage

### Quick Start

```bash
# 1. Install the skill
bash install.sh

# 2. Paste your conversation into the input template
# 3. Run the analysis pipeline
python tools/run_pipeline.py --input your_conversation.txt --output report.md
```

### Manual Flow (6 Prompts)

1. **P1-Input-Sanitizer** — Clean and structure raw conversation data
2. **P2-Conversation-Deconstructor** — Break down each exchange strategically
3. **P3-Weakness-Classifier** — Identify and categorize every flaw
4. **P4-Methodological-Rewriter** — Rewrite weak moments with optimal alternatives
5. **P5-Pattern-Miner** — Extract recurring communication DNA across sessions
6. **P6-Growth-Planner** — Generate a prioritized, drill-based improvement plan

## File Structure

```
communication-growth-skill/
├── SKILL.md                          # This file
├── README.md                         # Project overview & quickstart
├── CHANGELOG.md                      # Version history
├── LICENSE                           # MIT License
├── CONTRIBUTING.md                   # Contribution guidelines
├── install.sh                        # One-command installer
├── prompts/
│   ├── P1-Input-Sanitizer.md
│   ├── P2-Conversation-Deconstructor.md
│   ├── P3-Weakness-Classifier.md
│   ├── P4-Methodological-Rewriter.md
│   ├── P5-Pattern-Miner.md
│   └── P6-Growth-Planner.md
├── tools/
│   ├── input_sanitizer.py            # Preprocess raw chat/call data
│   ├── weakness_scorer.py            # Score and rank communication flaws
│   └── report_generator.py           # Generate final markdown report
└── examples/
    ├── example-work-chat.txt         # Sample workplace chat input
    ├── example-work-report.md        # Generated report for work chat
    ├── example-couple-chat.txt       # Sample relationship chat input
    └── example-couple-report.md      # Generated report for couple chat
```

## Principles

### 1. Radical Honesty
If someone was being a doormat, say it. If someone was being manipulative, say it. If the user themselves was the problem, say it louder. The only sin here is sugar-coating.

### 2. Conflict as Competence
Healthy disagreement is a skill. The report must distinguish between:
- **Unproductive conflict:** Emotional, personal, ego-driven
- **Productive conflict:** Strategic, boundary-setting, clarity-driven
And it must teach the user how to move from the former to the latter.

### 3. Structural Rigor
Communication is architecture. A messy response is a structural failure, not a personality trait. The skill must diagnose:
- Missing premises
- Logical leaps
- Buried conclusions
- Unnecessary qualifiers
- Deflection patterns

### 4. Emotional Accountability
Emotions are data, not excuses. The skill flags:
- **Emotional leakage:** When feelings hijack the message
- **Emotional suppression:** When fear hides the truth
- **Emotional manipulation:** When feelings are used as weapons

### 5. Power-Awareness
Every conversation has a power dynamic. The skill must analyze whether the user is:
- Over-deferring to authority
- Under-leading as a manager
- Over-compensating with peers
- Missing leverage with subordinates

## Weakness Categories

The skill recognizes the following flaw categories:

| Category | Description | Example |
|----------|-------------|---------|
| **Softness Overload** | Excessive apologizing, hedging, permission-seeking | "Sorry, but maybe could we possibly..." |
| **Emotional Hijack** | Letting anger, anxiety, or frustration drive the message | All-caps, sarcasm, passive-aggression |
| **Structural Chaos** | Rambling, missing thesis, burying the lead | 500 words to say what 50 could |
| **Conflict Avoidance** | Circling the issue, using euphemisms, ghosting | "Let's circle back" (forever) |
| **Over-Explaining** | Defensive justification, treating the other person as a jury | "The reason I did that was because..." |
| **Under-Asserting** | Failing to state needs, boundaries, or consequences | "It's fine" (when it's not) |
| **Tone Deafness** | Misreading the emotional temperature of the conversation | Making jokes during a serious moment |
| **Strategic Blindness** | Missing the real goal, fighting the wrong battle | Winning an argument, losing the war |
| **Reciprocity Failure** | Ignoring social contracts, taking without giving | Asking for favors without context |
| **Boundary Collapse** | Accepting unreasonable demands, failing to push back | "Sure, I can do that too" (the 5th time) |

## Contribution

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Acknowledgments

Inspired by the relentless self-improvement ethos of the daily-review-skill project and the no-nonsense communication philosophy of thinkers who treat conversation as a craft, not a personality trait.
