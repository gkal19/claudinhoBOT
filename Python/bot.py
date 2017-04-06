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
        howICanHelpYou = random.choice(("Você não é meu pai, porém como eu posso te ajudar?", "Como eu posso te ajudar?"))
        # Uma pergunta é impressa
        print("BOT:", howICanHelpYou)
        #os.system("BOT:" +howICanHelpYou+ ".")

        print("BOT: Cuidado ao digitar os comandos, tenha certeza de que escreveu eles em letras minúsculas e sem caracteres")
    
    ## DEIXA GUARDADO    
    """
    if "Caralho" or "Porra" or "Filho da Puta" or "Arrombado" or "fdp" or "Vai se fuder" or "vai se foder" or "vsf" == answer:
       print("Seu palavrão foi desnecessário, jovem! ;-;")
    """
    while 1:

        print("\nBOT: Comandos disponíveis:\nHorário\nSexo", "\n")
        commands = ["horario", "sexo", ""]
        # O usuário digita qual comando quer usar
        chooseCommand = input("VOCÊ: ")
    
        cl = ""
        for command in commands:
            if command in chooseCommand:
                cl = command
                
            # Comando Inválido
            if cl != "horario" or "sexo":
                print("BOT: Talvez este comando não esteja indisponível.\nVocê também poderia verificar se não há algum erro de digitação.")
                
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
                
            # Comando Sexo
            if cl == "sexo":
                print("BOT: Sexo online?\nIsso não me parece uma boa ideia.")
                canTry = input("VOCÊ: ")

                if "tentar" or "vamos lá" in canTry:
                    print("BOT: Minha resposta ainda é não, além do mais eu não tenho um corpo para isso.")
                    print("BOT: Vamos falar de outra coisa.")
                elif "tesão" in canTry:
                    print("BOT: O que é Tesão?")
                    whatIsIt = input("VOCÊ: ")

                    if "não sei" and "não sei explicar" in whatIsIt:
                        print("Que pena.")
                    else:
                        print("Acho que entendi. Obrigado!")
                
                
    break

