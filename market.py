import requests

API_KEY = "98521af3ba4d4620985262aaef2caf7b"

def get_prices(pair):

    url = f"https://api.twelvedata.com/time_series?symbol={pair}&interval=1min&outputsize=50&apikey={API_KEY}"

    r = requests.get(url).json()

    closes = []
    opens = []

    if "values" in r:
        for candle in r["values"]:
            closes.append(float(candle["close"]))
            opens.append(float(candle["open"]))

        closes.reverse()
        opens.reverse()

    return closes, opens

