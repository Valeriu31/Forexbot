import os
import time
import random
import requests
from datetime import datetime
from forex_filter import is_market_stable

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

def generate_signal():
    entry = round(random.uniform(2320, 2360), 2)
    tp1 = round(entry + random.uniform(2, 4), 2)
    tp2 = round(tp1 + random.uniform(2, 4), 2)
    sl = round(entry - random.uniform(5, 8), 2)
    return entry, tp1, tp2, sl

def send_morning_message():
    send_message("🌞 Bună dimineața, traderi! 💎 Începem ziua cu încredere și disciplină.")

def send_signal():
    if not is_market_stable():
        return
    entry, tp1, tp2, sl = generate_signal()
    signal = "<b>Semnal XAUUSD (M15)</b>

🟢 BUY @ {}
🎯 TP1: {}
🎯 TP2: {}
❌ SL: {}
⏰ {}

#gold #forex #xauusd".format(
        entry, tp1, tp2, sl, datetime.now().strftime('%H:%M %d/%m'))
    send_message(signal)

def send_tp1_notification():
    send_message("✅ TP1 atins! Poți seta <b>Break Even</b> pentru a proteja profitul. 💼")

def send_sl_notification():
    send_message("❌ SL atins. Rămânem disciplinați – orice trader profesionist are și pierderi. Mergem înainte! 🔥")

def send_profit_screenshot():
    send_image("profit_example.jpg", "📸 Profit obținut la TP2 cu lot 1.00")

if __name__ == "__main__":
    send_message("🔄 Test manual – botul funcționează și trimite mesaje!")
    send_morning_message()
    time.sleep(random.randint(5, 15))
    send_signal()
    time.sleep(random.randint(5, 15))
    send_tp1_notification()
    time.sleep(random.randint(5, 15))
    send_profit_screenshot()
    time.sleep(random.randint(5, 15))
    send_sl_notification()


