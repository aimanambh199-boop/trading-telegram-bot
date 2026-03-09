import numpy as np

# RSI Indicator
def rsi(prices, period=14):

    deltas = np.diff(prices)

    gain = np.maximum(deltas, 0)
    loss = np.abs(np.minimum(deltas, 0))

    avg_gain = np.mean(gain[:period])
    avg_loss = np.mean(loss[:period])

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss

    rsi_value = 100 - (100 / (1 + rs))

    return rsi_value


# EMA Indicator
def ema(prices, period=20):

    ema_value = prices[0]

    multiplier = 2 / (period + 1)

    for price in prices:

        ema_value = (price - ema_value) * multiplier + ema_value

    return ema_value