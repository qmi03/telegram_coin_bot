from telegram import Update, constants
from telegram.ext import ContextTypes

from bot.utils import get_crypto_prices


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
    coins = ["bitcoin", "ethereum"]
    prices = get_crypto_prices(coins)
    print(prices)
    if prices:
        message_lines = []
        for coin, coin_prices in prices.items():
            line = f"<b>{coin}</b> price in " + ", ".join(
                [f"<b>{currency.upper()}</b>: {price}" for currency, price in coin_prices.items()]
            )
            message_lines.append(line)
        message = "\n".join(message_lines)
    else:
        message = "Failed to retrieve prices. Please try again later."

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=constants.ParseMode.HTML)
