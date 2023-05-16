import telebot
from telebot import types
import json
import requests
import os

with open('PATH_TO_TOKEN_FILE') as file:
    token = file.read()

bot = telebot.TeleBot(token)

res = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/')
data = json.loads(res.text)
print(data)
usd = data[0]
usd = usd["Rate"]
eur = data[1]
eur = eur["Rate"]
rub = data[2]
rub = rub["Rate"]
date = data[0]
date = date["Date"]

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('USD 🇺🇸 / SUM 🇺🇿')
    item2 = types.KeyboardButton('EUR 🇪🇺 / SUM 🇺🇿')
    item3 = types.KeyboardButton('RUB 🇷🇺 / SUM 🇺🇿')
    info = types.KeyboardButton('Инфо')
    markup.add(item1, item2, item3, info)
    bot.send_message(message.chat.id, (f'Привет! 👋\n\n🤖 С помощью этого бота можно следить за курсом иностранных валют в соотношении к узбекского сума в режиме реального времени\n\n🔍 Источник: Центральный банк Республики Узбекистан\n\n📆 Последнее обновление курса валют:  {date}\n\n🔽 Выберите необходимую валюту, чтобы посмотреть курс:').format(message.from_user), reply_markup = markup)
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Инфо':
            bot.send_message(message.chat.id, 'ssss')
        elif message.text == 'USD 🇺🇸 / SUM 🇺🇿':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('EUR 🇪🇺 / SUM 🇺🇿')
            item2 = types.KeyboardButton('RUB 🇷🇺 / SUM 🇺🇿')
            back = types.KeyboardButton('Назад ◀')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, f'📈 Курс доллара в соотношении к узбекскому суму:\n\n1 🇺🇸 = {usd} 🇺🇿' , reply_markup=markup)
        elif message.text == 'EUR 🇪🇺 / SUM 🇺🇿':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('USD 🇺🇸 / SUM 🇺🇿')
            item2 = types.KeyboardButton('RUB 🇷🇺 / SUM 🇺🇿')
            back = types.KeyboardButton('Назад ◀')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, f'📈 Курс евро в соотношении к узбекскому суму:\n\n1 🇪🇺 = {eur} 🇺🇿' , reply_markup=markup)
        elif message.text == 'RUB 🇷🇺 / SUM 🇺🇿':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('USD 🇺🇸 / SUM 🇺🇿')
            item2 = types.KeyboardButton('EUR 🇪🇺 / SUM 🇺🇿')
            back = types.KeyboardButton('Назад ◀')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, f'📈 Курс рубля в соотношении к узбекскому суму:\n\n1 🇷🇺 = {rub} 🇺🇿' , reply_markup=markup)
        elif message.text == 'Назад ◀':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('USD 🇺🇸 / SUM 🇺🇿')
            item2 = types.KeyboardButton('EUR 🇪🇺 / SUM 🇺🇿')
            item3 = types.KeyboardButton('RUB 🇷🇺 / SUM 🇺🇿')
            info = types.KeyboardButton('Инфо')
            markup.add(item1, item2, item3, info)
            bot.send_message(message.chat.id, (f'Привет! 👋\n\n🤖 С помощью этого бота можно следить за курсом иностранных валют в соотношении к узбекского сума в режиме реального времени\n\n🔍 Источник: Центральный банк Республики Узбекистан\n\n📆 Последнее обновление курса валют:  {date}\n\n🔽 Выберите необходимую валюту, чтобы посмотреть курс:').format(message.from_user), reply_markup = markup)
bot.infinity_polling()
