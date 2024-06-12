import requests

from utils.variables import coingecko_api_key


def get_crypto_prices(coins,currencies=["usd"]):
    headers = {"accept": "application/json"}
    coin_ids = "%2C".join(coins)
    currency_ids = "%2C".join(currencies)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_ids}&vs_currencies={currency_ids}&x_cg_demo_api_key={coingecko_api_key}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        prices = {}
        for coin in coins:
            if coin in data:
                prices[coin] = {currency: data[coin][currency] for currency in currencies if currency in data[coin]}
        return prices
    else:
        return None
