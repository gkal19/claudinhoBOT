#! /usr/bin/env Python

import os 
import random
import time 
import locale 
import datetime as dt 
import webbrowser

from locale import setlocale 
from datetime import date 

for i in range(1, 7):
    greeting = random.choice(("Oi", "Olá", "Papai, é você?", "E aí", "kk eae men", "Irineu"))
    print("BOT:", greeting)

    answer = input("VOCÊ: ")

    if greeting == "Papai, é você?":
        print("BOT: me enganei, você não é meu pai")
    
    if answer not in greeting:
        howICanHelpYou = random.choice(("Precisa de ajuda em quê?", "Como eu posso te ajudar?"))
        print("BOT:", howICanHelpYou)
        print("\nBOT: Cuidado ao digitar os comandos, tenha certeza de que escreveu eles em letras minúsculas e sem caracteres")
    
    elif answer == "":
        print("BOT: Vai falar nada, não?")

    """
    Palavrões 
    if "Caralho" or "Porra" in answer:
       print("Seu palavrão foi desnecessário, jovem! ;-;")
    """
    
    while 1:

        print("\nBOT: Comandos disponíveis:\nHorário\nPiada\nSomar\nMultiplicar\nPesquisa", "\n")
        
        commands = ("horario","piada","somar","multiplicar","pesquisa","")
        chooseCommand = input("VOCÊ: ")
    
        cl = chooseCommand
           
        # Comando Inválido
        if cl not in commands:
            print("BOT: Comando Inválido!")
        elif cl != commands:
            print("BOT: Eu sugiro que digite algo")
            
        # Comando Horário
        if cl == "horario":
            data = date.today()
            hora = dt.datetime.now().hour
            minuto = dt.datetime.now().minute
            print("Hoje é:", data, "\nE são:", hora, ":", minuto)

        # Comando Piada
        if cl == "piada":
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

        # Comando Pesquisa
        if cl == "pesquisa":
            tabUrl= "http://www.google.com/?#q="
            new = 2
            questionSearch = random.choice(("O que deseja pesquisar hoje?","O que deseja saber?","Quer procurar o quê hoje?"))
            print("BOT:", questionSearch)
            search = input("VOCÊ: ")
            webbrowser.open(tabUrl+search, new=new)
            print("No momento não tenho uma função para exibir o resultado de sua pesquisa aqui.\nNão esquenta, enviei sua pesquisa para seu navegador.")
            
            
    break
