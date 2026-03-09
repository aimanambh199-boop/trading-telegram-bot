import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator


def calculate_indicators(closes):

    df = pd.DataFrame()
    df["close"] = closes

    rsi = RSIIndicator(df["close"], window=14).rsi().iloc[-1]
    ema = EMAIndicator(df["close"], window=20).ema_indicator().iloc[-1]

    return rsi, ema


def candle_pattern(closes, opens):

    if len(closes) < 2:
        return None

    last_close = closes[-1]
    last_open = opens[-1]

    prev_close = closes[-2]
    prev_open = opens[-2]

    if prev_close < prev_open and last_close > last_open and last_close > prev_open:
        return "BULLISH"

    if prev_close > prev_open and last_close < last_open and last_close < prev_open:
        return "BEARISH"

    return None

