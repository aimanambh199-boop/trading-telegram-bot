import requests

def get_prices(pair):

    url = f"https://api.binance.com/api/v3/klines?symbol={pair}T&interval=1m&limit=50"

    try:
        response = requests.get(url)
        data = response.json()

        closes = []

        for candle in data:
            closes.append(float(candle[4]))

        return closes

    except:
        return None


