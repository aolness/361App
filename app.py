from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkcalendar import Calendar
import datetime
import CreateExercise
from ClassCreateEx import CreateExercise1

root = Tk()
root.title("Fittin dis pizza")
root.geometry("800x600")

"""Menubar functions"""

def goHome():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    txt="This is the home screen."
    Label(mainFrame, text=txt).pack()

def lookupExercise():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    txt="This is the lookupExercise screen."
    Label(mainFrame, text=txt).pack()

def createRoutine():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    txt="This is the createRoutine screen."
    Label(mainFrame, text=txt).pack()



def lookupRoutine():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    txt="This is the lookupRoutine screen."
    Label(mainFrame, text=txt).pack()

def calendar_view():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    days = [ [2022, 7, 1], [2022, 7, 11], [2022, 7, 21], [2022, 7, 26]]
    cal = Calendar(mainFrame)

    for date in days:
        year, month, day = date
        calD =datetime.datetime(year, month, day)
        cal.calevent_create(calD, "Workout", 'workout')

    cal.grid(row=1, column=1)  

def help_view():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    txt="This is the help screen."
    Label(mainFrame, text=txt).pack()



"""Creat the menubar"""
menubar = Menu(root)

home = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", menu=home)
home.add_command(label="Go Home", command=goHome)

exercise = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Exercises", menu=exercise)
exercise.add_command(label="Create", command=lambda: CreateExercise1(mainFrame))
exercise.add_command(label="Lookup", command=lookupExercise)

routine = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Routines", menu=routine)
routine.add_command(label="Create", command=createRoutine)
routine.add_command(label="Lookup", command=lookupRoutine)

calendar = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Calendar", menu=calendar)
calendar.add_command(label="View Calendar", command=calendar_view)

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="Get Help", command=help_view)

mainFrame = Frame(root)
mainFrame.pack()

txt="This is the home screen."
Label(mainFrame, text=txt).grid()


root.config(menu=menubar)
root.mainloop()