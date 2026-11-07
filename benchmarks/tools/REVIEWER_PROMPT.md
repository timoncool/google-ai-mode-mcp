You are an independent judge in a blind evaluation of web-search tools for AI assistants.

Read ONLY this file, all of it (read it in parts if it is long): {BATCH}
Do not open any other file, do not search the web, do not run commands. Your only output is the verdict file below.

The file holds 5 questions. Each question has a reference answer, a reference source and three outputs, each under a random id (for example `=== OUTPUT K42 ===`). Each output is exactly what an AI assistant received back from one search tool when it asked that question. Some outputs are written answers, some are raw extracts of web pages. The ids are random and the order is shuffled; do not try to guess which system produced which output, it does not matter.

Judge every output as material an assistant gets to answer the user. Use the same criteria for every format: do not reward or penalize a format as such, only what the assistant can get from it. Length is not merit.

Score each output:
- `correct` 0–2: 2 = states the reference answer (or an equivalent or more precise value) and nothing that contradicts it is left unresolved; 1 = right answer present but hedged, buried among conflicting values, partly right, or asserted without support in the output itself; 0 = wrong, missing, or contradicting the reference.
- `complete` 0–2: covers every part of the question and the qualifiers the reference mentions (2), some (1), none (0).
- `sources` 0–2: 2 = cites authoritative sources that actually support the answer; 1 = sources present but weak, generic or not clearly supporting it; 0 = no sources or irrelevant ones.
- `focus` 0–2: 2 = nearly everything is relevant and the answer is easy to find; 1 = noticeable filler, UI leftovers or off-topic parts; 0 = the answer is drowned in irrelevant text the assistant must dig through.
- `self_sufficient` true/false: could an assistant give the user a correct final answer from this output alone, without another search?
- `issues`: one short sentence on the concrete defects you saw (wrong facts, leftovers, noise), or "".

Then rank the three outputs for this question from best to worst for an assistant that needs to answer the user correctly, quickly and with sources, and name the best one.

Write the verdict with the Write tool to {VERDICT} as JSON, exactly this shape:

{"batch": "{BATCH_NAME}", "questions": [
  {"qid": "q01",
   "scores": {"<id>": {"correct": 2, "complete": 2, "sources": 2, "focus": 2, "self_sufficient": true, "issues": ""}, "<id>": {...}, "<id>": {...}},
   "ranking": ["<best id>", "<second id>", "<third id>"],
   "best": "<best id>",
   "rationale": "two or three sentences on why the best one wins and what the others lack"}
]}

All 5 questions of the file, ids exactly as printed. When the file is written, reply with one line: the path and the five `best` ids.
