import os
import random
import time
from telegram import Bot
from datetime import datetime

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

def send_signal():
    entry = round(random.uniform(2300, 2400), 2)
    tp1 = round(entry + random.uniform(2, 5), 2)
    tp2 = round(tp1 + random.uniform(2, 5), 2)
    sl = round(entry - random.uniform(5, 10), 2)

    message = f"""📊 *Semnal XAUUSD* (M15)
🟢 BUY @ {entry}
🎯 TP1: {tp1}
🎯 TP2: {tp2}
❌ SL: {sl}
⏰ {datetime.now().strftime('%H:%M %d/%m')}
#gold #forex #xauusd"""

    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

def send_motivational():
    messages = [
        "💎 Nu renunța! Fiecare SL te aduce mai aproape de un TP mare!",
        "🔥 Pierderile sunt lecții. Continuă să înveți și să câștigi!",
        "📈 Încrederea în sistemul tău aduce rezultate.",
        "🚀 Fii disciplinat, fii constant, fii PROFITABIL!"
    ]
    bot.send_message(chat_id=CHAT_ID, text=random.choice(messages))

# Program loop
if __name__ == "__main__":
    while True:
        send_signal()
        time.sleep(3600)  # o dată pe oră
        send_motivational()
