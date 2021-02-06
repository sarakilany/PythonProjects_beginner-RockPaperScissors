# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 01:17:09 2021

@author: Ouso
"""

import tkinter as tk
import random

def playerchoice(userChoice):
    
    
    computerChoice = random.randint(1,3)
    if userChoice ==1:
        if computerChoice ==2:
            result = "Computer choose paper, you win"
            
        elif computerChoice ==1:
            result="Computer choose scissors, This is a tie"
        else:
            result ="Computer choose rock, you lose"
    elif userChoice ==2:
        if computerChoice ==1:
            result = "Computer choose scissors, you win"
        elif computerChoice ==2:
            result = "Computer choose paper, This is a tie"
        else:
            result = "Computer choose rock, you lose"
    elif userChoice ==3:
        if computerChoice ==1:
            result = "Computer choose scissors, you win"
        elif computerChoice ==3:
            result = "Computer choose rock, This is a tie"
        else:
            result = "Computer choose paper, you lose"
    global output
    output.config(text =result)

def pass_s():
    playerchoice(1)


def pass_r():
    playerchoice(3)


def pass_p():
    playerchoice(2)
    
window=tk.Tk()
window.title("This is the first GUI")
window.geometry("900x500")



label1=tk.Label(window,text="Press Scissors, Rock, or Paper",font=100)
#label1.grid(column=0,row=0)
label1.pack()

rock=tk.Button(window,text="Rock",height=2, width = 10,font = 20,command=pass_r)
#btn1.grid(column=3,row=1)
rock.pack()

paper=tk.Button(window,text="Paper",bg='red',height=2, width = 10,font = 20,command=pass_p)
#btn2.grid(column=3,row=2)
paper.pack()

scissors=tk.Button(window,text="Scissors",bg='yellow',height=2, width = 10,font = 20,command=pass_s)
#btn3.grid(column=3,row=3)
scissors.pack()
output = tk.Label(window, width=150, fg="blue",text='Waiting for choice',font = 20)
output.pack()

window.mainloop()