"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem +
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem 
import datetime
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


planets_dict = {
        'Mars': ephem.Mars, 'Марс' : ephem.Mars,
                   'Venus': ephem.Venus, 'Венера' : ephem.Venus,
                   'Saturn': ephem.Saturn, 'Сатурн' : ephem.Saturn,
                   'Jupiter': ephem.Jupiter, 'Юпитер' : ephem.Jupiter,
               'Neptune': ephem.Neptune, 'Нептун' : ephem.Neptune,
               'Uranus': ephem.Uranus, 'Уран' : ephem.Uranus,
               'Mercury': ephem.Mercury, 'Меркурий' : ephem.Mercury
               }

def greet_user(update, context):
    text = 'Вызван /start'
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet(update, context):
    text = 'Вызван /planet'
    update.message.reply_text('Введите название планеты')

def call_planet(update, context):
    day_now = datetime.date.today()
    user_text = update.message.text
    user_text = user_text.capitalize()
    if user_text in planets_dict:
        planet = planets_dict[user_text]
        constellation_full = ephem.constellation(planet(day_now))
        update.message.reply_text(constellation_full[1])
    else:
        update.message.reply_text('Такой планеты я не знаю')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, call_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
