#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler
import logging
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(bot, update):
	update.message.reply_text("Oi, eu sou o NEO!")
	update.message.reply_text("Em que posso lhe ajudar??")

def mytoken(bot, update):
    update.message.reply_text('Você quer meu Token? Ok né...')
    time.sleep(5)
    update.message.reply_text('312719685:5bc4aaaa3385-6542ae862a172c19fb65Cc')

def restart(bot, update):
	update.message.reply_text("Reiniciando...")
	time.sleep(5)
	update.message.reply_text("MENTIRA! HAHAHAHAHAHAHAH")

updater = Updater('TELEGRAM_TOKEN')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('mytoken', mytoken))
updater.dispatcher.add_handler(CommandHandler('restart', restart))

updater.start_polling()
updater.idle()
