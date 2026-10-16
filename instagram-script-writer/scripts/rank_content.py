#!/usr/bin/env python3
"""Rank public content evidence without inventing missing metrics.

Usage:
  python rank_content.py evidence.json > ranked.json
  python rank_content.py evidence.jsonl --jsonl > ranked.jsonl

The score is a transparent heuristic, not a prediction of reach.
"""
import argparse, json, math, sys
from datetime import date


def load(path, jsonl=False):
    with open(path, encoding="utf-8") as f:
        if jsonl:
            return [json.loads(line) for line in f if line.strip()]
        data = json.load(f)
        return data if isinstance(data, list) else data.get("items", [])


def num(x):
    return float(x) if isinstance(x, (int, float)) and x >= 0 else None


def percentile(values, value):
    if value is None or not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return 1.0
    return sum(v <= value for v in ordered) / len(ordered)


def recency(item):
    raw = item.get("published_at") or item.get("date")
    try:
        days = max(0, (date.today() - date.fromisoformat(str(raw)[:10])).days)
        return max(0.0, 1.0 - min(days, 730) / 730)
    except Exception:
        return 0.5


def rank(items):
    engagement = []
    for x in items:
        views = num(x.get("views"))
        counts = [num(x.get(k)) or 0 for k in ("likes", "comments", "shares", "saves")]
        engagement.append(sum(counts) / views if views and views > 0 else None)
    visible = [v for v in engagement if v is not None]
    relevance = [min(1.0, max(0.0, num(x.get("relevance")) or 0.5)) for x in items]
    for i, x in enumerate(items):
        eng = percentile(visible, engagement[i]) if engagement[i] is not None else 0.0
        rel = relevance[i]
        rec = recency(x)
        comments = num(x.get("comments"))
        comment_signal = percentile([num(y.get("comments")) for y in items if num(y.get("comments")) is not None], comments) if comments is not None else 0.0
        x["visible_engagement_rate"] = round(engagement[i], 6) if engagement[i] is not None else None
        x["research_score"] = round(100 * (0.40 * eng + 0.25 * rel + 0.15 * rec + 0.10 * comment_signal), 2)
        x["rank_confidence"] = "medium" if engagement[i] is not None else "low"
    return sorted(items, key=lambda x: x["research_score"], reverse=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--jsonl", action="store_true")
    args = ap.parse_args()
    result = rank(load(args.input, args.jsonl))
    if args.jsonl:
        for item in result:
            print(json.dumps(item, ensure_ascii=False))
    else:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        print()


if __name__ == "__main__":
    main()
