import os

import requests
from dotenv import load_dotenv

load_dotenv()

CoinGeckoAPIKey = os.getenv("COINGECKO_API_KEY")


url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum&vs_currencies=usd&x_cg_demo_api_key={CoinGeckoAPIKey}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
