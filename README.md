# BizzantBot

Telegram bot starter project for Railway, built with Python and `python-telegram-bot`.

## Features

- `/start` — greeting and command list
- `/help` — help message
- Long polling (no public URL or webhook required)
- Startup logs with Railway service/environment/deployment metadata
- Secret-safe diagnostics: the bot never prints the `BOT_TOKEN` value

## Deploy on Railway

1. Connect this GitHub repository to a Railway **worker** service.
2. In that same service and target environment, add the variable:
   - `BOT_TOKEN` = token from Telegram's `@BotFather`
3. Review and deploy any staged variable changes.
4. Deploy the latest commit from the `main` branch.
5. Open the deployment logs. A healthy startup includes `BOT_TOKEN present: True` and `BizzantBot is starting in polling mode.`

The repository uses `Procfile` to start the bot with `python -u main.py`. Do not configure this service as a web server.

## Local run

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
# Set BOT_TOKEN in your shell (do not commit it), then:
python main.py
```

## Troubleshooting

If the log says `BOT_TOKEN present: False`, the Python process did not receive the variable. Confirm that the variable belongs to the exact Railway service and environment used by the active deployment. The bot cannot fix Railway variable scoping from source code.

Never commit `.env`, bot tokens, or credentials.
