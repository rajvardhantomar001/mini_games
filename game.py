from puzzle import *
from tkinter import *
from rahul import *
from PIL import Image, ImageTk
from gameoflifeimp import *
from main import *


def play():
    global rt
    if(rt.get() == 1):
        start_rahul()
    if(rt.get() == 2):
        start_raj()
    if(rt.get() == 3):
        start_abhi()
    if(rt.get() == 4):
        start_kri()


screen = Tk()
screen.title("Welcome to our Game")
screen.geometry("1280x720")
back_img = ImageTk.PhotoImage(Image.open("back.jpg"))
lab_back = Label(screen, image = back_img)
lab_back.grid(row = 0, column = 0, rowspan = 1280, columnspan = 720)
rt = IntVar()
rt.set(0)
btn1 = Radiobutton(screen, text = "Pong", variable = rt, value = 1)
btn2 = Radiobutton(screen, text = "2048", variable = rt, value = 2)
btn3 = Radiobutton(screen, text = "Snake", variable = rt, value = 3)
btn4 = Radiobutton(screen, text = "Game Of Life", variable = rt, value = 4)

btn1.grid(row = 200, column = 350)
btn2.grid(row = 300, column = 350)
btn3.grid(row = 400, column = 350)
btn4.grid(row = 500, column = 350)

start_btn = Button(screen, text = 'Start Game', command = play)
start_btn.grid(row = 600, column = 350)

screen.mainloop()