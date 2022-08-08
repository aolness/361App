from tkinter import *
from tkinter.ttk import *
import json
from tkinter import messagebox

path = "C:/OSU/CS 361 Software Engineering I/VScode/361App/ex.json"

class CreateRoutine:

    def __init__(self, frame):

        self.window = Frame(frame)
        self.window.grid(row=0, column=0)
        self.label = Label(self.window, text="Create a Routine!").grid(row=0, column=0)
        
        self.daysClicked = IntVar()
        self.mainClicked = IntVar()
        self.accessoryClicked = IntVar()
        self.levelClicked = StringVar()

        self.confirmLabel = Label(self.window, text=None)
        self.confirmLabel.grid(row=8, column=1)
        self.newRoutine = None

        self.create_widgets()

    def create_widgets(self):
        daysLabel = Label(self.window, text="Days:")
        daysLabel.grid(row=2, column=0)
        days = (1,2,3,4,5,6,7)
        self.daysClicked.set(days[0])
        self.daysDrop = OptionMenu(self.window, self.daysClicked, None, *days, command=self.mainFn)
        self.daysDrop.grid(row=2, column=1)

    #selector for number of main lifts
    def mainFn(self, x):
        mainLabel = Label(self.window, text="# of Main Lifts:")
        mainLabel.grid(row=3, column=0)
        mainLift = (0,1,2,3,4,5,6,7,8,9)
        self.mainClicked.set(mainLift[0])
        self.mainDrop = OptionMenu(self.window, self.mainClicked, None, *mainLift, command=self.accessoryFn)
        self.mainDrop.grid(row=3, column=1)

    #selector for number of accessory lifts
    def accessoryFn(self, x):
        accessoryLabel = Label(self.window, text="# of Accessory Lifts")
        accessoryLabel.grid(row=4, column=0)
        accessoryLift = (0,1,2,3,4,5,6,7,8,9)
        self.accessoryClicked.set(accessoryLift[0])
        self.accessoryDrop = OptionMenu(self.window, self.accessoryClicked, None, *accessoryLift, command=self.levelFn)
        self.accessoryDrop.grid(row=4, column=1)

    #selector for experience level
    def levelFn(self, x):
        levelLabel = Label(self.window, text="Experience Level")
        levelLabel.grid(row=5, column=0)
        levels = ('Beginner', 'Intermediate', 'Advanced')
        self.levelClicked.set(levels[0])
        self.levelDrop = OptionMenu(self.window, self.levelClicked, None, *levels, command=self.nameRoutine)
        self.levelDrop.grid(row=5, column=1)

    def nameRoutine(self, x):
        self.newRoutineLabel = Label(self.window, text="New Routine Name:")
        self.newRoutineLabel.grid(row=6, column=0)
        self.newRoutine = Entry(self.window, width=20)
        self.newRoutine.grid(row=6, column=1)
        self.submit = Button(self.window, text="Submit", command=self.saveNew)
        self.submit.grid(row=7, column=1)

    def saveNew(self):
        if self.newRoutine.get() != '':
            self.popup = messagebox.askokcancel('Confirm', 'Are you sure you want to create?')
            if self.popup == 1:
                with open(path, 'r+') as file:
                    data = json.load(file)
                    data['Routines'][self.newRoutine.get()]={
                        "Days":self.daysClicked.get(),
                        'Main':self.mainClicked.get(),
                        "Accessory":self.accessoryClicked.get(),
                        "Level":self.levelClicked.get()}
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.close()
                txt = self.newRoutine.get() + ' added!'
                self.confirmLabel.configure(text=txt)
            else:
                self.confirmLabel.configure(text='None added')
            self.newRoutine.select_clear()
        else:
            l = Label(self.window, text="Please enter a name.")
            l.grid(row=9, column=1)