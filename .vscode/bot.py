import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

if not BOT_TOKEN:
    print("❌ BOT_TOKEN topilmadi! Railway Variables ga qo'yishni unutmang!")
    exit()

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Bot ishlayapti! 🎉")

bot.polling(none_stop=True)