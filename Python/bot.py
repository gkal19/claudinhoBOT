import os
import random
import time

for i in range(1, 5):
    greeting = random.choice(("Ei", "Oi", "Olá", "Papai, é você?"))
    print(greeting)
    str(os.system("BOT:" +greeting+ ""))

    answer = input("")

    if answer not in ("eae", "E aí"):
        howICanHelpYou = random.choice(("Você não é meu pai mas como posso te ajudar?", "Como posso te ajudar?", "Então, como eu posso te ajudar?"))
        print(howICanHelpYou)
        os.system("BOT:" +howICanHelpYou+ ".")

    if "Caralho" or "Porra" or "Filho da Puta" or "Arrombado" or "fdp" or "Vai se fuder" or "vai se foder" or "vsf" in answer:
        print("Seu palavrão foi desnecessário, jovem! ;-;")

        break
