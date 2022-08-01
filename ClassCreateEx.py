from tkinter import *
from tkinter.ttk import *
import json
from tkinter import messagebox
import os


class CreateExercise1:
    
    def __init__(self, frame):

        self.window = Frame(frame)
        self.window.grid(row=0, column=0)
        self.label = Label(self.window, text="Create an exercise!").grid(row=0, column=0)
        
        self.moveTypeClicked = StringVar()
        self.regionClicked = StringVar()
        self.muscleClicked = StringVar()
        
        self.confirmLabel = Label(None, text=None)
        self.confirmLabel.grid(row=5, column=1)
        self.newEx = None


        self.create_widgets()

    def create_widgets(self):
        moveType = ("Compound", "Accessory")
        self.moveTypeClicked.set(moveType[0])
        self.moveDrop = OptionMenu(self.window, self.moveTypeClicked, None, *moveType, command=self.regionFn)
        self.moveDrop.grid(row=2, column=0)

    def regionFn(self, x):
        region = ('Upper', 'Lower')
        self.regionClicked.set(region[0])
        self.regionDrop = OptionMenu(self.window, self.regionClicked, None, *region, command=self.muscleFn)
        self.regionDrop.grid(row=2, column=1)

    def muscleFn(self, x):
        if self.moveTypeClicked.get() == 'Compound':
            if self.regionClicked.get() == 'Upper':
                muscle = ('Chest', 'Back', 'Shoulders')
                self.muscleClicked.set(muscle[0])
                self.muscleDrop = OptionMenu(self.window, self.muscleClicked, None, *muscle, command=self.nameExercise)
                self.muscleDrop.grid(row=2, column=2)
            else:
                muscle = ('Legs', '')
                self.muscleClicked.set('Legs')
                self.muscleDrop = OptionMenu(self.window, self.muscleClicked, None, *muscle, command=self.nameExercise)
                self.muscleDrop.grid(row=2, column=2)
        elif self.moveTypeClicked.get() == 'Accessory':
            if self.regionClicked.get() == 'Upper':
                muscle = ('Chest', 'Back', 'Shoulders', 'Biceps', 'Triceps')
                self.muscleClicked.set(muscle[0])
                self.muscleDrop = OptionMenu(self.window, self.muscleClicked, None, *muscle, command=self.nameExercise)
                self.muscleDrop.grid(row=2, column=2)
            else:
                muscle = ('Legs', 'Calves')
                self.muscleClicked.set(muscle[0])
                self.muscleDrop = OptionMenu(self.window, self.muscleClicked, None, *muscle, command=self.nameExercise)
                self.muscleDrop.grid(row=2, column=2)

    def nameExercise(self, x):
        self.newExLabel = Label(self.window, text="New Exercise Name:")
        self.newExLabel.grid(row=3, column=0)
        self.newEx = Entry(self.window, width=20)
        self.newEx.grid(row=3, column=1)
        self.submit = Button(self.window, text="Submit", command=self.saveNew)
        self.submit.grid(row=4, column=1)
    
    def saveNew(self):
        if self.newEx.get() != '':
            self.popup = messagebox.askokcancel('Confirm', 'Are you sure you want to create?')
            if self.popup == 1:
                with open("361App/ex.json", 'r+') as file:
                    data = json.load(file)
                    data['Exercises'][self.moveTypeClicked.get()][self.regionClicked.get()][self.muscleClicked.get()].append(self.newEx.get())
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.close()
                txt = self.newEx.get() + ' added!'
                self.confirmLabel.configure(text=txt)
            else:
                self.confirmLabel.configure(text="None added")
            self.newEx.select_clear()
        else:
            l = Label(self.window, text="Please enter a name.")
            l.grid(row=5, column=1)

  
