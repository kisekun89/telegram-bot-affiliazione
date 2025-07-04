import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CANALI = os.getenv("CANALI", "").split(",")
TIPO_LINK_SVAPO = os.getenv("TIPO_LINK_SVAPO", "svapostore")

bot = telebot.TeleBot(BOT_TOKEN)

def get_offerta_fake(canale):
    if "svapo" in canale:
        return f"🔥 [TEST] Offerta SvapoStore:
👉 Aroma premium a 2,99€!
🔗 https://www.svapostore.net/?tracking=test"
    else:
        return f"🔥 [TEST] Offerta Amazon:
👉 Powerbank 20000mAh a 14,99€!
✅ Spedito da Amazon
🔗 https://www.amazon.it/dp/B08XMBLKR2?tag=affaritech21-21"

def pubblica_test():
    for canale in CANALI:
        try:
            testo = get_offerta_fake(canale)
            bot.send_message(canale.strip(), testo)
            print(f"✅ Test inviato su {canale}")
        except Exception as e:
            print(f"❌ Errore su {canale}: {e}")

pubblica_test()
