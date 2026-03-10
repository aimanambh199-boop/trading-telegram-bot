import signal
from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_TOKEN

async def start(update, context):
    await update.message.reply_text(
        "🚀 PRO Trading Bot Online\n\nScanning market every 60 seconds."
    )

def main():
    print("🚀 PRO Trading Bot Running...")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # graceful shutdown
    def shutdown(sig, frame):
        print("Stopping bot safely...")
        app.stop()

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    app.run_polling()

if __name__ == "__main__":
    main()
