# How to benchmark search tools for an AI assistant

A repeatable procedure for comparing any search tools an assistant can call (MCP servers, built-in web search, APIs) on speed, correctness, sourcing and noise, with a blind AI judge. The [2026-11-07 run](README.md) follows it step by step; its files are the worked example.

## 1. Questions first, answers fixed in advance

- **Stable answers.** Pick questions whose answers do not change: specifications, constants, dates, how-to recipes, facts that need two hops. Prices, news and "latest version" questions cannot be repeated or checked later.
- **Spread.** 5 topics × 5 questions is the minimum that says something per topic. Mix the languages your users ask in, and include multi-hop questions: the answer has to be derived from two facts, not quoted.
- **Reference first.** Before calling any tool, write the reference answer and the source that proves it into `questions.json`:

```json
{"id": "q01", "topic": "tech", "question": "...", "reference": "...", "source": "https://..."}
```

## 2. Run every tool the same way

- **One session, one machine.** Run all tools from a single assistant session; the session transcript is the record of what each tool returned and when.
- **Same input.** Send the question text verbatim, with each tool's default settings. Write down any setting you had to give (for example a required `objective`).
- **Strict order.** One call per message, one after another, every tool for a question before the next question (A → B → C). Calls made in parallel share the network and the harness, so their times are not comparable.
- **Redo cleanly.** If a tool fails or you fix your own tool mid-run, re-run the affected calls sequentially and keep both runs: the extractor takes the latest successful run for content and the latest sequential run for timing.

## 3. Extract outputs and timings

```bash
python tools/extract.py <session.jsonl> questions.json raw.json
```

It matches each tool call in the transcript to its question by the exact text and stores:
- the raw output;
- the time from the call to its result;
- whether the call ran alone in its message.

It fails loudly when a question has no successful or no sequential run. To add a tool, add its tool name to `TOOLS` in `extract.py`.

## 4. Blind the outputs

```bash
python tools/normalize.py raw.json questions.json <review_dir> mapping.json
```

- **Envelopes only.** Strip only what the tool or harness wraps around the content (JSON envelopes, ids, harness reminders). Never edit the content: leftovers, noise and missing sources are what is being measured. To add a tool, add a normalizer to `NORMALIZERS`.
- **Random ids, shuffled order.** Every output gets a random id per question and the order inside each question is shuffled.
- **One file per topic.** The review files are written one per topic; the id→tool map goes to `mapping.json`.
- **Keep the judge away from tool data.** Put the review files in a folder the judge has no other reason to open, away from `raw.json` and `mapping.json`.

## 5. Judge blind

- **Prompt.** Fill [REVIEWER_PROMPT.md](tools/REVIEWER_PROMPT.md): `{BATCH}` is the review file, `{VERDICT}` the verdict path, `{BATCH_NAME}` its name. Run it with the strongest model you have, one independent instance per review file. The judge must see whole outputs, so split by file rather than truncate.
- **Criteria**, scored 0–2 each, the same for written answers and raw page extracts:
  - correct;
  - complete;
  - sources;
  - focus;
  - plus whether the assistant could answer from this output alone, a ranking and the best id.
- **Check the judge**, from each judge's transcript:
  - which model actually ran;
  - that it read only its own review file;
  - that it used no web search.

## 6. Unblind and total

```bash
python tools/aggregate.py <run_dir>
```

It checks that every verdict uses exactly the ids of its question, maps them back to tools and writes `results.json`. The file holds:
- wins and mean rank;
- mean of each criterion;
- the fully correct count;
- median time;
- output size;
- per-question scores with the judge's notes.

## 7. Verify before you conclude

- **Check what you blame on your tool.** Treat every defect the judge names against your own tool as a lead, not a fact. Reproduce it on the live tool before fixing it, and separate defects of your tool from the behaviour of the service behind it. In the 2026-11-07 run, "no sources" turned out to be Google showing none, while "Use code with caution" was a real extraction bug.
- **Publish the defects.** List the defects you found and say which scores they affected.
- **State the limits.** Give the sample size, the single judge, one run per tool and anything account- or region-dependent.
