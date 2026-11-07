# Benchmark: Google AI Mode MCP vs Claude Code WebSearch vs Exa

Run of 7 November 2026. 25 questions, three search tools an AI coding assistant can call, one blind AI judge. Every input, raw output, verdict and script is in this folder, so the numbers below can be recomputed and the run repeated with other tools ([PROCEDURE.md](PROCEDURE.md)).

## Result

| | Google AI Mode MCP | Claude Code WebSearch | Exa `web_search_exa` |
|---|---|---|---|
| Best answer (of 25) | **10** | 5 | **10** |
| Mean rank (1 = best) | **1.76** | 2.36 | 1.88 |
| Mean score, of 8 | **6.96** | 6.72 | 6.76 |
| Fully correct | **23/25** | 19/25 | **23/25** |
| Correct, 0–2 | **1.92** | 1.76 | **1.92** |
| Complete, 0–2 | **1.96** | 1.92 | 1.88 |
| Sources, 0–2 | 1.32 | 1.16 | **1.96** |
| Focus, 0–2 | 1.76 | **1.88** | 1.00 |
| Answer from this output alone | **25/25** | **25/25** | 24/25 |
| Median time per call | 3.1 s | 5.1 s | **0.95 s** |
| Median output size | 1.1k chars | 0.8k chars | 15.5k chars |
| Output for all 25 questions | 31k chars | 21k chars | 433k chars |

- **Google AI Mode MCP** gave the best answers overall: best mean rank and best mean score, tied with Exa for the most wins. It was right as often as Exa while handing the assistant 14 times less text, and it was 1.6 times faster than the built-in WebSearch.
- **Its weak point is sources.** It cited fewer and weaker sources than Exa. For three simple facts (q08, q13, q24) Google showed no sources at all: checked live for q08 and q24, the AI Mode page has no external link.
- **Exa** is the fastest by far and its sources are the best. It returns raw page extracts with no written answer, though, so the assistant reads about 15k characters per question and must reconcile conflicting values itself. Both of its multi-hop misses (q21, q25) are cases where the answer has to be derived, not quoted.
- **WebSearch** writes the most compact answers. It was right least often (19/25) and twice answered from the model's own knowledge because its results did not contain the fact (q21, q25).

Wins by topic:

| Topic | AI Mode | WebSearch | Exa |
|---|---|---|---|
| tech | 3 | 0 | 2 |
| science | 0 | 1 | 4 |
| history-geo | 3 | 0 | 2 |
| howto | 1 | 2 | 2 |
| multihop | 3 | 2 | 0 |

## Defects of our MCP found by this benchmark

The judge saw Google AI Mode MCP output with every defect below that was still present at review time. All six were in the extension's text extraction, not in Google's answers:

| Defect | Seen in | Status |
|---|---|---|
| Formulas were dropped (Avogadro constant, C‑14) | q06, q07 | fixed in 9d9cbab before the runs that were judged |
| Names shown as clickable chips were dropped (Curie, Baikal) | q12, q13 | fixed in a2fd140 before the runs that were judged |
| The code block caption "Use code with caution" and the language label leaked into the text | q17–q20 | judged with the defect, fixed after the review |
| The answer footer (AI disclaimer, legal links) leaked into the text | q09, q10 | judged with the defect, fixed after the review |
| The first real section heading was dropped as if it repeated the question | q20 | judged with the defect, fixed after the review |
| Adjacent bold runs came out as `****` | q11, q13, q17 | judged with the defect, fixed after the review |

So the scores above are for the build before the last four fixes. The fixes remove the "UI leftovers" the judge deducted focus for on q09, q10 and q17–q20. They do not touch the source deductions.

## Per question

Score = correct + complete + sources + focus, each 0–2, as given by the blind judge.

