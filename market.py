import requests
from config import TWELVE_DATA_API_KEY

def get_market_data(pair, timeframe):

    if pair == "EURUSD":
        pair = "EUR/USD"

    if pair == "GBPUSD":
        pair = "GBP/USD"

    url = f"https://api.twelvedata.com/time_series?symbol={pair}&interval={timeframe}&apikey={TWELVE_DATA_API_KEY}&outputsize=100"

    response = requests.get(url)
    data = response.json()

    candles = data["values"]

    closes = [float(c["close"]) for c in candles]
    opens = [float(c["open"]) for c in candles]

    return closes, opens