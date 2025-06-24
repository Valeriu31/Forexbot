
import requests
import random

API_KEY = "demo"
SYMBOL = "XAUUSD"

def get_live_price():
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=XAU&to_currency=USD&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    try:
        price = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        return round(price, 2)
    except (KeyError, ValueError):
        raise RuntimeError("❌ Nu s-a putut obține prețul XAUUSD din API.")

def generate_signal():
    last_price = get_live_price()
    direction = random.choice(["BUY", "SELL"])

    if direction == "BUY":
        entry = round(last_price + 0.5, 2)
        tp1 = round(entry + 3.0, 2)
        tp2 = round(entry + 6.0, 2)
        sl = round(entry - 3.5, 2)
    else:
        entry = round(last_price - 0.5, 2)
        tp1 = round(entry - 3.0, 2)
        tp2 = round(entry - 6.0, 2)
        sl = round(entry + 3.5, 2)

    signal_text = (
        f"📢 <b>Semnal XAUUSD (M15)</b>\n\n"
        f"🔹 Tip: {direction}\n"
        f"🔹 Entry: {entry}\n"
        f"🎯 TP1: {tp1}\n"
        f"🎯 TP2: {tp2}\n"
        f"🛑 SL: {sl}\n\n"
        f"💡 Admin: 'Setează Break-Even la TP1!'"
    )

    return {
        "text": signal_text,
        "wait_tp1": 1800,
        "wait_sl": 900
    }

