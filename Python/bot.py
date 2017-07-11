#! /usr/bin/env Python

# ----------------------------
# Dependências
import random
import time
import socket
import datetime as dt
import webbrowser
import platform

import pygoogle

from datetime import date
from time import strftime
# ----------------------------
# Variáveis
greeting = random.choice(("Oi", "Olá", "Papai, é você?", "E aí", "kk eae men", "Irineu"))
howICanHelpYou = random.choice(("Precisa de ajuda em quê?", "Como eu posso te ajudar?"))

commands = ("horario","piada","pesquisa","meuip","data","meusistema","localizacao","")

data = date.today()
hora = dt.datetime.now().hour
minuto = dt.datetime.now().minute

urlGoogle= "http://www.google.com.br/?#q="
new = 1
questionSearch = random.choice(("O que deseja pesquisar hoje?","O que deseja saber?","Quer procurar o quê hoje?"))

ip_address = socket.gethostbyname(socket.gethostname())

# ----------------------------
# Código (começa abaixo)
print("Iniciando...")
time.sleep(random.randint(1, 3))

for i in range(1, 7):
    print("BOT:", greeting)
    answer = input("VOCÊ: ")

    if greeting == "Papai, é você?":
        print("BOT: me enganei, você não é meu pai.")

    if answer == "":
        print("BOT: Vai falar nada, não?")
        print("\nBOT: Cuidado ao digitar os comandos, tenha certeza de que escreveu eles em letras minúsculas e sem caracteres")
    else:
        print("BOT:", howICanHelpYou)
        print("\nBOT: Cuidado ao digitar os comandos, tenha certeza de que escreveu eles em letras minúsculas e sem caracteres")

    while 1:

        print("\nBOT: Comandos disponíveis:\nData\nHorário\nPiada\nPesquisa\nMeuIP\nMeuSistema\nLocalização\n")
        chooseCommand = input("VOCÊ: ")

        cl = chooseCommand

        # Comando Inválido
        if cl not in commands:
            print("BOT: Comando Inválido!")

        # Comando Data
        if cl == "data":
            print("BOT: Hoje é:", data)

        # Comando Horário
        if cl == "horario":
            print("BOT: Pela sua localização atual vejo que são:", hora, ":", minuto)

        # Comando Pesquisa
        if cl == "pesquisa":
            print("BOT:", questionSearch)
            search = input("VOCÊ: ")
            if search == "nada":
                print("BOT: Nada? Isso tá errado ae. Depois dessa vou embora! Tchau!")
                time.sleep(2)
                break
            else:
                print("BOT: No momento estou sem uma função para isso. Não esquenta, em alguns segundos vou mandar sua pesquisa para seu navegador.")
                time.sleep(random.randint(3, 5))
                webbrowser.open(urlGoogle+search, new=new)

        # Comando MeuIP
        if cl == "meuip":
            if ip_address != "127.0.0.1":
                print("BOT: Seu IP é", ip_address)
            else:
                print("BOT: Você deve estar sem acesso a internet, já que seu IP está como:", ip_address)

        # Comando MeuSistema
        if cl == "meusistema":
            if platform.system() == "Linux":
                print("BOT: Você está usando", platform.system(), platform.release())
            elif platform.system() == "Windows" or platform.system() == "win32":
                print("BOT: Você está usando",platform.system(), platform.release())
            elif platform.system() == "darwin":
                print("BOT: Você está usando", platform.system(), platform.release())

    break
