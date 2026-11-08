# BizzantBot — fresh start

Minimal Telegram bot configured for Railway worker deployment.

## Commands
- `/start` — start message
- `/help` — help
- Unknown commands receive a short response

## Railway deployment
1. Connect this repository to a Railway service.
2. Use a **worker** service (not a web server).
3. Add `BOT_TOKEN` to the Variables of the same service and environment.
4. Deploy the latest commit from `main`.

The start command is in `Procfile`. There is intentionally no `runtime.txt` version pin: Railway/Railpack should select its supported Python runtime. The token is never stored in the repository or printed in logs.

If the process logs that `BOT_TOKEN` is missing, that variable is not present in the environment attached to the active process. Source-code changes cannot attach Railway variables to a service.

## Local use
Install dependencies with `pip install -r requirements.txt`, set `BOT_TOKEN` in your shell, then run `python main.py`.
