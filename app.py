from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkcalendar import Calendar
import datetime

from ClassLookupEx import LookupExercise
from ClassCreateEx import CreateExercise1

root = Tk()
root.title("Fittin dis pizza")
root.geometry("800x600")

mainFrame = Frame(root)
mainFrame.grid()


def createExercise():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    creatEx=Frame(mainFrame, height=600, width=800, relief=SUNKEN, borderwidth=5 )
    creatEx.grid_propagate(0)
    creatEx.grid(row=0, column=0)
    CreateExercise1(creatEx)

def lookupExercise():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    lookupEx=Frame(mainFrame, height=600, width=800, relief=SUNKEN, borderwidth=5)
    lookupEx.grid_propagate(0)
    lookupEx.grid(row=0, column=0)
    LookupExercise(lookupEx)


menubar = Menu(root)
home = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", menu=home)
home.add_command(label="Go Home", command=None)

exercise = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Exercises", menu=exercise)
exercise.add_command(label="Create", command=lambda: createExercise())
exercise.add_command(label="Lookup", command=lambda: lookupExercise())

routine = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Routines", menu=routine)
routine.add_command(label="Create", command=None)
routine.add_command(label="Lookup", command=None)

calendar = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Calendar", menu=calendar)
calendar.add_command(label="View Calendar", command=None)

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="Get Help", command=None)


root.config(menu=menubar)
root.mainloop()