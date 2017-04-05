import os #Importar os
import random #Importar random
import time #Importar time
import locale #Importar locale
import datetime as dt #Importar datetime nomeado para dt

from locale import setlocale #Importar setlocale de locale
from datetime import date #Importar date de datatime

for i in range(1, 7):
    # Vai escolher aleatoriamente entre essas saudações
    greeting = random.choice(("Ei", "Oi", "Olá", "Papai, é você?", "E aí", "kk eae men"))
    # Imprimir alguma saudação aleatória
    print("BOT:", greeting)
    #str(os.system("BOT:" +greeting+ ""))

    # O usuário digita
    answer = input("VOCÊ: ")
    # Verifica se o usuário digitou Irineu ou irineu
    if answer == "Irineu" or answer == "irineu":
        # Após verificar, é imprimido "Você não sabe e nem eu..."
        print("BOT: Você não sabe e nem eu...")

    # Verifica qualquer outra resposta da saudação    
    if answer not in greeting:
        # O BOT pergunta ao usuário como ele poderia o ajudar aleatoriamente
        howICanHelpYou = random.choice(("Você não é meu pai mas como posso te ajudar?", "Como posso te ajudar?", "Então, como eu posso te ajudar?"))
        # Uma pergunta é impressa
        print("BOT:", howICanHelpYou)
        #os.system("BOT:" +howICanHelpYou+ ".")


    
    ## DEIXA GUARDADO    
    """
    if "Caralho" or "Porra" or "Filho da Puta" or "Arrombado" or "fdp" or "Vai se fuder" or "vai se foder" or "vsf" == answer:
       print("Seu palavrão foi desnecessário, jovem! ;-;")
    """
    while 1:

        commands = ("horario", "")
        # O usuário digita qual comando quer usar
        chooseCommand = input("VOCÊ: ")
    
        cl = ""
        for command in commands:
            if command in chooseCommand:
                cl = command
            # Comando Horário
            if cl == "horario":
                #Data
                data = date.today()
                #Hora
                hora = dt.datetime.now().hour
                #Minuto
                minuto = dt.datetime.now().minute
                #Imprime na tela a data, hora e minuto
                print("Hoje é:", data, "\nE são:", hora, ":", minuto)
            """
            if cl == "nome":
                data = date.today()
                hora = dt.datetime.now().hour
                minuto = dt.datetime.now().minute
                print("Hoje é:", data, "\nE são:", hora, ":", minuto)
            """    
    break

