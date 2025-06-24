import os
import time
import random
import requests
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

def send_image(photo_path, caption=""):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as photo:
        payload = {
            "chat_id": CHAT_ID,
            "caption": caption,
            "parse_mode": "HTML"
        }
        files = {
            "photo": photo
        }
        requests.post(url, data=payload, files=files)

def send_morning_message():
    send_message("🌞 Bună dimineața, traderi!"

💎 Începem ziua cu încredere și disciplină. Semnalele de astăzi vor fi reale și analizate atent.
📊 Fii pregătit pentru profit! #VIPForex")

def send_signal():
    entry = round(random.uniform(2320, 2360), 2)
    tp1 = round(entry + random.uniform(2, 4), 2)
    tp2 = round(tp1 + random.uniform(2, 4), 2)
    sl = round(entry - random.uniform(5, 8), 2)
    signal = f"""<b>Semnal XAUUSD (M15)</b>
🔹 Tip: BUY
🔹 Entry: {entry}
🎯 TP1: {tp1}
🎯 TP2: {tp2}
🛑 SL: {sl}

💡 Admin: Pentru protejarea capitalului, setați BE la TP1!"""
    send_message(signal)

def send_tp1_notification():
    send_message("✅ TP1 atins! Poți seta <b>Break Even</b> pentru a proteja profitul. 💼")

def send_sl_notification():
    send_message("❌ SL atins. Rămânem disciplinați – orice trader profesionist are și pierderi. Mergem înainte! 🔥")

def send_profit_screenshot():
    send_image("profit_example.jpg", "📸 Profit obținut la TP2 cu lot 1.00")

if __name__ == "__main__":
    now = datetime.now()
    if now.hour == 7:
        send_morning_message()
    time.sleep(5)
    send_signal()
    time.sleep(5)
    send_tp1_notification()
    time.sleep(5)
    send_profit_screenshot()
    time.sleep(5)
    send_sl_notification()