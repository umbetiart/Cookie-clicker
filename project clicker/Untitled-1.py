from cProfile import label
from doctest import master
from email import message
from logging import root
from tkinter import *
from tkinter import messagebox, Tk, Button, Canvas, Frame, BOTH
from PIL import ImageTk
import time

master = Tk()

bg = PhotoImage(file = "C:/Users/1/Desktop/project clicker/L.png")
label1 = Label(master, image = bg)
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

our_button = PhotoImage(file="C:/Users/1/Desktop/project clicker/cookie.png")
our_button = our_button.subsample(2,2)

def blankLine():
    for i in range(5):
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
        messagebox.color
        blankLine()
click = 0 
label1 = Label(master, textvariable = click, font=('Times 14'), width=20, height=5)
label1.pack() 
for i in range(6): 
    time.sleep(1)   
    master.update_idletasks()



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

def purchaseBakeryCommand():
    global click
    if click < 100:
        print("Not enough clicks!")
        blankLine()
    elif click >= 100:
        click = click - 100
        messagebox.showinfo("BAKERY PURCHASED", "BAKERY PURCHASED")
        while True:
            click = click + 10
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


mainClickButton = Button(master, image=our_button, highlightthickness=0, bd=0, command=buttonCommand)
mainClickButton.place(x = 190, y=0)
mainClickButton.pack()

purchaseDoubleClickButton = Button(master, text="Purchase Double Clicks", command = purchaseDoubleClicksCommand)
purchaseDoubleClickButton.place(x=800, y = 100)
purchaseDoubleClickButton.pack()

purchaseAutoClickerButton = Button(master, text="Purchase Auto Clicker", command = purchaseAutoClickerCommand)
purchaseAutoClickerButton.pack()

master.title("Cookie clicker")
master.geometry("800x533")
mainloop()
