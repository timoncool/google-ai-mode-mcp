# Google AI Mode MCP — notes for working on the code

Google AI Mode (`google.com/search?udm=50`) as an MCP server. A browser extension runs the searches in the user's own signed-in browser and returns the answer as markdown with citations.

## How a search flows

```
MCP client ─stdio─▶ server/google_ai_scraper/mcp_server/server.py
                        │ HTTP
                        ▼
                  relay server/google_ai_scraper/app.py (127.0.0.1:15551)
                        ▲ long-poll GET /pending?wait=20, POST /result/{id}
                        │
                  extension/background.js ──▶ hidden frame (offscreen document) or a background tab
                                                  └─ extension/content.js extracts the answer
```

- **MCP processes share one relay.** Each MCP process reuses the relay or starts it detached, with `CREATE_NO_WINDOW` on Windows. Several clients share one relay and one extension.
- **Long-poll.** The extension long-polls `/pending`: the relay answers as soon as a query is queued, or after 20 s with nothing. `PENDING_MAX_WAIT` stays under the MV3 30 s idle limit.
- **Hidden frames by default.** `DEFAULT_SEARCH_WINDOW_MODE = "offscreen"` in `background.js` loads the search page in an iframe inside an offscreen document. A declarativeNetRequest session rule strips `X-Frame-Options` and CSP only for `sub_frame` requests to `www.google.com` that come from no tab. The other mode, `current`, opens background tabs.
- **Offscreen frames have no layout.** Their viewport is 0×0, so `offsetParent` and sizes are useless there. Visibility is decided by computed style (`isShown`, `cloneVisible`).
- **Completion marker.** An answer is complete when Google renders the rating buttons `[data-snt]` under it, in every UI language.
- **Threads.** A thread stays open for follow-ups for 120 s of inactivity (`THREAD_TTL`). With close-after-search on (the default), the page is closed right after the answer and the thread is parked with its conversation URL for 30 minutes. A follow-up reopens that URL with `#_resume=1&_oq=<id>&_fq=<question>` and types the question there.

## Answer extraction (`extension/content.js`)

- **`cloneVisible(root)` works on the live tree, then clones.** Hidden elements and the answer footer are dropped there: the footer holds the rating buttons, legal links in a hidden menu and the AI disclaimer. It also does two conversions:
  - formulas, drawn as aria-hidden SVGs of positioned glyphs, become text with `^`/`_`;
  - names rendered as `span[role=button]` chips are unwrapped to plain text.
- **`answerMarkdown(clone, question)`** finishes the cleanup and runs Turndown:
  - code blocks become fenced blocks with their language, without the copy caption;
  - UI elements and source-card clusters are removed;
  - the first heading goes only if it repeats the question.
- **Follow-ups** extract the newest `main-col` through the same functions.

Selectors that do not depend on the UI language are a requirement. The extension must work in any Google interface language: test both English and Russian.

## Files

| Path | What |
|---|---|
| `server/google_ai_scraper/mcp_server/server.py` | MCP tools `search`, `search_many`, `follow_up`, `generate_image`, `health`; relay start-up; `--extension` installer |
| `server/google_ai_scraper/app.py` | Relay: query queue, long-poll, threads, parked threads, image queue |
| `server/pyproject.toml` | Package `google-ai-mode-mcp`; the extension folder is bundled into the wheel |
| `extension/` | Chrome MV3 extension: `background.js`, `content.js`, `offscreen.*`, popup, options, `_locales/{en,ru}` |
| `firefox-extension/` | Firefox copy; only `manifest.json` is its own, the rest comes from `scripts/sync-firefox-extension.sh` |
| `skills/google-ai-mode/SKILL.md` | Skill telling Claude when and how to search |
| `benchmarks/` | Benchmark report, procedure and scripts |
| `tests/` | Node tests for the background worker |

## Working on it

- **Extension.** Load `extension/` unpacked in `chrome://extensions`. After editing extension files, press the reload arrow on its card; the relay and MCP do not need a restart.
- **MCP from a checkout:** `uv run --directory server google-ai-mode-mcp`.
- **Relay checks:** `curl http://127.0.0.1:15551/health` shows whether the extension is polling. Send non-ASCII questions to `/ask` from Python rather than Git Bash `curl`, which garbles Cyrillic on Windows.
- **Tests.** Check syntax with `node --check extension/*.js` and run `node tests/background-restart.test.js`. Then verify on real searches through the MCP tools: a plain fact, a formula, a code answer, a Russian question and a follow-up.
- **Firefox.** After changing shared extension files, run `scripts/sync-firefox-extension.sh`, or copy the changed file into `firefox-extension/`.
