"""Add variants of one tool (the same tool asked with different query texts) to a run.

Each variant maps every question id to the exact query text that was sent. Only calls made
after the latest call with the first query of the first variant are used, so earlier
experiments with the same texts do not leak in. Tools already in the base run are copied.

Usage: python extract_variants.py <session.jsonl> <tool_name> <base_raw.json> <out_raw.json> <variant>=<queries.json> [...]

<queries.json> is {"q01": "query text", ...}; the literal value "@question" uses questions.json
next to base_raw.json.
"""
import json
import sys
from datetime import datetime
from pathlib import Path


def ts(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def result_text(block):
    content = block.get("content")
    if isinstance(content, str):
        return content
    return "\n".join(part.get("text", "") for part in content or [] if part.get("type") == "text")


def main(transcript, tool_name, base_path, out_path, *variant_args):
    base = json.load(open(base_path, encoding="utf-8"))
    questions = json.load(open(Path(base_path).with_name("questions.json"), encoding="utf-8"))
    variants = {}
    for arg in variant_args:
        name, source = arg.split("=", 1)
        if source == "@question":
            variants[name] = {q["id"]: q["question"] for q in questions}
        else:
            variants[name] = json.load(open(source, encoding="utf-8"))

    calls, order = {}, []
    with open(transcript, encoding="utf-8") as fh:
        for line in fh:
            entry = json.loads(line)
            message = entry.get("message") or {}
            content = message.get("content")
            if not isinstance(content, list) or "timestamp" not in entry:
                continue
            for block in content:
                if block.get("type") == "tool_use" and block.get("name") == tool_name:
                    if set(block["input"]) - {"query"}:
                        continue
                    calls[block["id"]] = {"query": block["input"]["query"], "started": entry["timestamp"]}
                    order.append(block["id"])
                elif block.get("type") == "tool_result" and block.get("tool_use_id") in calls:
                    call = calls[block["tool_use_id"]]
                    call["finished"] = entry["timestamp"]
                    call["output"] = result_text(block)
                    call["is_error"] = bool(block.get("is_error"))

    first_variant = next(iter(variants.values()))
    first_query = first_variant[questions[0]["id"]]
    starts = [calls[c]["started"] for c in order if calls[c]["query"] == first_query]
    if not starts:
        raise SystemExit(f"[ERROR] no call with the first query: {first_query!r}")
    since = max(starts)

    out = {qid: dict(tools) for qid, tools in base.items()}
    for name, queries in variants.items():
        by_text = {text: qid for qid, text in queries.items()}
        for call_id in order:
            call = calls[call_id]
            if call["started"] < since or "finished" not in call or call["is_error"]:
                continue
            qid = by_text.get(call["query"])
            if qid is None:
                continue
            out[qid][f"{tool_name_short(tool_name)}:{name}"] = {
                "output": call["output"],
                "query": call["query"],
                "content_call": call_id,
                "seconds": round((ts(call["finished"]) - ts(call["started"])).total_seconds(), 2),
                "timing_from_content_call": True,
            }
        missing = [q["id"] for q in questions if f"{tool_name_short(tool_name)}:{name}" not in out[q["id"]]]
        if missing:
            raise SystemExit(f"[ERROR] variant {name}: no run for {missing}")
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for qid, tools in out.items():
        print(qid, " ".join(f"{t}={v['seconds']}s" for t, v in tools.items()))


def tool_name_short(tool_name):
    return {"mcp__google-ai-mode__search": "google_ai_mode"}.get(tool_name, tool_name)


if __name__ == "__main__":
    main(*sys.argv[1:])
