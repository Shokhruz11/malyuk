# -*- coding: utf-8 -*-
"""
Yangi Super Talaba bot (minimal versiya)
"""

import os
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

if not BOT_TOKEN:
    print("⚠️ BOT_TOKEN topilmadi! Railway'ga qo'yishni unutmang.")

bot = telebot.TeleBot(BOT_TOKEN)

def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📝 Slayd", "📄 Referat")
    kb.row("📚 Kurs ishi", "❓ Yordam")
    return kb

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Assalomu alaykum!\n\nBu YANGI test bot. Hozircha menyu ishlaydi.\nKeyin AI va to'lov tizimi qo'shamiz.",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda m: m.text == "📝 Slayd")
def slayd(message):
    bot.send_message(message.chat.id, "Slayd xizmati keyin qo'shiladi 😊")

@bot.message_handler(func=lambda m: m.text == "📄 Referat")
def referat(message):
    bot.send_message(message.chat.id, "Referat xizmati keyin qo'shiladi.")

@bot.message_handler(func=lambda m: m.text == "📚 Kurs ishi")
def kurs(message):
    bot.send_message(message.chat.id, "Kurs ishi xizmati keyin qo'shiladi.")

@bot.message_handler(func=lambda m: m.text == "❓ Yordam")
def yordam(message):
    bot.send_message(message.chat.id, "Savolingizni yozing.")

@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(message.chat.id, "Menyudan tugma tanlang.", reply_markup=main_menu())

if __name__ == "__main__":
    print("Bot ishga tushdi...")
    bot.infinity_polling(skip_pending=True)

