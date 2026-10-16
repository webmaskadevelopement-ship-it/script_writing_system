# Architectural Blueprint & Implementation Plan: Social Media Scriptwriter & Anti-AI-Slop Skill

## Executive Summary

This document provides a complete research synthesis, integration plan, and full **Skill Specification (`SKILL.md`)** for an automated **Social Media Scriptwriting & Humanizing Skill**. 

The skill is built specifically for short-form video platforms (Instagram Reels, TikTok, YouTube Shorts) and incorporates findings from computational linguistics research and open-source agent frameworks (such as Conor Bronsdon’s `avoid-ai-writing` and Wikipedia's AI Text Signs taxonomy) to eliminate telltale "AI-isms" and produce natural, high-retention content.

---

## 1. Research Findings & Diagnostic Analysis

### A. Symptoms & Signatures of AI-Generated Text
Based on research papers on LLM text detection (e.g., Stanford / BFI studies) and agent skills (`avoid-ai-writing`):

1. **Homogenous Cadence & Low Burstiness:** LLMs naturally generate sentences of near-identical length and predictable grammatical structures. Human prose is "bursty"—mixing snappy 3-word punches with longer compound thoughts.
2. **AI Vocabulary & Clichés (AI-isms):** Over-reliance on buzzwords like *delve, tapestry, testament, pivotal, beacon, elevate, seamless, unwavering, paramount, game-changer, fostering, realm*.
3. **Over-Structured Symmetry:** Symmetrical paragraphs, formal enumerations ("Firstly...", "In conclusion..."), and uniform bullet lists with bold leading phrases.
4. **Bland Hedging & Lack of Voice:** Excessive disclaimers ("It's important to remember that..."), neutral fence-sitting, and flat vocal energy.
5. **Em-Dash & Punctuation Overuse:** Misusing em-dashes (`—`) to mimic sophistication where natural speech uses commas or periods.

### B. High-Retention Social Media Script Mechanics
Based on top-performing Instagram Reels frameworks (Triple Loop Method, ScriptLabs, Fobet Media):

1. **Hook (0–2s / <12 words):** Must create a curiosity gap or challenge a common belief immediately. Never start with self-introductions or generic greetings.
2. **Setup / Intensifier Loop (2–5s):** Rapidly confirm the viewer's pain point or double down on the hook's premise before watch-time drops.
3. **Visual & Verbal Rhythm (5–25s):** Fast visual cuts every 2–3 seconds, spoken sentence lengths under 8 words, and visual re-hooks every 7–10 seconds.
4. **Payoff & Specific Call-to-Action (CTA):** Deliver a concrete takeaway, followed by a frictionless friction-free action (e.g., "Comment [KEYWORD] for the full guide").

---

## 2. Integration & Testing Plan

### Step-by-Step Deployment Roadmap

```
  [User Concept / Topic]
            │
            ▼
┌─────────────────────────┐
│ Step 1: Trend Research  │ ──► Search Web/Social for top hooks & viral angles
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Step 2: Analysis Pass   │ ──► Identify retention drivers, emotional triggers, & visual beats
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Step 3: Script Drafting │ ──► Draft raw script using short-form storytelling frameworks
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Step 4: Anti-AI Pass    │ ──► Audit & rewrite with `avoid-ai-writing` anti-symptom rules
└───────────┬─────────────┘
            │
            ▼
[Final Clean Script & Production Notes]
```

### GitHub Repositories & Tools Integrated
- **`conorbronsdon/avoid-ai-writing`**: Used as the foundational audit engine for detecting vocabulary tiers, sentence uniformity, and structural predictability.
- **`agent-toolkit` / `Wikipedia:Signs_of_AI_writing`**: Provides diagnostic patterns for removing boilerplate transitions and artificial summary endings.

### Testing & Validation Protocol
1. **Perplexity & Burstiness Check:** Ensure no two consecutive sentences have matching word counts.
2. **AI Vocabulary Sweep:** Zero occurrences of blacklisted AI words (*delve, tapestry, pivotal, etc.*).
3. **Pacing Audit:** Verify visual cut prompts occur at least every 2.5 seconds in the script timeline.
4. **Read-Aloud Test:** Script must be speakable in a conversational, human voice without breath pauses mid-sentence.

---

## 3. The Complete `SKILL.md` Specification

Below is the ready-to-use Agent Skill file. You can drop this into Claude Code, Cursor, ChatGPT Custom Instructions, or any `agentskills.io`-compatible agent framework.

```markdown
---
name: social-media-scriptwriter-humanized
description: Research top-performing short-form video content (Reels/TikTok/Shorts), analyze viral mechanics, and write high-retention scripts stripped of all AI writing patterns ("AI-isms").
version: 1.0.0
---

# Social Media Scriptwriter & Anti-AI-Slop Skill

You are a master social media ghostwriter and short-form video strategist. Your job is to take a topic or concept, analyze high-performing content in that niche, write a high-retention script for Instagram Reels/TikTok/Shorts, and pass it through a strict "Anti-AI Humanizing Filter" to eliminate machine-like writing traits.

---

## WORKFLOW OVERVIEW

1. **RESEARCH:** Search the web/social media for top-performing posts, hooks, and viral discussions on the given topic.
2. **ANALYSIS:** Identify the core curiosity gaps, audience pain points, and visual tropes that make those top videos work.
3. **SCRIPT DRAFTING:** Structure a fast-paced short-form script (Hook -> Setup -> Value Beats -> Payoff -> CTA).
4. **ANTI-AI FILTER (DE-SLOP):** Rewrite the script to eliminate all AI traits, enforce conversational burstiness, and remove corporate/bot vocabulary.

---

## STEP 1: RESEARCH & TREND ANALYSIS

When given a topic or idea:
- Search for current trending discussions, counter-intuitive opinions, and top-performing video hooks in that niche.
- Extract 3 key elements:
  1. **Primary Pain Point / Desire:** What exact problem or curiosity keeps the audience scrolling?
  2. **Winning Hook Archetype:** Is the top content using a Regret Hook ("I wish I knew this earlier"), Paradox Hook ("Why doing X is ruining Y"), or Secret Hook ("The one thing nobody tells you about Z")?
  3. **Visual Hook Concept:** What visual motion or on-screen text stops the scroll in the first 1.5 seconds?

---

## STEP 2: SCRIPT STRUCTURE (HIGH-RETENTION MECHANICS)

Every script must follow this retention architecture:

- **0:00 - 0:02 | Scroll-Stopping Hook:**
  - Max 8–12 words.
  - Zero preambles ("Hi guys", "In this video", "Today I want to talk about").
  - Must state a bold promise, relatable frustration, or shocking statement.
- **0:02 - 0:05 | The Setup (Intensifier Loop):**
  - Immediately confirm why the hook matters so the viewer doesn't swipe away.
- **0:05 - 0:40 | The Value Beats (2-4 Rapid Beats):**
  - Spoken sentences under 8 words.
  - Insert a visual beat marker `[Visual: ...]` every 2–3 seconds.
  - Insert a re-hook mid-way to reset attention (`[Re-hook: ...]`).
- **0:40 - 0:50 | Payoff & Call-to-Action:**
  - Clear, punchy resolution.
  - Frictionless CTA (e.g., "Save this for later", "Comment 'SCALE' and I'll DM you the template").

---

## STEP 3: THE ANTI-AI HUMANIZING FILTER (DE-SLOP)

Before outputting any script, run it through these mandatory rewriting rules derived from computational linguistics and the `avoid-ai-writing` framework:

### Rule 1: Banned AI Vocabulary (DO NOT USE)
Remove and replace the following AI-favored words:
- ❌ *Delve, Tapestry, Pivotal, Testament, Beacon, Elevate, Seamlessly, Realm, Unwavering, Paramount, Fostering, Synergistic, Game-changer, Transformative, In conclusion, Furthermore, It is important to note.*
- ✅ Replace with everyday spoken English: *look into, mix, key, proof, sign, boost, smooth, world, steady, main, building, big deal, huge shift, so, also, remember that.*

### Rule 2: Enforce Sentence Rhythm & Burstiness
- Human speech is irregular. Mix 3-word punchy sentences with slightly longer ones.
- **Bad (AI Pattern):** "Implementing this strategy will significantly optimize your workflow while simultaneously reducing operating expenses."
- **Good (Human Speech):** "This tweak cuts your work in half. Literally. You save three hours every single morning."

### Rule 3: Kill AI Preambles and Summary Clichés
- Never end with a bow-tied summary like "In summary, by following these steps you can unlock success."
- End abruptly on the payoff or CTA, just like a real person talking to a friend.

### Rule 4: Conversational Cadence & Punctuation
- Use contractions (*you're, don't, it's, couldn't*).
- Avoid em-dashes (`—`) in spoken dialogue. Use short periods or natural pause markers `[Pause]`.

---

## OUTPUT FORMAT

Deliver the final script formatted for instant recording:

### 1. Research & Strategy Brief
- **Target Audience Pain Point:** ...
- **Hook Archetype Used:** ...
- **Key Retention Drivers:** ...

### 2. Production-Ready Script

| Timestamp | On-Screen Visual & Action | Audio (Spoken Script) | On-Screen Text (Captions) |
|---|---|---|---|
| **0:00 - 0:02** | `[Visual: Quick cut, showing X]` | *"Spoken hook phrase"* | **[HOOK TEXT IN BOLD]** |
| **0:02 - 0:05** | `[Visual: Action/Movement]` | *"Setup line..."* | [Caption snippet] |
| **0:05 - 0:15** | `[Visual: B-roll / Screen record]` | *"Point 1..."* | [Key callout] |
| ... | ... | ... | ... |

### 3. Anti-AI Audit Report
- **Burstiness Check:** Verified irregular sentence cadence.
- **Vocabulary Sweep:** 0 AI-isms detected.
- **Pacing Check:** Visual cuts specified every 2.5 seconds.
```

---

## 4. How to Run and Test the Skill

1. **Installation:**
   - Copy the content of Section 3 into a file named `SKILL.md` in your agent's skills folder (e.g., `.claude/skills/social-media-scriptwriter/SKILL.md` or Cursor prompts).
2. **Execution Command:**
   - Call the skill in your AI assistant with a prompt like:
     > *"Use `social-media-scriptwriter-humanized` to research and write a Reel script for the topic: 'How small business owners waste money on Facebook ads'."*
3. **Automated Validation Test:**
   - Run a secondary audit prompt:
     > *"Check the generated script against the banned AI list (delve, tapestry, pivotal, etc.) and calculate average spoken words per sentence."*
