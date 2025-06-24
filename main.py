import os
import asyncio
import random
from datetime import datetime
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

async def send_signal():
    entry = round(random.uniform(2300, 2400), 2)
    tp1 = round(entry + random.uniform(2, 5), 2)
    tp2 = round(tp1 + random.uniform(2, 5), 2)
    sl = round(entry - random.uniform(5, 10), 2)

    message = f"""📊 *Semnal XAUUSD* (M15)
🟢 BUY @ {entry}
🎯 TP1: {tp1}
🎯 TP2: {tp2}
❌ SL: {sl}
🕰️ {datetime.now().strftime('%H:%M %d/%m')}
#gold #forex #xauusd"""

    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

async def send_motivational():
    messages = [
        "💎 Nu renunța! Fiecare SL te aduce mai aproape de un TP mare!",
        "🔥 Pierderile sunt lecții. Continuă să înveți și să câștigi!",
        "📈 Încrederea în sistemul tău aduce rezultate.",
        "🚀 Fii disciplinat, fii constant, fii PROFITABIL!"
    ]
    await bot.send_message(chat_id=CHAT_ID, text=random.choice(messages))

async def main_loop():
    while True:
        await send_signal()
        await send_motivational()
        await asyncio.sleep(3600)  # o dată pe oră

if __name__ == "__main__":
    asyncio.run(main_loop())
