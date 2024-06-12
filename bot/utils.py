import requests

from utils.variables import coingecko_api_key


def get_crypto_prices():
    headers = {"accept": "application/json"}
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum&vs_currencies=usd&x_cg_demo_api_key={coingecko_api_key}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data["bitcoin"]["usd"]
        ethereum_price = data["ethereum"]["usd"]
        return bitcoin_price, ethereum_price
    else:
        return None, None
