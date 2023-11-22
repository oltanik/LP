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

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

day = '22/11/2023'
text_dict = {
    'Mars': ephem.Mars(day), 'Марс': ephem.Mars(day),
             'Venus': ephem.Venus(day), 'Венера': ephem.Venus(day),
               'Saturn': ephem.Saturn(day), 'Сатурн': ephem.Saturn(day),
               'Jupiter': ephem.Jupiter(day), 'Юпитер' : ephem.Jupiter(day),
               'Neptune': ephem.Neptune(day), 'Нептун' : ephem.Neptune(day),
               'Uranus': ephem.Uranus(day), 'Уран' : ephem.Uranus(day),
               'Mercury': ephem.Mercury(day), 'Меркурий': ephem.Mercury(day)
               }

 
def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def call_planet(update, context):
    text = 'Вызван /planet'
    update.message.reply_text('Введите название планеты')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def name_planet(update, context):
     planet = update.message.text.split()[1]
     planet_pol = text_dict.get(planet)
     if planet_pol != None:
         constellation = ephem.constellation(text_dict[planet])
         update.message.reply_text(constellation[1])
     else:
         update.message.reply_text('Я не знаю такой планеты')
     

def main():
    mybot = Updater("6727725792:AAHHxeZVSIYvdxldrDfbMm5zTIyo8cydoEQ", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", call_planet)) 
    dp.add_handler(MessageHandler(Filters.text, name_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
  
    

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
