# /usr/bin/python3

import telebot.async_telebot
import os
import asyncio
import requests

bot = telebot.async_telebot.AsyncTeleBot(os.environ["TOKEN"])
storage_node = os.environ["STORAGE_NODE"]

@bot.message_handler(commands=['help', 'start'])
async def start(message):
    await bot.reply_to(message, "/help - Displays this message\n\
/getid - Displays user's id\n\
/chatid - Displays chat id\n\
/calc - Allows to evaluate various mathematical expression\n\
/set - Allows to store data\n\
/get - Allows to retrieve stored data\n")

@bot.message_handler(commands=['getid'])
async def getid(message):
    await bot.reply_to(message, message.from_user.id)

@bot.message_handler(commands=['chatid'])
async def chatid(message):
    await bot.reply_to(message, message.from_user.id)

@bot.message_handler(commands=['calc'])
async def calc(message):
    expression = message.text[6:].strip()
    for x in expression:
        if x not in "0123456789 *+-/^&|()" and not x.isalpha():
            await bot.reply_to(message, "Found forbidden symbol '" + x + "'")
            return 
    try:
        result = eval(expression)
        await bot.reply_to(message, str(result))
    except:
        await bot.reply_to(message, "Failed to evaluate the expression")

@bot.message_handler(commands=['set'])
async def set_(message):
    expression = message.text[5:].strip()
    name, value = expression.split()
    for x in name:
        if not x.isalpha():
            await bot.reply_to(message, "Found forbidden symbol '" + x + "' in name")
            return
    response = requests.post(storage_node + "/api/" + str(message.from_user.id) + "/" + name, data=value.encode())
    await bot.reply_to(message, ("Stored" if response.text == "OK" else "Failed to store"))

@bot.message_handler(commands=['get'])
async def set_(message):
    name = message.text[5:].strip()
    for x in name:
        if not x.isalpha():
            await bot.reply_to(message, "Found forbidden symbol '" + x + "' in name")
            return
    response = requests.get(storage_node + "/api/" + str(message.from_user.id) + "/" + name)
    await bot.reply_to(message, "The recovered value is '" + response.text + "'")

asyncio.run(bot.polling())
