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
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
import urllib.request
link = 'https://ulkabo.github.io/bot-friday/data/'

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
    kb = [[InlineKeyboardButton('Кафедра КМАД', callback_data = 'kafedra')],
          [InlineKeyboardButton('Можливості для студентів', callback_data = 'mozhlivosti')],
          [InlineKeyboardButton('Умови вступу', callback_data = 'umovy')],]
    reply = InlineKeyboardMarkup(kb)
    update.message.reply_text('Hi! You can choose', reply_markup = reply )
    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def bro(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("I'm bro, you are bro, we are brothers ")



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def kafedra(update, context):
    """Send a message when the command /start is issued."""
    kb = [[InlineKeyboardButton('Викладачі', callback_data = 'vykladachi')],
          [InlineKeyboardButton('Принципи навчання на кафедрі', callback_data = 'printsipy')],
          [InlineKeyboardButton('Історія кафедри ', callback_data = 'istoria')],]
    reply = InlineKeyboardMarkup(kb)
    update.callback_query.message.reply_text('З чого почнемо?', reply_markup = reply )
    
def mozhlivosti(update, context):
    kb = [[InlineKeyboardButton("Проектне навчання", callback_data = 'proektne')],
          [InlineKeyboardButton("Дуальне навчання", callback_data = 'dualna')],
          [InlineKeyboardButton("Працевлаштування",callback_data = 'pracevlasht')],
          [InlineKeyboardButton("Практика",callback_data = 'praktica')]]
    reply = InlineKeyboardMarkup(kb)
    update.message.reply_text("У нас є багато цікавих можливостей для студентів:", reply_markup=reply)
    
def umovy(update, context):
    kb = [[InlineKeyboardButton('Конкурсні предмети ЗНО',callback_data = '')],
          [InlineKeyboardButton('Розрахунок конкурсного балу',callback_data = '')],
          [InlineKeyboardButton('Етапи вступної компанії',callback_data = '')],
          [InlineKeyboardButton('Корисні посилання',callback_data = '')],
          [InlineKeyboardButton('Кількість бюджетних та контрактних мість для вступників',callback_data = '')],]
    reply = InlineKeyboardMarkup(kb)
    update.callback_query.message.reply_text('Hi! you can choose', reply_markup = reply )
    
def mozhlivosti(update, context):
	  pass
def pridmeti_dlya_zno(update, context):
	  pass
def rozrahunok_konkursnogo_balu(update, context):
	  pass
def etapi_vstupnoi_kompanii(update, context):
	  pass
def korisni_posilanya(update, context):
    link_file = link + 'korisni_posilanya.txt'
    content = read_content_from_file(link_file)
    update.callback_query.message.reply_text(content, reply_markup = reply )
def mistcya_dlya_vstupnikiv(update, context):
    link_file = link + 'mistcya_dlya_vstupnikiv.txt'
    content = read_content_from_file(link_file)
    update.callback_query.message.reply_text(content, reply_markup = reply )
def vikladachi(update, context):
    link_file = link + 'vikladachi.txt'
    content = read_content_from_file(link_file)
    update.callback_query.message.reply_text(content, reply_markup = reply )
def vidmini_kafedri(update, context):
    pass
def istoriya(update, context):
    pass
def auditorii(update, context):
    pass
def vipusniki(update, context):
    pass
def main():
  
    updater = Updater("1600092846:AAHLA--iPlmFI8LMfp-U7PEL2NtmrGqUJJQ", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("bro", bro))
    dp.add_handler(CallbackQueryHandler(kafedra, pattern = 'kafedra'))
    dp.add_handler(CallbackQueryHandler(mozhlivosti, pattern = 'mozhlivosti'))
    dp.add_handler(CallbackQueryHandler(umovy, pattern = 'umovy'))
    dp.add_handler(CallbackQueryHandler(mozhlivosti , pattern = 'mozhlivosti'))
    dp.add_handler(CallbackQueryHandler(pridmeti_dlya_zno, pattern = 'pridmeti_dlya_zno'))
    dp.add_handler(CallbackQueryHandler(rozrahunok_konkursnogo_balu , pattern = 'rozrahunok_konkursnogo_balu'))
    dp.add_handler(CallbackQueryHandler( etapi_vstupnoi_kompanii, pattern = 'etapi_vstupnoi_kompanii'))
    dp.add_handler(CallbackQueryHandler(korisni_posilanya , pattern = 'korisni_posilanya'))
    dp.add_handler(CallbackQueryHandler(mistcya_dlya_vstupnikiv , pattern = 'mistcya_dlya_vstupnikiv'))
    
    dp.add_handler(CallbackQueryHandler(proektne, pattern = 'proektne'))
    dp.add_handler(CallbackQueryHandler(dualna, pattern = 'dualna'))
    dp.add_handler(CallbackQueryHandler(pracevlasht, pattern = 'pracevlasht'))
    dp.add_handler(CallbackQueryHandler(practica, pattern = 'practica'))
    
    dp.add_handler(CallbackQueryHandler(vikladachi, pattern = 'vikladachi'))
    dp.add_handler(CallbackQueryHandler(vidmini_kafedri, pattern = 'vidmini_kafedri'))
    dp.add_handler(CallbackQueryHandler(istoriya, pattern = 'istoriya'))
    dp.add_handler(CallbackQueryHandler(auditorii, pattern = 'auditorii'))
    dp.add_handler(CallbackQueryHandler(vipusniki, pattern = 'vipusniki'))
    
    dp.add_handler(CallbackQueryHandler(proektne, pattern = 'proektne'))
    dp.add_handler(CallbackQueryHandler(dualna, pattern = 'dualna'))
    dp.add_handler(CallbackQueryHandler(pracevlasht, pattern = 'pracevlasht'))
    dp.add_handler(CallbackQueryHandler(practica, pattern = 'practica'))

    
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

dskfjsdkjf
if __name__ == '__main__':
    main()
