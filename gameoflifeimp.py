import numpy as nu
from tkinter import *
from PIL import Image, ImageTk
import pygame
import time
import argparse

def upd(scr, cell, size, withprogress=False):
    global rules,BG,GRID, COLOR_NEXT,ALIVE,KEEP_ALIVE,BRING_TO_LIFE,SI,window,choice
    upc = nu.zeros(cell.shape)

    for row, col in nu.ndindex(cell.shape):
        nofalive = nu.sum(cell[row - 1: row + 2, col - 1: col + 2]) - cell[row, col]
        color = BG if cell[row, col] == 0 else ALIVE

        if cell[row, col] == 1:
            if nofalive not in KEEP_ALIVE:
                if withprogress:
                    color = BG
            else:
                upc[row, col] = 1
                if withprogress:
                    color = ALIVE

        else:
            if nofalive in BRING_TO_LIFE:
                upc[row, col] = 1
                if withprogress:
                    color = ALIVE

        pygame.draw.rect(scr, color, (col * size, row * size, size - 1, size - 1))

    return upc


def main():
    global rules,BG,GRID, COLOR_NEXT,ALIVE,KEEP_ALIVE,BRING_TO_LIFE,SI,window,choice
    pygame.init()
    
    if choice.get()==1:
        l=20
        b=15
    elif choice.get()==2:
        l=40
        b=30
    elif choice.get()==3:
        l=80
        b=60

    scr = pygame.display.set_mode((l*10, b*10))
    cell = nu.zeros((b, l))
    scr.fill(GRID)
    upd(scr, cell, SI)

    pygame.display.flip()
    pygame.display.update()

    is_on = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_on = not is_on
                    upd(scr, cell, SI)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                coordinates = pygame.mouse.get_pos()
                cell[coordinates[1] // SI, coordinates[0] // SI] = 1
                upd(scr, cell, SI)
                pygame.display.update()

        scr.fill(GRID)

        if is_on:
            cell = upd(scr, cell, SI, withprogress=True)
            pygame.display.update()

        time.sleep(0.01)

def start_kri():
    global rules,BG,GRID, COLOR_NEXT,ALIVE,KEEP_ALIVE,BRING_TO_LIFE,SI,window,choice
    rules = ["23","3"]
    BG = (34, 116, 130)
    window = Toplevel()
    window.title("Game of Life")
    window.geometry("400x400")
    img = ImageTk.PhotoImage(Image.open('back.jpg'))
    img_lbl = Label(window, image = img)
    img_lbl.grid(row = 0, column = 0, columnspan = 720, rowspan = 1280)
    #Baground colour
    GRID =(252, 255, 253)
    #Grid colour
    COLOR_NEXT=(84, 124, 125)
    #Colour of the cell dying next
    ALIVE=(12, 36, 18)
    #Colour of the alive cell
    # game parameters
    KEEP_ALIVE = [int(_) for _ in rules[0]]
    BRING_TO_LIFE = [int(_) for _ in rules[1]]
    SI = 10
    choice = IntVar()
    choice.set(0)
    label0 = Label(window, text = "Choose an option")
    label0.grid(row = 80, column = 90)
    label1 = Radiobutton(window, text = "Small Scale", variable = choice, value = 1)
    label1.grid(row = 140, column = 90)
    label2 = Radiobutton(window, text = "Intermediate Scale", variable = choice, value = 2)
    label2.grid(row = 200, column = 90)
    label3 = Radiobutton(window, text = "Large Scale", variable = choice, value = 3)
    label3.grid(row = 260, column = 90)
    st_bt = Button(window, text = 'Play', command = main)
    st_bt.grid(row = 320, column = 90)

    window.mainloop()
    

