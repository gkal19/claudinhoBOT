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

jokes = random.choice(("O garoto apanhou da vizinha, e a mãe furiosa foi tomar satisfação: Por que a senhora bateu no meu filho? Ele foi mal-educado, e me chamou de gorda. E a senhora acha que vai emagrecer batendo nele?", "Na aula de química o professor pergunta:\n- Quais as principais reações do álcool?\n- Chorar pela ex, achar que esta rico, ficar valente e pegar mulher feia\n- Tirou 10!", "Marido: Estou de saco cheio. Você fica com um lado da casa que eu fico com o outro.\nEsposa: OK. Você fica com o lado de fora.","Você sabe por que todo japonês tem tamanha inteligência?\nPorque, ele tem um micro entre as pernas!","Você sabe o que os testemunhas de Jeová e os testículos tem em comum?\nÉ que os dois sempre andam juntos e ninguém os deixa entrar.","Qual a semelhança entre o ginecologista e um entregador de pizza?\nAmbos podem ver, cheirar, mas não podem comer.","A freira mestre disse: Hoje de sobremesa temos banana!\nEEEEEHHHH!\nEm rodelas\nAAAHHHH!","Mulher é como o circo, o espetáculo está por baixo do pano","Mulher é igual filme: Só se revela no escuro!","Porque a China tem tanta gente?\nÉ por que eles comem com dois pauzinhos.","A filha chega em casa aos prantos: Mãe, fui violentada por um argentino!\nMas, como você sabe que era um argentino?\nEle me fez agradecer","Qual é a melhor marca de aspirador de pó na argentina?\nMaradona ltda."))

urlGoogle= "http://www.google.com/?#q="
new = 2
questionSearch = random.choice(("O que deseja pesquisar hoje?","O que deseja saber?","Quer procurar o quê hoje?"))

num_page = 3

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

        # Comando Piada
        if cl == "piada":
            print("BOT:", jokes)

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
                print("BOT: Você está usando OS X", platform.system(), platform.release())
        # Comando MeuSistema
        if cl == "localizacao":
            print("")
        
    break
