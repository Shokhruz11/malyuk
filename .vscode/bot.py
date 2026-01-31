# -*- coding: utf-8 -*-
"""
Yangi Super Talaba bot (minimal versiya)

Hozircha:
- /start va /help ishlaydi
- Menyuda 4 ta tugma: Slayd, Referat, Kurs ishi, Yordam
- Hech qanday OpenAI, to'lov, fayl yaratish yo'q (ularni keyin qo'shamiz)
"""

import os
import telebot
from telebot import types

# BOT_TOKEN ni Railway VARIABLES dan olamiz
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

if not BOT_TOKEN:
    print("⚠️ OG'OHLANTIRISH: BOT_TOKEN o'rnatilmagan! Locally test qilish uchun terminalda BOT_TOKEN ni export qiling.")

bot = telebot.TeleBot(BOT_TOKEN)

def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📝 Slayd", "📄 Referat")
    kb.row("📚 Kurs ishi", "❓ Yordam")
    return kb

@bot.message_handler(commands=["start"])
def cmd_start(message):
    text = (
        "Assalomu alaykum!\n\n"
        "Bu YANGI test bot.\n"
        "Hozircha faqat menyu va oddiy javoblar ishlaydi.\n\n"
        "Keyin slayd, referat, kurs ishi, to'lov va boshqa funksiyalarni qo'shamiz."
    )
    bot.send_message(message.chat.id, text, reply_markup=main_menu())

@bot.message_handler(commands=["help"])
def cmd_help(message):
    bot.send_message(message.chat.id, "Savollar bo'lsa, shu yerda yozing.", reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "📝 Slayd")
def handle_slayd(message):
    bot.send_message(message.chat.id, "Slayd xizmatini keyin qo'shamiz. Bot hozir test rejimida 😊")

@bot.message_handler(func=lambda m: m.text == "📄 Referat")
def handle_referat(message):
    bot.send_message(message.chat.id, "Referat/mustaqil ish xizmatini keyin qo'shamiz.")

@bot.message_handler(func=lambda m: m.text == "📚 Kurs ishi")
def handle_kurs(message):
    bot.send_message(message.chat.id, "Kurs ishi xizmatini ham keyin qo'shamiz.")

@bot.message_handler(func=lambda m: m.text == "❓ Yordam")
def handle_help_btn(message):
    bot.send_message(message.chat.id, "Bot ishlayapti. Hozircha test versiya.", reply_markup=main_menu())

@bot.message_handler(func=lambda m: True, content_types=["text"])
def fallback(message):
    bot.send_message(message.chat.id, "Menyudagi tugmalardan birini tanlang.", reply_markup=main_menu())

if __name__ == "__main__":
    print("Yangi test bot ishga tushdi...")
    bot.infinity_polling(skip_pending=True)
