import logging

from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)

from utils.variables import telegram_api_key
from bot.handlers import start, echo, get_rate 
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def main():
    application = ApplicationBuilder().token(telegram_api_key).build()

    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    get_rate_handler = CommandHandler("get_rate", get_rate)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(get_rate_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
