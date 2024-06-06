import logging

import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters)

from variables import coingecko_api_key, telegram_api_key

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    welcome_message = "I'm a bot, please talk to me!"

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=welcome_message
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text
    )


async def get_rate(update: Update, context: ContextTypes.DEFAULT_TYPE):

    headers = {"accept": "application/json"}
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum&vs_currencies=usd&x_cg_demo_api_key={coingecko_api_key}"
    response = requests.get(url, headers=headers)
    message = ""
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data["bitcoin"]["usd"]
        ethereum_price = data["ethereum"]["usd"]
        message = f"""
BTC/USD Conversion Rate: $ {bitcoin_price}
ETC/USD Conversion Rate: $ {ethereum_price}
        """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


if __name__ == "__main__":
    application = ApplicationBuilder().token(telegram_api_key).build()
    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    get_rate_handler = CommandHandler("get_rate", get_rate)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(get_rate_handler)
    application.run_polling()
