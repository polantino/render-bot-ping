import os
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Initialize Flask app
app = Flask(__name__)

# Get the bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")  # Replace with env variable

# Initialize the bot application
bot_app = Application.builder().token(BOT_TOKEN).build()

# Handle the /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "🎉 Welcome to the Team Earnings Program! 🎉\n\n"
        "Are you ready to turn a small investment into life-changing returns? With just 2,700 Naira, you can join a proven system that helps you grow your money exponentially while building a network of like-minded earners.\n\n"
        "👇 Get Started Now or explore more below:\n"
        "[👉 Join Now]\n"
        "[📚 How It Works]\n"
        "[📝 Steps to Follow]\n"
        "[❓ FAQs]\n"
        "[📞 Contact Support]"
    )

# Handle non-command messages
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(f"You said: {update.message.text}")

# Add handlers to the bot application
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Webhook route (SYNC version)
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # Log the incoming request data
        update_data = request.get_json()
        print("Incoming request data:", update_data)
        
        # Parse the incoming update
        update = Update.de_json(update_data, bot_app.bot)
        print("Parsed update:", update)
        
        # Process the update asynchronously
        asyncio.run(bot_app.process_update(update))
        return "OK", 200
    except Exception as e:
        # Log any errors
        print("Error processing update:", e)
        return {"info": "Invalid request!"}, 400

# Health check route
@app.route("/", methods=["GET"])
def health_check():
    return "Bot is running!", 200

# Run the Flask app
if __name__ == "__main__":
    # Use Render's default port
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
