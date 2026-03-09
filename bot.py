from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN
from market import get_market_data
from strategy import generate_signal


# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("EURUSD", callback_data="pair_EURUSD"),
            InlineKeyboardButton("GBPUSD", callback_data="pair_GBPUSD")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📊 Select Trading Pair",
        reply_markup=reply_markup
    )


# BUTTON HANDLER
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # PAIR SELECT
    if "pair" in data:

        pair = data.split("_")[1]

        context.user_data["pair"] = pair

        keyboard = [
            [
                InlineKeyboardButton("1 Minute", callback_data="tf_1min"),
                InlineKeyboardButton("5 Minute", callback_data="tf_5min"),
                InlineKeyboardButton("15 Minute", callback_data="tf_15min")
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            f"Pair Selected: {pair}\n\nSelect Timeframe",
            reply_markup=reply_markup
        )

    # TIMEFRAME SELECT
    if "tf" in data:

        timeframe = data.split("_")[1]

        pair = context.user_data.get("pair")

        closes, opens = get_market_data(pair, timeframe)

        signal, confidence, rsi_value, pattern = generate_signal(closes, opens)

        message = f"""
📊 Trading Signal

Pair: {pair}
Timeframe: {timeframe}

Signal: {signal}

Pattern: {pattern}

RSI: {round(rsi_value,2)}
Confidence: {confidence}%

Entry: Next Candle
"""

        await query.edit_message_text(message)


def main():

    app = (
        ApplicationBuilder()
        .token(TELEGRAM_BOT_TOKEN)
        .connect_timeout(60)
        .read_timeout(60)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("🚀 PRO Trading Bot Running...")

    app.run_polling()


if __name__ == "__main__":
    main()