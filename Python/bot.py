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
    if "Caralho" or "Porra" in answer:
       print("Seu palavrão foi desnecessário, jovem! ;-;")
    """
    
    while 1:

        print("\nBOT: Comandos disponíveis:\nHorário\nSexo\nPiada", "\n")
        
        commands = ("horario", "sexo", "piada")
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

            
    break

