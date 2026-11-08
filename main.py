import logging
import os
from typing import Final

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("bizzantbot")

WELCOME_TEXT: Final = (
    "Salom! Men BizzantBot 🤖\n\n"
    "Buyruqlar:\n"
    "/start — botni boshlash\n"
    "/help — yordam"
)
HELP_TEXT: Final = (
    "BizzantBot yordam bo‘limi.\n"
    "Hozircha /start va /help buyruqlari mavjud."
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_message:
        await update.effective_message.reply_text(WELCOME_TEXT)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_message:
        await update.effective_message.reply_text(HELP_TEXT)


def main() -> None:
    token = os.getenv("BOT_TOKEN", "").strip()

    # Log only deployment metadata and whether the secret exists; never its value.
    logger.info(
        "Startup metadata: service=%s environment=%s deployment=%s commit=%s",
        os.getenv("RAILWAY_SERVICE_NAME", "unknown"),
        os.getenv("RAILWAY_ENVIRONMENT_NAME", "unknown"),
        os.getenv("RAILWAY_DEPLOYMENT_ID", "unknown"),
        os.getenv("RAILWAY_GIT_COMMIT_SHA", "unknown"),
    )
    logger.info("BOT_TOKEN present: %s", bool(token))

    if not token:
        logger.error(
            "BOT_TOKEN is absent from this process. Verify the variable is attached "
            "to this exact Railway service and environment, then deploy staged changes."
        )
        raise RuntimeError("Required environment variable BOT_TOKEN is missing.")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    logger.info("BizzantBot is starting in polling mode.")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
