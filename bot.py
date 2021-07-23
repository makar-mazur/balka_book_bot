#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
#Coment for Max
#Test probelm conncet
#Chenge

"""
Simple Bot to reply to Telegram messages.
kokoaaaaaaaaa
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
import urllib.request
link = 'https://makar-mazur.github.io/balka_book_bot/data/'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
def read_content_from_url(file):
    f = urllib.request.urlopen(file)
    text = f.read().decode(encoding = 'utf-8')
    f.close()
    return text

def read_content_from_file(file):
    f = open(file, 'r')
    text = f.read()
    f.close()
    return text

def start(update, context):
    """Send a message when the command /start is issued."""
    kb = [[InlineKeyboardButton('Время работы интернет-магазина', callback_data = 'online_store_working_hours')],
          [InlineKeyboardButton('Отправка заказов', callback_data = 'sending_orders')],
          [InlineKeyboardButton('Уточнить статус моего заказа', callback_data = 'clarify_status_of_my_order')],
          [InlineKeyboardButton('Наличие или стоимость товара на сайте', callback_data = 'availability_or_cost_of_goods_on_site')],
          [InlineKeyboardButton('Подтвердить оплату заказа', callback_data = 'clarify_status_of_my_order')],]
    reply = InlineKeyboardMarkup(kb)
    update.message.reply_text('Hi! You can choose', reply_markup = reply )
    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def online_store_working_hours(update, context):
    link_file = link + 'online_store_working_hours.txt'
    content = read_content_from_file(link_file)
    up.callback_query.message.reply_text(content, reply_markup = reply)

def main():
  
    updater = Updater(config.TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CallbackQueryHandler(online_store_working_hours, pattern = 'online_store_working_hours'))
#    dp.add_handler(CallbackQueryHandler(sending_orders, pattern = 'sending_orders'))
#    dp.add_handler(CallbackQueryHandler(clarify_status_of_my_order, pattern = 'clarify_status_of_my_order'))
#    dp.add_handler(CallbackQueryHandler(availability_or_cost_of_goods_on_site, pattern = 'availability_or_cost_of_goods_on_site'))
#    dp.add_handler(CallbackQueryHandler(clarify_status_of_my_order, pattern = 'clarify_status_of_my_order'))
    
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()