def support_resistance(closes):

    support = min(closes[-10:])
    resistance = max(closes[-10:])

    return support, resistance


def generate_signal(price, rsi, ema, pattern, support, resistance):

    if price > ema and rsi < 35 and pattern == "BULLISH" and price > support:
        return "BUY 📈", 92

    if price < ema and rsi > 65 and pattern == "BEARISH" and price < resistance:
        return "SELL 📉", 92

    return None, 0
