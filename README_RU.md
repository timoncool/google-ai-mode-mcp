<div align="center">

<img src="docs/icon.png" width="128" alt="Иконка Google AI Mode MCP" />

# Google AI Mode MCP

**Режим ИИ Google для Claude и любого MCP-клиента — ответы с источниками из вашего собственного браузера примерно за три секунды, без вкладок, без ключей API и без своих лимитов.**

[![Stars](https://img.shields.io/github/stars/timoncool/google-ai-mode-mcp?style=flat-square)](https://github.com/timoncool/google-ai-mode-mcp/stargazers)
[![License](https://img.shields.io/github/license/timoncool/google-ai-mode-mcp?style=flat-square)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/timoncool/google-ai-mode-mcp?style=flat-square)](https://github.com/timoncool/google-ai-mode-mcp/commits/main)
[![Issues](https://img.shields.io/github/issues/timoncool/google-ai-mode-mcp?style=flat-square)](https://github.com/timoncool/google-ai-mode-mcp/issues)

**[English](README.md)** · **[Русский](README_RU.md)**

</div>

Режим ИИ Google сам читает десятки страниц и пишет один ответ со ссылками. Этот MCP-сервер отдаёт такой ответ вашему агенту: Claude задаёт вопрос, маленькое расширение спрашивает Google в вашем Chrome под вашим аккаунтом, и ответ возвращается чистым Markdown с источниками. Один вызов заменяет чтение пяти-десяти страниц и стоит в разы меньше токенов.

## Возможности

- **Быстро** — в наших замерах в среднем около 3 с на ответ (6,2 с → 3,2 с против расширения, из которого вырос проект): ответ забирается в тот же миг, когда Google помечает его готовым, а запрос попадает в расширение сразу, без опроса по таймеру.
- **Невидимо** — в Chrome каждый поиск идёт в скрытом offscreen-фрейме: ни вкладки, ни окна, на экране ничего не мелькает.
- **Уточнения** — можно спрашивать дальше в том же диалоге Google; он открывается заново по ссылке даже после закрытия фрейма, 30 минут.
- **Параллельно** — `search_many` отправляет до 10 вопросов сразу, примерно за время одного.
- **По стране** — `gl="us"` (или любая страна) для цен, наличия и местных новостей.
- **Любой язык интерфейса** — работает с Google на русском, английском и любом другом.
- **Чистые ответы** — никакого мусора интерфейса в тексте, кириллица идёт текстом, а не `\uXXXX`.
- **Понятные ошибки** — капча, уснувшее расширение или исчерпанная квота приходят агенту с подсказкой, что делать.
- **Ваш аккаунт, ваш компьютер** — без ключей API и платных прокси, наружу уходит только сам поисковый запрос.

## Установка

Нужны [uv](https://docs.astral.sh/uv/) и Chrome (Firefox тоже подходит, но вместо скрытых фреймов — фоновые вкладки).

**1. MCP-сервер — одной командой:**

```bash
claude mcp add google-ai-mode -- uvx --from git+https://github.com/timoncool/google-ai-mode-mcp#subdirectory=server google-ai-mode-mcp
```

Claude Desktop, Cursor и другие клиенты — та же команда в их конфиге:

```json
{
  "mcpServers": {
    "google-ai-mode": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/timoncool/google-ai-mode-mcp#subdirectory=server", "google-ai-mode-mcp"]
    }
  }
}
```

**2. Расширение браузера** — едет внутри пакета:

```bash
uvx --from git+https://github.com/timoncool/google-ai-mode-mcp#subdirectory=server google-ai-mode-mcp --extension
```

Команда кладёт расширение в постоянную папку и печатает её путь. Откройте `chrome://extensions`, включите **Режим разработчика**, нажмите **Загрузить распакованное расширение** и выберите эту папку. Обновление — та же команда и круглая стрелка на карточке расширения.

**3. Скилл (по желанию)** — скопируйте [`skills/google-ai-mode`](skills/google-ai-mode/SKILL.md) в `~/.claude/skills/`, и Claude будет знать, когда искать и как спрашивать.

## Инструменты

| Инструмент | Что делает |
|---|---|
| `search(query, mode, gl, hl)` | Один вопрос → ответ, `citations`, `thread_id`. `mode="fast"` для быстрых фактов, `gl` — страна |
| `search_many(queries)` | До 10 независимых вопросов параллельно, ответы в том же порядке |
| `follow_up(query, thread_id)` | Следующий вопрос в том же диалоге |
| `generate_image(prompt, save_path)` | Картинка из генератора Google в режиме ИИ |
| `health()` | Состояние сервера и расширения, с подсказкой, если что-то не так |

Спрашивайте на том языке, на котором нужен ответ: ответ идёт на языке вопроса (`hl` меняет только интерфейс Google).

## Как это работает

```
Claude ──MCP──▶ google-ai-mode-mcp ──HTTP──▶ локальный ретранслятор :15551 ◀──long-poll── расширение браузера
                                                                                              │
                                                   скрытый offscreen-фрейм: google.com/search?udm=50
```

- MCP-сервер поднимает маленький локальный ретранслятор. Расширение держит к нему открытый запрос и получает каждый вопрос в момент его появления.
- В Chrome вопрос открывается в iframe offscreen-документа. Google запрещает встраивать свои страницы, поэтому правило сессии снимает этот запрет только для запросов, не принадлежащих ни одной вкладке; обычный браузинг не затрагивается.
- Ответ забирается, когда Google рисует под ним кнопки оценки, скрытый текст интерфейса отбрасывается, а ссылка на диалог сохраняется для уточнений.

Настройки (параметры расширения): где идёт поиск — в скрытых фреймах (по умолчанию) или в фоновых вкладках. Переменные окружения: `GOOGLE_AI_SCRAPER_URL` — адрес ретранслятора, `GOOGLE_AI_SCRAPER_CLOSE_AFTER_SEARCH=0` — не закрывать вкладки между уточнениями в режиме вкладок.

**Ограничения.** Поиск идёт так же, как у человека, — через ваш браузер; Google может показать капчу: откройте Google, пройдите её и повторите. Скрытые фреймы работают в Chrome и других Chromium-браузерах, Firefox использует фоновые вкладки.

Вдохновлено проектом [balakumardev/google-ai-scraper](https://github.com/balakumardev/google-ai-scraper).

## Другие проекты [@timoncool](https://github.com/timoncool)

| Проект | Описание |
|--------|----------|
| [telegram-api-mcp](https://github.com/timoncool/telegram-api-mcp) | Telegram Bot API целиком как MCP-сервер |
| [civitai-mcp-ultimate](https://github.com/timoncool/civitai-mcp-ultimate) | Civitai API как MCP-сервер — модели, картинки, промпты |
| [trail-spec](https://github.com/timoncool/trail-spec) | TRAIL — протокол отслеживания контента между MCP |
| [ACE-Step Studio](https://github.com/timoncool/ACE-Step-Studio) | AI-студия музыки — песни, вокал, каверы, клипы |
| [VideoSOS](https://github.com/timoncool/videosos) | AI-видеопродакшн в браузере |
| [Bulka](https://github.com/timoncool/Bulka) | Платформа лайв-кодинга музыки |

## Авторы

- **Nerual Dreming** — [Telegram](https://t.me/nerual_dreming) | [neuro-cartel.com](https://neuro-cartel.com) | [ArtGeneration.me](https://artgeneration.me)

## Поддержать автора

Я создаю опенсорс софт и занимаюсь исследованиями в области ИИ. Большая часть всего, что я делаю, находится в открытом доступе. Ваши пожертвования позволяют мне создавать и исследовать больше, не отвлекаясь на поиск еды для продолжения существования =)

**[Все способы поддержки](https://github.com/timoncool/ACE-Step-Studio/blob/master/DONATE.md)** | **[dalink.to/nerual_dreming](https://dalink.to/nerual_dreming)** | **[boosty.to/neuro_art](https://boosty.to/neuro_art)**

- **BTC:** `1E7dHL22RpyhJGVpcvKdbyZgksSYkYeEBC`
- **ETH (ERC20):** `0xb5db65adf478983186d4897ba92fe2c25c594a0c`
- **USDT (TRC20):** `TQST9Lp2TjK6FiVkn4fwfGUee7NmkxEE7C`

## Star History

<a href="https://github.com/timoncool/google-ai-mode-mcp/stargazers">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="docs/stars-dark.svg" />
   <source media="(prefers-color-scheme: light)" srcset="docs/stars-light.svg" />
   <img alt="Star History Chart" src="docs/stars-light.svg" />
 </picture>
</a>

## Лицензия

MIT
