from doctest import master
from email import message
from logging import root
from tkinter import *
from tkinter import messagebox, Tk, Button
from PIL import ImageTk
import time

master = Tk()

def uiPrint():
    info()
    print("")
    print(click)
    blankLine()

def info():
    print("Double click purchases need 50 clicks!")
    print("Auto clicker purchases need 75 clicks!")

info()

master.title('Cookie clicker announcement')
master.iconbitmap('D:/Загрузки/cookie.png')
master.geometry("300x300")
click = 0
mult = 1
dcp1 = 0

def blankLine():
    for i in range(20):
        print("")


def purchaseDoubleClicksCommand():
    global click
    global mult
    if click < 5:
        print("Not enough clicks!")
        blankLine()
    elif click >= 5:
        mult = mult*2
        click = click - 5
        messagebox.showinfo("DOUBLE CLICKS PURCHASED", "DOUBLE CLICKS PURCHASED")
        blankLine()


def purchaseAutoClickerCommand():
    global click
    if click < 7:
        print("Not enough clicks!")
        blankLine()
    elif click >= 7:
        click = click - 7
        messagebox.showinfo("AUTO CLICKER PURCHASED", "AUTO CLICKER PURCHASED")
        while True:
            click = click + 1
            time.sleep(1)


def buttonCommand():
    global click
    global mult
    click += 1*(mult)
    uiPrint()

    if click == 100:
        print('''Achievement Unlocked: Junior Clicker!
        BONUS 100 clicks!''')
        click += 100

    elif click == 400:
        print ('''Achievement Unlocked: Little Ninja Clicks!
        BONUS 200!''')
        click += 300

    elif click == 1500:
        print ('''Achievement Unlocked: Click Ninja Master!
        QUAD CLICKS!''')
        mult = mult * 4

    elif click == 3000:
        print ('''Achievement Unlocked:  Jackie Chan Style!
        8 TIMES THE CLICKS!''')
        mult = mult * 8

mainClickButton = Button(master, text="Click!", command = buttonCommand)
mainClickButton.pack()

purchaseDoubleClickButton = Button(master, text="Purchase Double Clicks", command = purchaseDoubleClicksCommand)
purchaseDoubleClickButton.pack()

purchaseAutoClickerButton = Button(master, text="Purchase Auto Clicker", command = purchaseAutoClickerCommand)
purchaseAutoClickerButton.pack()

master.title("Clicker! v0.0.6")
master.geometry("%sx%s+%s+%s" % (600,600,600,600))
mainloop()
