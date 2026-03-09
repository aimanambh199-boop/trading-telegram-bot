from indicators import rsi, ema

def candle_pattern(open_prices, close_prices):

    if close_prices[-1] > open_prices[-1] and close_prices[-2] < open_prices[-2]:
        return "Bullish Engulfing"

    if close_prices[-1] < open_prices[-1] and close_prices[-2] > open_prices[-2]:
        return "Bearish Engulfing"

    return "Normal"


def generate_signal(closes, opens):

    rsi_value = rsi(closes)
    ema_value = ema(closes)

    pattern = candle_pattern(opens, closes)

    price = closes[-1]

    if rsi_value < 30 and price > ema_value:

        signal = "BUY 📈"
        confidence = 88

    elif rsi_value > 70 and price < ema_value:

        signal = "SELL 📉"
        confidence = 88

    else:

        signal = "NO TRADE"
        confidence = 50

    return signal, confidence, rsi_value, pattern