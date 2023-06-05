from tkinter import *
import sys
import os

def submit():
    print("temperature is: " + str(scale.get()) + " C")

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

window = Tk()

hotimage = PhotoImage(file='hot.png')
hotlabel = Label(image=hotimage)
hotlabel.pack()

scale = Scale(window,
              from_=60,
              to=-30,
              length=500,
              width=20,
              orient=VERTICAL,  # orientation of scale could be horizontal
              font=("Consolas", 25),
              tickinterval=10,
              troughcolor="cyan",
              fg="black",
              bg="yellow"
              )
scale.pack()

coldimage = PhotoImage(file='Cold.png')
coldlabel = Label(image=coldimage)
coldlabel.pack()

button = Button(window, text="submit", command=submit)
button.pack()

Button(window, text="Restart", command=restart_program).pack()


window.mainloop()