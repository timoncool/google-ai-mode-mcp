"""Turn raw tool outputs into blind review batches.

Strips only what the harness or the tool adds around the content (JSON envelopes,
thread ids, the harness reminder), keeps every word of the content itself, gives
each output a random id per question and shuffles the order.

Usage: python normalize.py <raw.json> <questions.json> <review_dir> <mapping.json> [seed]
"""
import json
import random
import re
import string
import sys
from pathlib import Path

TOPICS = ["tech", "science", "history-geo", "howto", "multihop"]


def google_ai_mode(raw):
    envelope = json.loads(raw)
    data = json.loads(envelope["result"]) if "result" in envelope else envelope
    if data.get("error"):
        raise SystemExit(f"[ERROR] tool error kept in output: {data['error']}")
    sources = list(data.get("citations") or [])
    markdown = data["markdown"]

    def cite(match):
        url = match.group(1)
        if url not in sources:
            sources.append(url)
        return f" [{sources.index(url) + 1}]"

    markdown = re.sub(r"\[\]\((\S+?)\)", cite, markdown)
    return markdown.strip(), sources


def websearch(raw):
    text = raw.split("\n\nREMINDER: You MUST include the sources", 1)[0]
    links_match = re.search(r"^Links: (\[.*\])$", text, re.M)
    sources = [link["url"] for link in json.loads(links_match.group(1))] if links_match else []
    body = text[links_match.end():] if links_match else text
    body = re.sub(r"^Web search results for query: .*$", "", body, flags=re.M)
    return body.strip(), sources


def exa(raw):
    return raw.strip(), []


NORMALIZERS = {"google_ai_mode": google_ai_mode, "websearch": websearch, "exa": exa}


def render(answer_id, body, sources):
    lines = [f"=== OUTPUT {answer_id} ===", body]
    if sources:
        lines.append("")
        lines.append("Sources:")
        lines.extend(f"{i}. {url}" for i, url in enumerate(sources, 1))
    lines.append(f"=== END OF OUTPUT {answer_id} ===")
    return "\n".join(lines)


def main(raw_path, questions_path, review_dir, mapping_path, seed="20261107"):
    rng = random.Random(seed)
    raw = json.load(open(raw_path, encoding="utf-8"))
    questions = json.load(open(questions_path, encoding="utf-8"))
    review_dir = Path(review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)

    mapping, normalized, used = {}, {}, set()
    batches = {topic: [] for topic in TOPICS}
    for question in questions:
        entries = []
        for tool, run in raw[question["id"]].items():
            body, sources = NORMALIZERS[tool.split(":")[0]](run["output"])
            while True:
                answer_id = rng.choice(string.ascii_uppercase) + str(rng.randint(10, 99))
                if answer_id not in used:
                    used.add(answer_id)
                    break
            mapping.setdefault(question["id"], {})[answer_id] = tool
            normalized.setdefault(question["id"], {})[tool] = {"id": answer_id, "body": body, "sources": sources}
            entries.append(render(answer_id, body, sources))
        rng.shuffle(entries)
        block = [
            f"########## QUESTION {question['id']} ##########",
            f"Question: {question['question']}",
            f"Reference answer: {question['reference']}",
            f"Reference source: {question['source']}",
            "",
            "\n\n".join(entries),
        ]
        batches[question["topic"]].append("\n".join(block))

    for index, topic in enumerate(TOPICS, 1):
        (review_dir / f"batch{index}.md").write_text("\n\n\n".join(batches[topic]) + "\n", encoding="utf-8")
    json.dump(mapping, open(mapping_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(normalized, open(Path(mapping_path).with_name("normalized.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for index in range(1, len(TOPICS) + 1):
        size = (review_dir / f"batch{index}.md").stat().st_size
        print(f"[OK] batch{index}.md {size} bytes")


if __name__ == "__main__":
    main(*sys.argv[1:6])
