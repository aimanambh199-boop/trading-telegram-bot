import signal
from telegram.ext import ApplicationBuilder, CommandHandler

def main():
    print("🚀 PRO Trading Bot Running...")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Job Queue (auto scanner every 60 sec)
    job_queue = app.job_queue
    if job_queue:
        job_queue.run_repeating(scanner, interval=60, first=10)
        print("✅ Scanner started (60s interval)")
    else:
        print("❌ JobQueue not available. Check requirements.")

    # Graceful shutdown (important for cloud servers)
    def signal_handler(sig, frame):
        print("⚠️ Shutting down bot...")
        app.stop()

    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    app.run_polling()

if __name__ == "__main__":
    main()main()

