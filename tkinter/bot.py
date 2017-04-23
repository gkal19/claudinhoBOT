#! /usr/bin/env Python

# -----------------------
# Dependencies
from tkinter import *

# -----------------------
# Variables
root = Tk()

# -----------------------
# Code
root.title("BOT")
root.geometry("640x400")
root.resizable(0,0)
root["background"] = "#14191F"

lbYOU = Label(root, text = '> ')
lbYOU.place(x=3, y=348)

bt = Button(root, width=20, text="ENVIAR")
bt.place(x=483, y=348)

t_frame = Frame(root)
t_frame.grid(row=4, sticky=W, padx=50 ,pady=348)
t_text = Text(t_frame, width=49, height=1)

t_text.pack(side=LEFT, fill=BOTH)



root.mainloop()
