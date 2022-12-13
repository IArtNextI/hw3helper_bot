import telebot.async_telebot
import os
import asyncio

bot = telebot.async_telebot.AsyncTeleBot(os.environ["TOKEN"])

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, "Hello!")

@bot.message_handler(commands=['getid'])
async def send_welcome(message):
    await bot.reply_to(message, message.from_user.id)

asyncio.run(bot.polling())
