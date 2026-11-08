import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("bizzantbot")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    if message:
        await message.reply_text(
            "Assalomu alaykum! 🤖\n"
            "Bot ishga tushdi.\n\n"
            "Buyruqlar:\n"
            "/start — boshlash\n"
            "/help — yordam"
        )


async def help_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    message = update.effective_message
    if message:
        await message.reply_text(
            "Yordam bo‘limi.\n"
            "/start — botni boshlash\n"
            "/help — buyruqlar haqida"
        )


async def unknown_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    message = update.effective_message
    if message:
        await message.reply_text(
            "Bu buyruq tanilmadi. /help buyrug‘ini yuboring."
        )


def main() -> None:
    token = os.getenv("BOT_TOKEN", "").strip()

    logger.info(
        "Service=%s | Environment=%s | Deployment=%s",
        os.getenv("RAILWAY_SERVICE_NAME", "unknown"),
        os.getenv("RAILWAY_ENVIRONMENT_NAME", "unknown"),
        os.getenv("RAILWAY_DEPLOYMENT_ID", "unknown"),
    )

    if not token:
        logger.error("BOT_TOKEN environment variable is missing.")
        raise RuntimeError(
            "BOT_TOKEN is missing. Add it to the active Railway service/environment."
        )

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    logger.info("Bot starting with Telegram long polling.")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
