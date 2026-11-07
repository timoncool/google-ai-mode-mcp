# Does the skill help? Before and after

The same 25 questions as the [first run](../README.md), asked through Google AI Mode MCP twice on the same extension build:
- **before** — the question verbatim;
- **after** — the question written by the [`google-ai-mode` skill](../../skills/google-ai-mode/SKILL.md) templates: name the source to trust, say the answer's shape, ask for intermediate facts on multi-step questions.

The skill wording for every question was fixed before the runs: [skill_queries.json](skill_queries.json). The 50 calls ran one at a time.

## Result

| | First run (old build) | Before the skill | After the skill |
|---|---|---|---|
| Reference facts in the answer | 25/25 | 25/25 | 25/25 |
| Official or primary source cited | 10/24 | 13/24 | **22/24** |
| Answers without any source | 3 | 2 | **0** |
| Ending with an offer of more help | 22 | 23 | **0** |
| Google UI text leaked into the answer | 6 | **0** | **0** |
| Median answer length | 1,095 chars | 1,085 chars | **532 chars** |
| All 25 answers | 31.5k chars | 29.5k chars | **16.0k chars** |
| Median time | 3.13 s | 3.02 s | 3.18 s |

- **The skill changes the sources, not the facts.** Every variant contains the reference facts. With the source named in the question, the answer cites it — NIST, docs.python.org, postgresql.org, git-scm.com, man7.org, ffmpeg.org, nobelprize.org, RFC Editor — in 22 of 24 questions instead of 13.
- **Half the text, no closing offers.** "Answer in 2–3 sentences" and "give the command and a one-line explanation" halve the answer. "No follow-up offers" removes the closing paragraph every time. The cost is 0.16 s of median time.
- **Fixes, not the skill.** The UI leaks (6 → 0) went away with the extension fixes made during this work, not with the skill.
- **Where the skill did worse:**
  - q22: the plain answer cited microsoft.com, but only its home page; the skill answer cited Wikipedia and articles;
  - q24: the plain answer cited Britannica, the skill answer only Wikipedia.

## How it was measured

No judge this time: [objective_metrics.py](../tools/objective_metrics.py) checks every answer against [checks.json](checks.json), written before the comparison. The checks are:
- the reference facts, as keywords;
- the primary-source domains for each question;
- the number of sources;
- a closing offer;
- leaked Google UI text;
- length.

The keyword check proves a fact is present, not that the answer is free of errors; the [first run](../README.md) has the blind judge's view of correctness.

All outputs: [raw.json](raw.json) (`google_ai_mode:plain`, `google_ai_mode:skill`; WebSearch and Exa from the first run). Per-question numbers: [objective_metrics.json](objective_metrics.json).
