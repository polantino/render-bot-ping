import os
import time
from flask import Flask, request
import telebot

# Initialize Flask app
app = Flask(__name__)

# Get the bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN", "8194086003:AAGPFbfx0aXcDYqOBqaxrJK5mTwSBmB3fUA")

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Track bot initialization time
bot_start_time = time.time()

# Handle the /start command
@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Check if the bot is still initializing (cold start)
    if time.time() - bot_start_time < 10:  # Adjust the threshold as needed
        bot.reply_to(message, "⏳ Hang on, the bot is processing your message...")
        time.sleep(5)  # Simulate initialization delay
    bot.reply_to(message, "🎉 Welcome to the Team Earnings Program! 🎉\n\n"
                          "Are you ready to turn a small investment into life-changing returns? With just 2,700 Naira, you can join a proven system that helps you grow your money exponentially while building a network of like-minded earners.\n\n"
                          "👇 Get Started Now or explore more below:\n"
                          "[👉 Join Now]\n"
                          "[📚 How It Works]\n"
                          "[📝 Steps to Follow]\n"
                          "[❓ FAQs]\n"
                          "[📞 Contact Support]")

# Handle non-command messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Check if the bot is still initializing (cold start)
    if time.time() - bot_start_time < 10:  # Adjust the threshold as needed
        bot.reply_to(message, "⏳ Hang on, the bot is processing your message...")
        time.sleep(5)  # Simulate initialization delay
    bot.reply_to(message, f"You said: {message.text}")

# Webhook route
@app.route("/", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200

# Health check route
@app.route("/", methods=["GET"])
def health_check():
    return "Bot is running!", 200

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))