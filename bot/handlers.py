from telegram import Update
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
    bitcoin_price, ethereum_price = get_crypto_prices()

    if bitcoin_price is not None and ethereum_price is not None:
        message = f"""
BTC/USD Conversion Rate: $ {bitcoin_price}
ETH/USD Conversion Rate: $ {ethereum_price}
        """
    else:
        message = "Failed to retrieve prices. Please try again later."

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
