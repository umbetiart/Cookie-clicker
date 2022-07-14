from cProfile import label
from doctest import master
from email import message
from logging import root
from tkinter import *
from tkinter import messagebox, Tk, Button, Canvas, Frame, BOTH
from PIL import ImageTk, Image
import time


master = Tk()

frame = Frame(master)
frame.pack()

canvas = Canvas(master, width=0, height=0)
canvas.pack()

background1 = ImageTk.PhotoImage(file = "C:/Users/УмбетиарТ/Desktop/project clicker/gaflr.jpg")
canvas.create_image(800,566,image=background1)
label1 = Label(master, image = background1)
label1.place(x = 0, y = 0)

def uiPrint():
    info()
    print("")
    print(click)
    blankLine()
def info():
    print("Double click purchases need 50 clicks!")
    print("Auto clicker purchases need 75 clicks!")
    print("Home made cookies")
    print("Bakery")
    print("Factory")
    print("MINESHAFT")

info()

master.title('Cookie clicker announcement')
master.geometry("300x300")
click = 0
mult = 1
dcp1 = 0

our_button = ImageTk.PhotoImage(file="C:/Users/УмбетиарТ/Desktop/project clicker/cookie2.0.png.png")
canvas.create_image(30,30,image=our_button)

def blankLine():
    for i in range(5):
        print("")
Clicks_Text = IntVar()
Clicks_Text.set(click)
label2 = Label(master, text="Cookies counted:", fg="brown")
label2.place(x = 300, y=100)

CookieNumber_Label = Label(master, textvariable = Clicks_Text, font='Helvetica 10 bold')
CookieNumber_Label.place(x=395, y=100)

def every_second():
    global click, Clicks_Text, master
    Clicks_Text.set(click)
    master.after(50, every_second)

master.after(1000, every_second)
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
    if click < 10000:
        print("Not enough clicks!")
        blankLine()
    elif click >= 10000:
        click = click - 10000
        messagebox.showinfo("AUTO CLICKER PURCHASED", "AUTO CLICKER PURCHASED")
        while True:
            click = click + 1
            time.sleep(5)

def purchaseBakeryCommand():
        global click
        global mult
        if click < 100:
            print("Not enough clicks!")
            blankLine()
        elif click >= 100:
            mult = mult*3
            click = click - 100
            messagebox.showinfo("BAKERY PURCHASED", "BAKERY PURCHASED")
            messagebox.color
            blankLine()

def purchaseFactoryCommand():
        global click
        global mult
        if click < 500:
            print("Not enough clicks!")
            blankLine()
        elif click >= 500:
            mult = mult*4
            click = click - 500
            messagebox.showinfo("FACTORY PURCHASED", "FACTORY PURCHASED")
            messagebox.color
            blankLine()


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

def winGame():
    global click
    global mult
    if click < 10000:
        print("Not enough clicks!")
        blankLine()
    elif click >= 10000:
        messagebox.showinfo("GAME COMPLETE", "Is this the end?")
        messagebox.config(bg='pink', font=('times', 16, 'italic'))
        msg.pack()
        blankLine()


mainClickButton = Button(master, image=our_button, highlightthickness=0, bd=0, command=buttonCommand)
mainClickButton.place(x = 225, y=150)

purchaseDoubleClickButton = Button(master, text="Purchase Double Clicks", command = purchaseDoubleClicksCommand)
purchaseDoubleClickButton.place(x=150, y = 500)

purchaseBakeryClickerButton = Button(master, text="Purchase Bakery", command = purchaseBakeryCommand)
purchaseBakeryClickerButton.place(x=310, y = 500)

purchaseFactoryClickerButton = Button(master, text="Purchase Factory", command = purchaseFactoryCommand)
purchaseFactoryClickerButton.place(x=440, y = 500)

gameWinButton = Button(master, text="COMPLETE THE GAME", command = winGame)
gameWinButton.place(x=295, y = 450)
master.title("Cookie clicker")
master.geometry("800x533")
mainloop()
