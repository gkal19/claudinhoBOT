#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time
import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from emoji import emojize

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
	update.message.reply_text("Oi, eu sou o NEO!")
	update.message.reply_text("Em que posso lhe ajudar??")

def mytoken(bot, update):
    update.message.reply_text('Você quer meu Token? Ok né...')
    update.message.reply_text("Peraí...")
    time.sleep(2)
    update.message.reply_text('312719685:5bc4aaaa3385-6542ae862a172c19fb65Cc')
    update.message.reply_text(emojize('TROSLEI KKKKKKKKKKKKKKJJJLOL :joy: :ok_hand:', use_aliases=True))

def restart(bot, update):
	update.message.reply_text("Reiniciando...")
	time.sleep(3)
	update.message.reply_text("MENTIRA!")

def ping(bot, update):  
        update.message.reply_text("PING PONG É O CARALHO!")
	
def chat(bot, update):
    chat_id = update.message.chat_id
    message = update.message.text
    if 'manda' and 'nudes' in message:
            bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.UPLOAD_PHOTO)
            bot.sendPhoto(chat_id=chat_id, photo='http://i.imgur.com/DjMT3QT.png')
    if ('manda' and 'piada' in message) or ('conta' and 'piada' in message):
            update.message.reply_text("Não sou bom com piadas...")

updater = Updater('TOKEN')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('mytoken', mytoken))
updater.dispatcher.add_handler(CommandHandler('restart', restart))
updater.dispatcher.add_handler(CommandHandler('ping', ping))
updater.dispatcher.add_handler(MessageHandler([Filters.text], chat))
updater.start_polling()
updater.idle()
