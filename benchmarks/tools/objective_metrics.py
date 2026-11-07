"""Objective before/after metrics for variants of one tool, without a judge.

For every output: are the reference facts present (checks.json "facts": all groups must match,
any alternative in a group counts), is a primary source cited (checks.json "primary" domains),
how many sources, does it end with an offer of more help, does it leak Google UI text, length, time.

Usage: python objective_metrics.py <run_dir> <variant> [<variant> ...] [--extra name=raw.json:tool]
"""
import json
import re
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from normalize import NORMALIZERS  # noqa: E402

OFFER = re.compile(
    r"(would you like|let me know|i can (also )?(help|share|show|walk|explain|compare|provide|write|break)|"
    r"хотите|могу (подробнее|рассказать|подсказать|помочь|показать|объяснить)|подсказать\?|нужно ли|уточните)",
    re.I,
)
UI_LEAKS = ["Используйте код с осторожностью", "Use code with caution", "носит справочный характер",
            "may include mistakes", "могут быть ошибки"]


def metrics(body, sources, check):
    text = body + "\n" + "\n".join(sources)
    facts = all(any(alt.lower() in body.lower() for alt in group) for group in check["facts"])
    links = set(sources) | set(re.findall(r"\]\((https?://[^)\s]+)\)", body))
    primary = None if not check["primary"] else any(d in u for u in links for d in check["primary"])
    last = [p for p in body.strip().split("\n\n") if p.strip()][-1:] or [""]
    return {
        "facts": facts,
        "primary": primary,
        "sources": len(sources),
        "offer": bool(OFFER.search(last[0])),
        "ui_leak": any(s in text for s in UI_LEAKS),
        "chars": len(body),
    }


def main(run_dir, *args):
    run = Path(run_dir)
    raw = json.load(open(run / "raw.json", encoding="utf-8"))
    checks = json.load(open(run / "checks.json", encoding="utf-8"))
    columns = {}
    for arg in args:
        if arg.startswith("--extra="):
            name, spec = arg[len("--extra="):].split("=", 1)
            path, tool = spec.rsplit(":", 1)
            extra = json.load(open(path, encoding="utf-8"))
            columns[name] = {q: extra[q][tool] for q in checks}
        else:
            columns[arg] = {q: raw[q][arg] for q in checks}

    per_question, summary = {}, {}
    for name, runs in columns.items():
        rows = {}
        for qid, check in checks.items():
            tool = name if ":" in name or name in NORMALIZERS else "google_ai_mode"
            body, sources = NORMALIZERS[tool.split(":")[0]](runs[qid]["output"])
            rows[qid] = {**metrics(body, sources, check), "seconds": runs[qid]["seconds"]}
            per_question.setdefault(qid, {})[name] = rows[qid]
        with_primary = [r for r in rows.values() if r["primary"] is not None]
        summary[name] = {
            "facts_present": sum(r["facts"] for r in rows.values()),
            "primary_cited": f'{sum(r["primary"] for r in with_primary)}/{len(with_primary)}',
            "no_sources": sum(r["sources"] == 0 for r in rows.values()),
            "median_sources": statistics.median(r["sources"] for r in rows.values()),
            "ends_with_offer": sum(r["offer"] for r in rows.values()),
            "ui_leaks": sum(r["ui_leak"] for r in rows.values()),
            "median_chars": statistics.median(r["chars"] for r in rows.values()),
            "total_chars": sum(r["chars"] for r in rows.values()),
            "median_seconds": statistics.median(r["seconds"] for r in rows.values()),
        }
    json.dump({"summary": summary, "per_question": per_question},
              open(run / "objective_metrics.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    keys = list(next(iter(summary.values())))
    print("| metric | " + " | ".join(summary) + " |")
    print("|---" * (len(summary) + 1) + "|")
    for key in keys:
        print(f"| {key} | " + " | ".join(str(s[key]) for s in summary.values()) + " |")
    print()
    for qid, cols in per_question.items():
        print(qid, " | ".join(f"{n}: facts={c['facts']} prim={c['primary']} src={c['sources']} offer={c['offer']} leak={c['ui_leak']} {c['chars']}ch"
                              for n, c in cols.items()))


if __name__ == "__main__":
    main(*sys.argv[1:])
