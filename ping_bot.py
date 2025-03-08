import requests
import os

# Replace with your bot's URL
BOT_URL = os.getenv("BOT_URL", "https://your-bot.onrender.com")

def ping_bot():
    try:
        response = requests.get(BOT_URL)
        if response.status_code == 200:
            print(f"Successfully pinged {BOT_URL}")
        else:
            print(f"Failed to ping {BOT_URL}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error pinging {BOT_URL}: {e}")

if __name__ == "__main__":
    ping_bot()  # Run the script once