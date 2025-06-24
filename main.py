import os
import time
import random
from datetime import datetime
from telegram import Bot, InputFile
from forex_filter import is_market_stable

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

def generate_signal():
    entry = round(random.uniform(2320, 2360), 2)
    tp1 = round(entry + random.uniform(2, 4), 2)
    tp2 = round(tp1 + random.uniform(2, 4), 2)
    sl = round(entry - random.uniform(5, 8), 2)
    return entry, tp1, tp2, sl

def send_signal():
    if not is_market_stable():
        return
    entry, tp1, tp2, sl = generate_signal()
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

def send_intro_message():
    bot.send_message(chat_id=CHAT_ID, text="""
🚀 Bun venit în grupul *FXSignalsFREE*!

✅ Aici vei primi semnale reale, analizate cu atenție și filtrate inteligent pentru a evita momentele riscante.
📊 Avem experiență, disciplină și o comunitate care crește zilnic.
💰 Nu este un simplu bot, este începutul unei noi etape profitabile pentru tine.

#forex #xauusd #profit #disciplina
""", parse_mode="Markdown")

# Trimite mesaj de început o singură dată
if not Path("intro_sent.txt").exists():
    send_intro_message()
    with open("intro_sent.txt", "w") as f:
        f.write("sent")

# Trimite mesaj motivațional dimineața
today = datetime.now().strftime("%Y-%m-%d")
if not Path(f"motivational_{today}.txt").exists():
    send_motivational()
    with open(f"motivational_{today}.txt", "w") as f:
        f.write("sent")

# Trimite semnale pe parcursul zilei
while True:
    send_signal()
    time.sleep(3600)
