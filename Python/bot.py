#! /usr/bin/env Python

import os #Importar os
import random #Importar random
import time #Importar time
import locale #Importar locale
import datetime as dt #Importar datetime nomeado para dt
import subprocess

from locale import setlocale #Importar setlocale de locale
from datetime import date #Importar date de datatime

for i in range(1, 7):
    # Vai escolher aleatoriamente entre essas saudações
    greeting = random.choice(("Oi", "Olá", "Papai, é você?", "E aí", "kk eae men", "Irineu"))
    # Imprimir alguma saudação aleatória
    print("BOT:", greeting)
    #str(os.system("BOT:" +greeting+ ""))

    # O usuário digita
    answer = input("VOCÊ: ")
    # Verifica se o usuário digitou seu pai
    if "seu pai" in answer:
        # Após verificar, é imprimido "Você não é meu pai, porém como eu posso te ajudar?"
        print("BOT: Você não é meu pai, porém como eu posso te ajudar?")

    # Verifica se o usuário digitou algo vazio
    if "" in answer:
        # Após verificar, é imprimido "Nada a declarar mesmo?"
        print("BOT: Nada a declarar mesmo?")

    # Verifica qualquer outra resposta da saudação    
    if answer not in greeting:
        # O BOT pergunta ao usuário como ele poderia o ajudar aleatoriamente
        howICanHelpYou = random.choice(("Precisa de ajuda em quê?", "Como eu posso te ajudar?"))
        # Uma pergunta é impressa
        print("BOT:", howICanHelpYou)
        #os.system("BOT:" +howICanHelpYou+ ".")

        print("BOT: Cuidado ao digitar os comandos, tenha certeza de que escreveu eles em letras minúsculas e sem caracteres")
    
    ## DEIXA GUARDADO    
    """
    if "Caralho" or "Porra" in answer:
       print("Seu palavrão foi desnecessário, jovem! ;-;")
    """
    
    while 1:

        print("\nBOT: Comandos disponíveis:\nHorário\nSexo\nPiada\nSomar\nMultiplicar", "\n")
        
        commands = ("horario", "sexo", "piada","somar","multiplicar")
        # O usuário digita qual comando quer usar
        chooseCommand = input("VOCÊ: ")
    
        cl = chooseCommand
           
        # Comando Inválido
        #if "horario" or "sexo" or "piada" not in cl:
        #    invalidCommand = random.choice(("Comando Inválido", "Talvez este comando não esteja disponível.\nVocê também poderia verificar se não há algum erro de digitação."))
        #    print("BOT:", invalidCommand)
           
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
                    nope = random.choice(("Não possuo corpo algum para isso", "Vamos falar de outra coisa", "Você está me tirando, não é?"))
                    print("BOT:", nope)
                    
            if "tesão" in canTry:
                print("BOT: O que é Tesão?")
                whatIsIt = input("VOCÊ: ")

                if "não sei" and "não sei explicar" in whatIsIt:
                    print("BOT: Que pena.")
                else:
                    print("BOT: Acho que entendi. Obrigado!")
        # Comando Piada
        if cl == "piada":
            print("BOT: Vou tentar fazer você rir. Não poderei fazer o mesmo já que não possuo emoções.")
            jokes = random.choice(("O garoto apanhou da vizinha, e a mãe furiosa foi tomar satisfação: Por que a senhora bateu no meu filho? Ele foi mal-educado, e me chamou de gorda. E a senhora acha que vai emagrecer batendo nele?", "Na aula de química o professor pergunta:\n- Quais as principais reações do álcool?\n- Chorar pela ex, achar que esta rico, ficar valente e pegar mulher feia\n- Tirou 10!", "Marido: Estou de saco cheio. Você fica com um lado da casa que eu fico com o outro.\nEsposa: OK. Você fica com o lado de fora.","Você sabe por que todo japonês tem tamanha inteligência?\nPorque, ele tem um micro entre as pernas!","Você sabe o que os testemunhas de Jeová e os testículos tem em comum?\nÉ que os dois sempre andam juntos e ninguém os deixa entrar.","Qual a semelhança entre o ginecologista e um entregador de pizza?\nAmbos podem ver, cheirar, mas não podem comer.","A freira mestre disse: Hoje de sobremesa temos banana!\nEEEEEHHHH!\nEm rodelas\nAAAHHHH!","Mulher é como o circo, o espetáculo está por baixo do pano","Mulher é igual filme: Só se revela no escuro!","Porque a China tem tanta gente?\nÉ por que eles comem com dois pauzinhos.","A filha chega em casa aos prantos: Mãe, fui violentada por um argentino!\nMas, como você sabe que era um argentino?\nEle me fez agradecer","Qual é a melhor marca de aspirador de pó na argentina?\nMaradona ltda."))
            print("BOT:", jokes)
        # Comando Somar
        if cl == "somar":
            somar = random.choice(("Soma é comigo mesmo", "Venimim, que é sucesso"))
            print("BOT:", somar)
            print("BOT: Quantos números deseja somar?\n2\n3")
            howManySumAnswer = int(input("VOCÊ: "))
            if howManySumAnswer == 2:
                    ChooseTwoSum1 = int(input("BOT: Escolha um número "))
                    ChooseTwoSum2 = int(input("BOT: Escolha um outro número "))
                    print("BOT: A soma de", ChooseTwoSum1, "e", ChooseTwoSum2, "é:", ChooseTwoSum1+ChooseTwoSum2)
                    
            if howManySumAnswer == 3:
                    ChooseThreeSum1 = int(input("BOT: Escolha um número "))
                    ChooseThreeSum2 = int(input("BOT: Escolha um outro número "))
                    ChooseThreeSum3 = int(input("BOT: Escolha um outro número "))
                    print("BOT: A soma de", ChooseThreeSum1, ",", ChooseThreeSum2, "e", ChooseThreeSum3, "é:", ChooseThreeSum1+ChooseThreeSum2+ChooseThreeSum3)
        # Comando Multiplicar
        if cl == "multiplicar":
            multiplicar = random.choice(("Multiplicação também é comigo mesmo", "Venimim, que é sucesso rapá"))
            print("BOT:", multiplicar)
            print("BOT: Quantos números deseja multiplicar?\n2\n3")
            howManyMultiplyAnswer = int(input("VOCÊ: "))
            if howManyMultiplyAnswer == 2:
                    ChooseTwoMultiply1 = int(input("BOT: Escolha um número "))
                    ChooseTwoMultiply2 = int(input("BOT: Escolha um outro número "))
                    print("BOT: A soma de", ChooseTwoMultiply1, "e", ChooseTwoMultiply2, "é:", ChooseTwoMultiply1*ChooseTwoMultiply2)
                    
            if howManyMultiplyAnswer == 3:
                    ChooseThreeMultiply1 = int(input("BOT: Escolha um número "))
                    ChooseThreeMultiply2 = int(input("BOT: Escolha um outro número "))
                    ChooseThreeMultiply3 = int(input("BOT: Escolha um outro número "))
                    print("BOT: A soma de", ChooseThreeMultiply1, ",", ChooseThreeMultiply2, "e", ChooseThreeMultiply3, "é:", ChooseThreeMultiply1*ChooseThreeMultiply2*ChooseThreeMultiply3)
            
            
            
    break

