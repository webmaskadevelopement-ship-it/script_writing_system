---
name: instagram-script-writer
description: Research-driven Instagram script writing from public, current content signals. Use when the user wants Instagram Reels, carousels, captions, hooks, story scripts, trend analysis, competitor/content research, or scripts inspired by high-performing content without copying it.
---

# Instagram Script Writer

Use this skill to turn a topic and an original idea into a research-backed Instagram script. Treat “top-performing” as **publicly observable performance signals**, not verified reach: normalize comparisons within the same platform, format, language, niche, and recency window.

## Operating rules

- Research public content only. Use approved search, browser, or platform connectors; never bypass logins, CAPTCHAs, paywalls, rate limits, robots controls, or private accounts.
- Do not download or reproduce full copyrighted scripts, captions, audio, or creator-specific catchphrases. Extract abstract patterns and write a materially original script.
- Separate **observed fact**, **inference**, and **creative recommendation**. Cite URLs, handles, dates, and visible metrics when available.
- Do not claim a post is “viral” from likes alone. Report the signal and its limitations.
- Ask for missing choices only when they materially change the result; otherwise use sensible defaults: 30–60 seconds, 9:16 Reel, the user’s language, one clear audience, and a strong but honest CTA.

## Workflow

1. **Define the brief.** Capture topic, audience, objective, offer/CTA, format, language, tone, duration, brand constraints, taboo claims, and whether the user wants trend research, script generation, or both. If unspecified, state defaults.
2. **Build a search plan.** Create 6–12 query variants: broad topic, audience pain point, outcome, misconception, how-to, emotional angle, and relevant keywords/hashtags. Search Instagram plus at least two useful adjacent sources (TikTok, YouTube Shorts, Facebook, Reddit, Google/web, or a niche publication). Prefer the platform where the requested format lives.
3. **Collect a compact evidence set.** Aim for 10–20 public examples across multiple creators. Record URL, platform, creator, date, format, visible metrics, transcript/outline, opening hook, promise, proof, pacing, CTA, comments/replies, and why it appears relevant. Do not over-collect near-duplicates.
4. **Rank transparently.** Use the rubric in `references/research-rubric.md`. Prefer engagement rate or view-normalized signals where denominators are available; otherwise use a confidence-labeled qualitative rank. Run `scripts/rank_content.py` on a JSON or JSONL evidence file when structured ranking is useful.
5. **Extract the winning pattern.** Cluster examples by hook type, audience tension, promise, narrative arc, visual grammar, proof device, pacing, caption/CTA, and comment language. Identify recurring patterns and meaningful outliers. Never treat correlation as a guaranteed cause.
6. **Create a style fingerprint.** Summarize the reusable mechanics—not a creator’s identity—in 5–10 bullets: hook formula, sentence length, POV, emotional movement, proof density, scene changes, on-screen text, sound/visual conventions, CTA behavior, and what to avoid. Include confidence and evidence count for major findings.
7. **Generate an original script.** Apply the fingerprint to the user’s idea while changing the premise, wording, examples, sequence, and payoff. Prefer specificity, one core promise, spoken-language rhythm, and a first-2-second hook. Use the output template below.
8. **Quality-check.** Verify hook clarity, one audience/one promise, factual claims, originality, platform fit, retention beats, accessibility, brand safety, and CTA alignment. Mark any unverified claim for fact-checking.
9. **Offer variants.** When useful, provide 2–3 materially different hooks or endings, not near-duplicate rewrites. Explain the strategic trade-off briefly.

## Research output

When research is requested, return:

- **Brief and assumptions**
- **Evidence table**: source, date, format, visible metrics, normalized/qualitative rank, and relevance
- **What appears to work**: 3–7 patterns with supporting examples and confidence
- **Style fingerprint**: mechanics to borrow, mechanics to avoid, and originality boundaries
- **Creative opportunities**: gaps, unanswered comments, or underserved angles
- **Limitations**: missing metrics, platform bias, recency, sampling, and access constraints

Do not expose an unfiltered dump of scraped material. Summarize, link, and quote only short excerpts when necessary.

## Script output template

Use this default structure, adapting it to the requested format:

```text
TITLE / ANGLE:
AUDIENCE:
OBJECTIVE + CTA:
FORMAT / LENGTH:

HOOK (0–2s): [spoken line]
ON-SCREEN TEXT: [short, readable text]

SCRIPT:
[Beat 1 — pattern interrupt / tension]
[Beat 2 — context or relatable problem]
[Beat 3 — insight, demonstration, or story turn]
[Beat 4 — proof, example, or objection handling]
[Beat 5 — payoff and clear next step]

SHOT LIST:
1. [visual, framing, movement, text]
2. ...

CAPTION:
[caption with searchable phrasing, spacing, and CTA]

ALT TEXT:
[accessible description]

VARIANTS:
- Hook A: ...
- Hook B: ...

FACT-CHECK / RISK NOTES:
[claims to verify, disclosures, rights or safety notes]
```

For carousel posts, replace beats with slide-by-slide copy and visual direction. For Stories, use frame-by-frame beats with interaction stickers. For captions-only requests, preserve the same research and originality checks but omit production fields.

## Choosing tools

- Use web/search for public discovery and current factual context.
- Use a stateful browser or approved connector for dynamic public pages and visible metrics when search snippets are insufficient.
- Use `workflow` only for genuinely broad, multi-item research; for a normal topic, a bounded set of searches is enough.
- Read `references/platform-playbook.md` when choosing platform-specific research tactics or adapting one idea across Instagram, TikTok, YouTube Shorts, and Facebook.
- Read `references/research-rubric.md` when scoring evidence, handling incomplete metrics, or explaining confidence.

## Failure handling

- If Instagram is inaccessible, say so and triangulate with public search results and adjacent platforms; label the source gap.
- If metrics are hidden or inconsistent, use qualitative ranking and state that it is not a reach estimate.
- If the user requests imitation of a living creator, decline direct style cloning and offer a high-level fingerprint based on publicly observable mechanics.
- If the topic is medical, financial, legal, political, or safety-critical, add a verification step and avoid unsupported persuasion.
