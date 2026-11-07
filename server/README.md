# google-ai-mode-mcp (server package)

The MCP server and the local relay of [Google AI Mode MCP](https://github.com/timoncool/google-ai-mode-mcp). Installation, tools and how it works are in the [main README](https://github.com/timoncool/google-ai-mode-mcp#readme); this page is for running the package from source.

## Run

```bash
uvx --from git+https://github.com/timoncool/google-ai-mode-mcp#subdirectory=server google-ai-mode-mcp
```

From a checkout:

```bash
uv run --directory server google-ai-mode-mcp
```

The process speaks MCP over stdio. On start it reuses the relay on `127.0.0.1:15551`, or starts it in the background if none is running, so several MCP clients share one relay and one browser extension.

## Options

| Flag | What it does |
|---|---|
| `--extension` | Copy the bundled browser extension to a fixed folder and print how to load it |
| `--backend` | Run only the relay (FastAPI) |
| `--no-server` | Do not start or reuse a relay; talk to the one at `GOOGLE_AI_SCRAPER_URL` |
| `--sse` | MCP over SSE instead of stdio |
| `--port N` | Relay port, 15551 by default |

| Variable | Default | What it does |
|---|---|---|
| `GOOGLE_AI_SCRAPER_URL` | `http://127.0.0.1:15551` | Relay address |
| `GOOGLE_AI_SCRAPER_CLOSE_AFTER_SEARCH` | `1` | Close the search page right after the answer; `0` keeps it for follow-ups |

## Relay HTTP API

| Endpoint | Purpose |
|---|---|
| `GET /ask?q=…&thread_id=…&close_thread=…&mode=…&hl=…&gl=…&authuser=…` | Ask a question or a follow-up; returns `markdown`, `citations`, `thread_id` |
| `GET /generate_image?prompt=…` | Generate an image in AI Mode |
| `DELETE /thread/{thread_id}` | Close a conversation |
| `GET /health`, `GET /version` | Relay and extension status |
| `GET /pending?wait=20`, `POST /result/{id}`, `POST /image_result/{id}` | Used by the extension |
