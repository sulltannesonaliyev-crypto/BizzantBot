import os
import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "Salom! Men BizzantBot 🤖\n\n"
            "Buyruqlar:\n"
            "/start — botni boshlash\n"
            "/help — yordam"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "BizzantBot yordam bo‘limi.\n"
            "Hozircha /start va /help buyruqlari mavjud."
        )


def main():
    # Env value is read at startup (and whitespace is stripped).
    token = os.environ.get("BOT_TOKEN", "").strip()
    logger.info("BOT_TOKEN environment variable present: %s", bool(token))

    if not token:
        raise RuntimeError(
            "BOT_TOKEN is missing in this running Railway service. "
            "Check the service/environment attached to this deployment."
        )

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    logger.info("BizzantBot starting polling.")
    app.run_polling()


if __name__ == "__main__":
    main()
