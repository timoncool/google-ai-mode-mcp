"""Pull benchmark calls (query, raw output, timing) out of a Claude Code session transcript.

Usage: python extract.py <session.jsonl> <questions.json> <out_raw.json>
"""
import json
import sys
from collections import defaultdict
from datetime import datetime

TOOLS = {
    "mcp__google-ai-mode__search": "google_ai_mode",
    "WebSearch": "websearch",
    "mcp__exa__web_search_exa": "exa",
}


def ts(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def result_text(block):
    content = block.get("content")
    if isinstance(content, str):
        return content
    return "\n".join(part.get("text", "") for part in content or [] if part.get("type") == "text")


def main(transcript, questions_path, out_path):
    questions = json.load(open(questions_path, encoding="utf-8"))
    by_text = {q["question"]: q["id"] for q in questions}

    calls = {}
    tools_per_message = defaultdict(int)
    with open(transcript, encoding="utf-8") as fh:
        for line in fh:
            entry = json.loads(line)
            message = entry.get("message") or {}
            content = message.get("content")
            if not isinstance(content, list) or "timestamp" not in entry:
                continue
            for block in content:
                if block.get("type") == "tool_use" and block.get("name") in TOOLS:
                    query = block["input"].get("query", "")
                    if query not in by_text:
                        continue
                    calls[block["id"]] = {
                        "qid": by_text[query],
                        "tool": TOOLS[block["name"]],
                        "input": block["input"],
                        "message_id": message.get("id"),
                        "started": entry["timestamp"],
                    }
                    tools_per_message[message.get("id")] += 1
                elif block.get("type") == "tool_result" and block.get("tool_use_id") in calls:
                    call = calls[block["tool_use_id"]]
                    call["finished"] = entry["timestamp"]
                    call["output"] = result_text(block)
                    call["is_error"] = bool(block.get("is_error"))

    runs = defaultdict(list)
    for call_id, call in calls.items():
        if "finished" not in call:
            continue
        call["id"] = call_id
        call["seconds"] = round((ts(call["finished"]) - ts(call["started"])).total_seconds(), 2)
        call["parallel"] = tools_per_message[call["message_id"]] > 1
        runs[(call["qid"], call["tool"])].append(call)

    out = {}
    for question in questions:
        for tool in TOOLS.values():
            history = sorted(runs.get((question["id"], tool), []), key=lambda c: c["started"])
            ok = [c for c in history if not c["is_error"]]
            if not ok:
                raise SystemExit(f"[ERROR] no successful run for {question['id']} {tool}")
            content_run = ok[-1]
            timed = [c for c in ok if not c["parallel"]]
            if not timed:
                raise SystemExit(f"[ERROR] no sequential run to time for {question['id']} {tool}")
            timing_run = timed[-1]
            out.setdefault(question["id"], {})[tool] = {
                "output": content_run["output"],
                "content_call": content_run["id"],
                "content_started": content_run["started"],
                "seconds": timing_run["seconds"],
                "timing_call": timing_run["id"],
                "timing_from_content_call": timing_run["id"] == content_run["id"],
                "runs": len(history),
            }
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for qid, tools in out.items():
        print(qid, " ".join(f"{t}={v['seconds']}s/{len(v['output'])}ch{'' if v['timing_from_content_call'] else '*'}(x{v['runs']})" for t, v in tools.items()))


if __name__ == "__main__":
    main(*sys.argv[1:4])
