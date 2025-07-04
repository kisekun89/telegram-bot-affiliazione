import os
import time
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CANALI = os.getenv("CANALI", "").split(",")
FREQUENZA_MINUTI = int(os.getenv("FREQUENZA_MINUTI", "60").strip())
TIPO_LINK_SVAPO = os.getenv("TIPO_LINK_SVAPO", "svapostore")

bot = telebot.TeleBot(BOT_TOKEN)

def get_offerta_fake(canale):
    if "svapo" in canale:
        return f"🔥 Offerta SvapoStore:\n👉 Aroma premium a 2,99€!\n🔗 https://www.svapostore.net/?tracking=test"
    else:
        return f"🔥 Offerta Amazon:\n👉 Powerbank 20000mAh a 14,99€!\n✅ Spedito da Amazon\n🔗 https://www.amazon.it/dp/B08XMBLKR2?tag=affaritech21-21"

def pubblica_offerte():
    for canale in CANALI:
        try:
            testo = get_offerta_fake(canale)
            bot.send_message(canale.strip(), testo)
            print(f"✅ Inviato su {canale}")
        except Exception as e:
            print(f"❌ Errore su {canale}: {e}")

while True:
    pubblica_offerte()
    time.sleep(FREQUENZA_MINUTI * 60)
        except Exception as e:
            print(f"❌ Errore su {canale}: {e}")

while True:
    pubblica_offerte()
    time.sleep(FREQUENZA_MINUTI * 60)