| # | Topic | Question | Best | AI Mode | WebSearch | Exa |
|---|---|---|---|---|---|---|
| q01 | tech | Which RFC defines HTTP/3, and over which transport protocol does it run? | AI Mode | 8 | 8 | 7 |
| q02 | tech | С какой версии Python порядок вставки ключей в dict гарантирован спецификацией языка? | Exa | 7 | 8 | 7 |
| q03 | tech | Какое значение по умолчанию у параметра max_connections в PostgreSQL? | Exa | 7 | 7 | 7 |
| q04 | tech | In which Rust release did the 2021 edition become stable? | AI Mode | 8 | 7 | 7 |
| q05 | tech | Какой HTTP-код означает «Misdirected Request» и в каком RFC он сейчас определён? | AI Mode | 8 | 7 | 7 |
| q06 | science | What is the half-life of carbon-14? | Exa | 7 | 6 | 6 |
| q07 | science | Какое точное значение у постоянной Авогадро после переопределения СИ в 2019 году? | Exa | 7 | 7 | 7 |
| q08 | science | What is the boiling point of liquid nitrogen at 1 atm in degrees Celsius? | Exa | 5 | 7 | 7 |
| q09 | science | Какой нормальный пульс в покое у взрослого человека по данным American Heart Association? | Exa | 6 | 7 | 7 |
| q10 | science | Which enzyme does aspirin irreversibly inhibit, and by what mechanism? | WebSearch | 7 | 8 | 7 |
| q11 | history-geo | В каком году был подписан Вестфальский мир? | AI Mode | 8 | 7 | 7 |
| q12 | history-geo | What is the maximum depth of Lake Baikal? | AI Mode | 8 | 5 | 7 |
| q13 | history-geo | Кто первая женщина — лауреат Нобелевской премии, в какой области и в каком году? | Exa | 5 | 5 | 7 |
| q14 | history-geo | When was the first transatlantic telegraph cable completed, and when did a lasting connection begin? | AI Mode | 8 | 5 | 7 |
| q15 | history-geo | Какая высота у горы Килиманджаро? | Exa | 7 | 5 | 7 |
| q16 | howto | How do I undo the last git commit but keep its changes staged? | AI Mode | 8 | 7 | 7 |
| q17 | howto | Как в Linux узнать, какой процесс слушает порт 8080? | WebSearch | 6 | 7 | 7 |
| q18 | howto | Python: how to read a large file line by line without loading it into memory? | Exa | 6 | 7 | 7 |
| q19 | howto | Как с помощью ffmpeg сделать GIF из видео с частотой 10 кадров в секунду и шириной 480 пикселей? | WebSearch | 6 | 7 | 6 |
| q20 | howto | How do I delete duplicate rows in PostgreSQL while keeping one row per group? | Exa | 6 | 7 | 7 |
| q21 | multihop | Who was the US president when the Hubble Space Telescope was launched? | AI Mode | 7 | 6 | 5 |
| q22 | multihop | Какой язык программирования создал автор Turbo Pascal, уже работая в Microsoft? | WebSearch | 7 | 8 | 7 |
| q23 | multihop | В каком городе родился автор балета «Весна священная»? | AI Mode | 8 | 7 | 7 |
| q24 | multihop | What is the capital of the country where most of the Atacama Desert lies? | WebSearch | 6 | 7 | 7 |
| q25 | multihop | Сколько лет прошло от первой высадки человека на Луну до запуска первого модуля МКС? | AI Mode | 8 | 6 | 5 |

The judge's ranking, per-output scores, the defects it saw and its reasoning for every question are in [2026-11-07/results.json](2026-11-07/results.json).

## How it was run

- **Questions.** 25 questions in 5 topics (tech facts, science, history and geography, how-to, multi-hop), English and Russian. All have stable answers, so the run can be repeated. Each has a reference answer and source written before any tool was called: [questions.json](2026-11-07/questions.json).
- **Tools**, each called with its defaults and the question text verbatim:
  - Google AI Mode MCP `search` (this project, "pro" mode, through a signed-in Chrome);
  - Claude Code's built-in `WebSearch` in `standard` mode;
  - Exa MCP `web_search_exa`, with `objective` set to "Answer this question: …" and the default 10 results.
- **Order.** One call per message, strictly one after another, A → B → C for each question, all from one Claude Code session on one machine.
- **Timing** is the time between the tool call and its result in the session transcript. It includes the MCP and harness overhead every assistant pays.
  - The q01–q12 Google AI Mode answers were re-run after the two extraction fixes above. Those re-runs were made in parallel, so their timings are not used. The timings for these questions come from the earlier sequential runs, the content from the re-runs.
- **Blinding.** [normalize.py](tools/normalize.py) strips only the envelopes the tools add around their content: the JSON wrapper and thread ids, and the harness reminder after WebSearch results. Every word of the content is kept. It then gives each output a random id per question and shuffles the order. The id→tool map ([mapping.json](2026-11-07/mapping.json)) was never shown to the judge.
- **Judge.** Claude Opus 5.5 (`claude-opus-5-5`) with the prompt in [REVIEWER_PROMPT.md](tools/REVIEWER_PROMPT.md).
  - The material is about 600 KB, too much for one context, so the same judge prompt ran as five independent instances, one per topic. Each instance had 5 questions × 3 outputs.
  - The judges' transcripts confirm that each read only its own batch file and wrote only its verdict. They used no search and no other file.
  - Inputs and verdicts: [verdicts/](2026-11-07/verdicts/).
- **Totals** come from [aggregate.py](tools/aggregate.py) and are written to `results.json`.

## Limits

- **Small sample.** 25 questions with one run per tool. Google AI Mode does not answer the same question identically twice. A difference of one or two wins is within noise; the mean rank and the fully correct counts are steadier.
- **One judge model.** Its taste in sources and noise is one opinion.
- **Account-dependent.** Google AI Mode answers depend on the signed-in Google account, its language and location; this run used a Russian-language account.
- **Timing scope.** Times were measured on one machine and connection, at one time of day.
