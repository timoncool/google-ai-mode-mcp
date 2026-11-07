---
name: google-ai-mode
description: Web research through Google AI Mode (the google-ai-mode MCP server) — one call returns Google's AI answer synthesized from many sources, with citations and follow-ups in the same conversation. Use for any question that needs current information from the web: latest versions and release notes, news, prices, docs and APIs, comparisons, "what is X", "how do I", facts to verify. Prefer it over reading search results page by page; trigger words — найди, погугли, поищи, что нового, какая последняя версия, сколько стоит, сравни, search, google, look up, latest.
---

# Google AI Mode search

The `google-ai-mode` MCP server asks Google AI Mode in the user's own browser (their Google account) and returns the answer as Markdown with source links. One answer usually replaces reading 5–10 pages, at a fraction of the tokens.

## Tools

| Goal | Tool | Notes |
|---|---|---|
| One question | `search(query)` | Answer + `citations` + `thread_id` |
| Several independent questions | `search_many(queries=[...])` | Up to 10 in parallel; one call costs about as much time as one search |
| Dig deeper into the same topic | `follow_up(query, thread_id)` | Keeps the conversation context; ask 1–3 follow-ups instead of a new search |
| Local prices, availability, news | `search(query, gl="us")` | `gl` = country; without it results follow the user's location |
| Quick fact (date, number, definition) | `search(query, mode="fast")` | Faster, shorter |
| Check the setup | `health()` | Server and browser-extension status |

## How to ask

- Write the query as a full question in the language you want the answer in: the answer follows the language of the query (`hl` only changes Google's interface).
- Put the year or "latest"/"today" into the query when freshness matters.
- Split a broad task into independent questions and send them with `search_many`, then use `follow_up` on the thread that needs depth.
- Quote numbers and versions with their source from `citations`; for anything critical, open the cited page.

## Errors

Every error comes with a `hint`. The common ones:

- `google_captcha` — ask the user to open Google in the browser and solve the CAPTCHA, then retry.
- `Extension not connected` / timeout — the browser with the extension must be running; ask the user to open Chrome.
- `Thread expired` — start a new `search`; threads live 30 minutes.
- `quota_exhausted_all_accounts` — retry later or with `mode="fast"`.

Do not fall back silently to other search tools when this server fails: report the error and its hint to the user.
