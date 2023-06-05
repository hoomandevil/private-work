from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    colorhex = color[1]
    window.config(bg=colorhex)


window = Tk()
window.geometry('420x420')
button = Button(text='choose color', command=click)
button.pack()
window.mainloop()