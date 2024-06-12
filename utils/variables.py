import os

from dotenv import load_dotenv

load_dotenv()
coingecko_api_key = os.getenv("COINGECKO_API_KEY")

telegram_api_key = os.getenv("TELEGRAM_BOT_KEY")

url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum&vs_currencies=usd&x_cg_demo_api_key={coingecko_api_key}"
