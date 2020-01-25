# TGbot

import pyowm
import telebot

owm = pyowm.OWM('5edfb276a6e154e914b96ac9bf1cf2a0', language="ru")
bot = telebot.TeleBot("TOKEN")

# обычеая отправка сообщений -->

# bot.send_mesage(message.chat.id, message.text)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! чтобы узнать погоду напиши название города")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Чтобы узнать погоду напиши название города/страны")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас " + str(temp) + "\n\n"

    if temp < 10:
        answer += "На улице очень холодно. Желательно одеться потеплее."
    elif temp < 20:
        answer += "На улице достаточно холодно. Незабудь куртку."
    else:
        answer += "Погода заебумба, хоть в трусах гуляй."

    bot.send_message(message.chat.id, answer)


# @bot.message_handler(content_types=['text'])
# def handle_message(message):
    # bot.reply_to(message, "----")


bot.polling(none_stop=True)
