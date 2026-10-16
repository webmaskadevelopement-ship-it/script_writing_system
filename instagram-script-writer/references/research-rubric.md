# Research rubric

## Evidence record

Store one object per public item with these fields where available:

```json
{
  "url": "https://...",
  "platform": "instagram",
  "creator": "@handle",
  "published_at": "2026-01-01",
  "format": "reel",
  "language": "en",
  "views": 120000,
  "likes": 4300,
  "comments": 210,
  "shares": null,
  "saves": null,
  "hook": "short paraphrase, not a transcript",
  "outline": "one-sentence summary",
  "relevance": 0.9
}
```

## Ranking

1. Filter to the same or comparable format, language, niche, and recent window before comparing.
2. If views exist, calculate visible engagement rate as `(likes + comments + shares + saves) / views`. Do not treat this as the platform's true engagement rate.
3. If views do not exist, use creator-size-normalized engagement only if follower count is visible and recent; otherwise rank qualitatively.
4. Blend signals rather than selecting only the largest account:
   - 40% normalized engagement or view rate
   - 25% relevance to the brief
   - 15% recency
   - 10% comment evidence (specific questions, “how do I…”, saves/shares language)
   - 10% cross-platform recurrence
5. Keep raw fields and component scores. Never fabricate missing values; use `null`.

## Confidence labels

- **High**: 5+ comparable examples from 3+ creators, with visible metrics and a repeated pattern.
- **Medium**: 3–4 comparable examples or incomplete metrics, but a coherent repeated pattern.
- **Low**: 1–2 examples, mixed formats, old posts, or mostly qualitative signals.

A pattern is a hypothesis, not a guarantee. Prefer wording such as “appears associated with” or “worth testing.”

## Pattern extraction checklist

For each candidate pattern, note:

- Hook: question, contradiction, result-first, confession, warning, list, or story-in-progress.
- Tension: pain, desire, identity, status, fear, curiosity, or time pressure.
- Payoff: transformation, explanation, demonstration, reveal, checklist, or emotional resolution.
- Delivery: POV, sentence length, pauses, cuts, b-roll, captions, sound, and visual contrast.
- Trust: demonstration, source, credentials, social proof, caveat, or comment response.
- Conversion: follow, save, share, comment keyword, DM, click, or purchase.
- Failure signals: slow setup, vague promise, unsupported claim, generic CTA, or overloaded ideas.
