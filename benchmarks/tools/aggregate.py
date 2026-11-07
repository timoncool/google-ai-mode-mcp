"""Map blind verdicts back to tools and summarize scores, wins and speed.

Usage: python aggregate.py <bench_dir>
"""
import json
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

LABELS = {"google_ai_mode": "Google AI Mode MCP", "websearch": "Claude Code WebSearch", "exa": "Exa web_search_exa"}


def label(tool):
    base, _, variant = tool.partition(":")
    return LABELS.get(base, base) + (f" ({variant})" if variant else "")
CRITERIA = ["correct", "complete", "sources", "focus"]


def main(bench_dir):
    bench = Path(bench_dir)
    mapping = json.load(open(bench / "mapping.json", encoding="utf-8"))
    raw = json.load(open(bench / "raw.json", encoding="utf-8"))
    normalized = json.load(open(bench / "normalized.json", encoding="utf-8"))
    questions = {q["id"]: q for q in json.load(open(bench / "questions.json", encoding="utf-8"))}

    rows = []
    for path in sorted((bench / "verdicts").glob("verdict*.json")):
        for verdict in json.load(open(path, encoding="utf-8"))["questions"]:
            qid = verdict["qid"]
            ids = mapping[qid]
            if set(verdict["scores"]) != set(ids):
                raise SystemExit(f"[ERROR] {path.name} {qid}: ids {sorted(verdict['scores'])} != {sorted(ids)}")
            rows.append({
                "qid": qid,
                "topic": questions[qid]["topic"],
                "best": ids[verdict["best"]],
                "ranking": [ids[i] for i in verdict["ranking"]],
                "scores": {ids[i]: s for i, s in verdict["scores"].items()},
                "rationale": verdict["rationale"],
            })
    if len(rows) != len(questions):
        raise SystemExit(f"[ERROR] {len(rows)} verdicts for {len(questions)} questions")
    rows.sort(key=lambda r: r["qid"])

    tools = sorted({t for ids in mapping.values() for t in ids.values()})
    summary = {}
    for tool in tools:
        scores = [r["scores"][tool] for r in rows]
        summary[tool] = {
            "wins": sum(r["best"] == tool for r in rows),
            "mean_rank": round(statistics.mean(r["ranking"].index(tool) + 1 for r in rows), 2),
            **{c: round(statistics.mean(s[c] for s in scores), 2) for c in CRITERIA},
            "total_of_8": round(statistics.mean(sum(s[c] for c in CRITERIA) for s in scores), 2),
            "self_sufficient": sum(bool(s["self_sufficient"]) for s in scores),
            "fully_correct": sum(s["correct"] == 2 for s in scores),
            "median_s": statistics.median(raw[q][tool]["seconds"] for q in raw),
            "mean_s": round(statistics.mean(raw[q][tool]["seconds"] for q in raw), 2),
            "median_chars": statistics.median(len(normalized[q][tool]["body"]) for q in normalized),
            "total_chars": sum(len(normalized[q][tool]["body"]) for q in normalized),
        }
    by_topic = defaultdict(Counter)
    for r in rows:
        by_topic[r["topic"]][r["best"]] += 1

    result = {"summary": summary, "wins_by_topic": {t: dict(c) for t, c in by_topic.items()}, "per_question": rows}
    json.dump(result, open(bench / "results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    for tool, s in summary.items():
        print(f"{label(tool):36} wins={s['wins']:2} rank={s['mean_rank']} score8={s['total_of_8']} "
              f"correct={s['correct']} complete={s['complete']} sources={s['sources']} focus={s['focus']} "
              f"self_suff={s['self_sufficient']}/25 fully_correct={s['fully_correct']}/25 "
              f"median={s['median_s']}s chars_med={s['median_chars']}")
    for topic, counter in result["wins_by_topic"].items():
        print(topic, dict(counter))
    for r in rows:
        print(r["qid"], "best:", r["best"], "| rank:", ">".join(r["ranking"]),
              "|", " ".join(f"{t}={sum(r['scores'][t][c] for c in CRITERIA)}" for t in tools))


if __name__ == "__main__":
    main(sys.argv[1])
