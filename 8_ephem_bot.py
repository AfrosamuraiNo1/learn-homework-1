"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from pydoc import plain
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from datetime import datetime

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)
    # Командуем боту начать ходить в Telegram за сообщениями
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_user))
#    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(MessageHandler(Filters.text, planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def planet_user(update, context):
    print('Вызван /planet')
    update.message.reply_text('Введи планету по англиский. Напимер Mars')

def planet(update, context):
    planet = update.message.text
    dt_now = datetime.now()
    time_now = dt_now.strftime('%Y/%m/%d')
    name_planet = getattr(ephem,planet[0:].capitalize())(time_now)
    constellation = ephem.constellation(name_planet)
    update.message.reply_text(f'В созвездии сегодня находится планета {constellation}')
    
if __name__ == "__main__":
    main()