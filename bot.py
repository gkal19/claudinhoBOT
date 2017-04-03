import telebot
from telebot import types

import os

TOKEN = "312719685:AAGjURfrXOxiY29FaLcRNiz9KvouANDAhv4"
chat_id = '306350863'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Oi, eu sou o Claudinho.\nComo posso te ajudar?")

@bot.message_handler(commands=['help', 'commands'])
def send_welcome(message):
	bot.reply_to(message, "Os comandos não estão disponíveis!")

@bot.message_handler(commands=['about'])
def send_welcome(message):
	bot.reply_to(message, "Gabriel Kalani (@ogabriel) me criou\nGithub: https://github.com/gkal19")

@bot.message_handler(commands=['irineu'])
def send_welcome(message):
	bot.reply_to(message, "Você não sabe e nem eu!")

@bot.message_handler(commands=['mytoken'])
def send_welcome(message):
	bot.reply_to(message, "Token Público:\n 4101bef87:4fed986e95dfb5ed10e1a3f28aeaa074a3a")

bot.polling()
