from tkinter import *
from tkinter import ttk
import cv2
import numpy as np
from PIL import ImageTk, Image
import Harmoni

main =Tk()

Scales = ['A','Ais','B','C','Cis','D','Dis','E','F','Fis','G','Gis']

def generateFretboard():
    scale=ddscale.get()                            #get variable from dropdown
    lab1_text.set(scale)
    x = Harmoni.CreateFretboardScale(scale)   
    imgFretboard = ImageTk.PhotoImage(file=".\img\Generated.jpg")        #load image and save in variable
    lab1_img.configure(image = imgFretboard)                              
    lab1_img.image = imgFretboard

def showAll():
    x = Harmoni.CreateFretboardAllTones()   
    imgFretboard = ImageTk.PhotoImage(file=".\img\Generated.jpg")        #load image and save in variable
    lab1_img.configure(image = imgFretboard)                              
    lab1_img.image = imgFretboard


def nextFunction():
    scale=ddscale.get()
    scale_index = Scales.index(scale) + 1

    if scale_index >= len(Scales):
        scale_index  = scale_index - len(Scales)

    ddscale.set(Scales[scale_index])
    scale=ddscale.get()
    
    lab1_text.set(scale)
    x = Harmoni.CreateFretboardScale(scale)   
    imgFretboard = ImageTk.PhotoImage(file=".\img\Generated.jpg")        #load image and save in variable
    lab1_img.configure(image = imgFretboard)                              
    lab1_img.image = imgFretboard

def prevFunction():
    scale=ddscale.get()
    scale_index = Scales.index(scale) - 1

    if scale_index < 0:
        scale_index  = scale_index + len(Scales)

    ddscale.set(Scales[scale_index])
    scale=ddscale.get()
    
    lab1_text.set(scale)
    x = Harmoni.CreateFretboardScale(scale)   
    imgFretboard = ImageTk.PhotoImage(file=".\img\Generated.jpg")        #load image and save in variable
    lab1_img.configure(image = imgFretboard)                              
    lab1_img.image = imgFretboard

#___Image Label
imgFretboard = ImageTk.PhotoImage(file=".\img\Fretboard.jpg")
lab1_img = Label(main,image=imgFretboard)
lab1_img.pack(side = BOTTOM)

#___DropDown Menu
ddscale = StringVar(main)
ddscale.set(Scales[0])
DropDown = OptionMenu(main, ddscale, *Scales)
DropDown.pack(side = LEFT)

#___Text Label
lab1_text = StringVar()
lab1_text.set("-select key-")
lab1 = Label(main, textvariable = lab1_text)
lab1.pack(side = LEFT)

#___Next
next = Button(main, text=">>>", command=nextFunction, width=6)
next.pack()


#___Prev
prev = Button(main, text="<<<", command=prevFunction, width=6)
prev.pack()

#___All Tones
all = Button(main, text="All Tones", command=showAll, width=6)
all.pack()

#___Button
apply = Button(main, text="APPLY", command=generateFretboard, width=6)
apply.pack(side = LEFT)

extit = Button(main, text="Quit", command=main.destroy).pack(side = RIGHT)

main.mainloop()