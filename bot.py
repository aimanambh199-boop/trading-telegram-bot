import signal
from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_TOKEN, CHANNEL_ID, PAIRS
from market import get_prices
from indicators import calculate_indicators, candle_pattern
from strategy import generate_signal, support_resistance

async def start(update, context):
    await update.message.reply_text(
        "🚀 PRO Trading Bot Online\n\nScanning market every 60 seconds."
    )

async def scanner(context):
    bot = context.bot
    for pair in PAIRS:
        closes, opens = get_prices(pair)
        if len(closes) < 20:
            continue
        price = closes[-1]
        rsi, ema = calculate_indicators(closes)
        pattern = candle_pattern(closes, opens)
        support, resistance = support_resistance(closes)
        signal, confidence = generate_signal(
            price, rsi, ema, pattern, support, resistance
        )
        if signal:
            message = f"""
📊 PRO AUTO SIGNAL
Pair: {pair}
Signal: {signal}
RSI: {round(rsi,2)}
EMA: {round(ema,5)}
Pattern: {pattern}
Confidence: {confidence}%
"""
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text=message
            )

def main():
    print("🚀 PRO Trading Bot Running...")
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    job_queue = app.job_queue
    job_queue.run_repeating(scanner, interval=60, first=10)
    
    def shutdown(sig, frame):
        print("Stopping bot safely...")
        app.stop()
    
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)
    
    app.run_polling()

if __name__ == "__main__":
    main()

