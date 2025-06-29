
import os
import time
import requests
from datetime import datetime
from signal_generator import generate_signal

BOT_TOKEN = "7781849791:AAEHmv-ASP6elqBJ7SRisSyksuEyPvCgwGA"
CHAT_ID = "-1002891747269"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=payload)

def send_image(photo_path, caption=""):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    with open(photo_path, 'rb') as photo:
        payload = {"chat_id": CHAT_ID, "caption": caption, "parse_mode": "HTML"}
        files = {"photo": photo}
        requests.post(url, data=payload, files=files)

def send_morning_message():
    mesaj = (
        "🌄 Bună dimineața, traderi!\n"
        "🔔 Începem ziua cu încredere și disciplină.\n"
        "📊 Semnalele de azi vor fi reale, analizate de AI.\n"
        "💼 Fii pregătit pentru profit! #XAUUSD #M15"
    )
    send_message(mesaj)

def send_tp1_message():
    send_image("tp1_example.jpg", "📸 Profit TP1 atins!")
    time.sleep(2)
    send_message("✅ TP1 atins! Poți seta <b>Break Even</b> pentru a proteja profitul. 💼")

def send_sl_message():
    send_message("❌ SL atins. Rămânem disciplinați – urmează oportunități mai bune! 💪")

if __name__ == "__main__":
    sent_today = False
    while True:
        now = datetime.now()

        if now.hour == 6 and now.minute == 0:
            sent_today = False

        if not sent_today and now.hour == 7:
            send_morning_message()
            sent_today = True

        if now.weekday() < 5 and 6 <= now.hour <= 21:
            signal_data = generate_signal()
            send_message(signal_data['text'])
            print("✅ Semnal trimis:", signal_data['text'])
            time.sleep(signal_data['wait_tp1'])
            send_tp1_message()
            time.sleep(signal_data['wait_sl'])
            send_sl_message()

        time.sleep(60)
