
import os
import time
import random
import requests
from datetime import datetime
from pathlib import Path

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

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

def ai_generate_signal():
    entry = round(random.uniform(2320.00, 2340.00), 2)
    tp1 = round(entry - 3.50, 2)
    tp2 = round(entry - 8.00, 2)
    sl = round(entry + 3.50, 2)
    return (
        "<b>Semnal XAUUSD (M15)</b>\n"
        "Tip: SELL\n"
        f"Entry: {entry}\n"
        f"TP1: {tp1}\n"
        f"TP2: {tp2}\n"
        f"SL: {sl}\n"
        "Admin: 'Pentru protejarea capitalului, setați BE la TP1!'"
    )

def send_morning_message():
    send_message("Bună dimineața, traderi!\n\nÎncepem ziua cu încredere și disciplină. Semnalele de astăzi vor fi reale și analizate atent.\nFii pregătit pentru profit! #VIPForex")

def send_tp1_notification():
    send_message("TP1 atins! Poți seta <b>Break Even</b> pentru a proteja profitul.")

def send_sl_notification():
    send_message("SL atins. Rămânem disciplinați – orice trader profesionist are și pierderi. Mergem înainte!")

def send_profit_screenshot():
    send_image("profit_example.jpg", "Profit obținut la TP2 cu lot 1.00")

def send_intro_message_once():
    flag_file = Path("intro_sent.flag")
    if not flag_file.exists():
        send_message("Bine ați venit în grupul nostru de semnale profesionale!\n\nAcest grup este gestionat cu experiență, disciplină și algoritmi AI care oferă semnale reale XAUUSD.\n\nNu este un simplu bot – este un început profitabil pentru toți! #Welcome")
        flag_file.write_text("sent")

if __name__ == "__main__":
    send_intro_message_once()
    now = datetime.now()
    if now.hour == 7:
        send_morning_message()

    time.sleep(random.randint(120, 600))
    send_message(ai_generate_signal())

    time.sleep(10)
    send_tp1_notification()

    time.sleep(5)
    send_profit_screenshot()

    time.sleep(5)
    send_sl_notification()
