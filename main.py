import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
telegram_api_key = os.getenv("TELEGRAM_BOT_KEY")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    welcome_message = "I'm a bot, please talk to me!"

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=welcome_message
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(telegram_api_key).build()
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)
    application.run_polling()
