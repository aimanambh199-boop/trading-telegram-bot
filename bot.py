import asyncio

async def auto_signals(context):

    pair = "EURUSD"
    timeframe = "1min"

    closes, opens = get_market_data(pair, timeframe)

    signal, confidence, rsi_value, pattern = generate_signal(closes, opens)

    if confidence > 80:

        message = f"""
📊 AUTO SIGNAL

Pair: {pair}
Timeframe: {timeframe}

Signal: {signal}

RSI: {round(rsi_value,2)}
Confidence: {confidence}%
"""

        await context.bot.send_message(
            chat_id="@your_channel",
            text=message
        )
