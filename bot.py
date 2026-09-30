import os
import telebot

TOKEN = '8841651688:AAE0OXSnaNRblo8FV8B0zniDIxmcRePVWH0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا حارث! بوت تعقب الرسائل المحذوفة المعدلة يعمل بنجاح وبدون توقف.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

print("Bot is running...")
bot.infinity_polling()
