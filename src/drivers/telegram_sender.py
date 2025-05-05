import requests
import os

def send_telegram_message(message):
  token = os.getenv('BOT_TOKEN')
  chat_id = os.getenv('TELEGRAM_CHAT_ID')

  url = f"https://api.telegram.org/bot{token}/sendMessage"
  payload = {
    "chat_id": chat_id,
    "text": message
  }

  requests.post(url, data=payload)
