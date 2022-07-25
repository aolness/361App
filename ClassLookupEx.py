from tkinter import *
from tkinter.ttk import *
import json
from tkinter import messagebox

class LookupExercise:
    def __init__(self, frame):
        self.window = Frame(frame)
        self.window.grid(row=0, column=0)
        self.label = Label(self.window, text="Lookup exercises.").grid(row=0, column=0)

        self.moveTypeClicked = StringVar()
        self.regionClicked = StringVar()
        self.muscleClicked = StringVar()

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
                self.muscleDrop = OptionMenu(self.window, self.muscleClicked, None, *muscle, command=self.getExercises)
                self.muscleDrop.grid(row=2, column=2)
            else:
                self.muscleClicked.set('Legs')
                self.muscleDrop = OptionMenu(self.window, self.muscleClicked, 'Legs', command=self.getExercises)
                self.muscleDrop.grid(row=2, column=2)
        elif self.moveTypeClicked.get() == 'Accessory':
            if self.regionClicked.get() == 'Upper':
                muscle = ('Chest', 'Back', 'Shoulders', 'Biceps', 'Triceps')
                self.muscleClicked.set(muscle[0])
                self.muscleDrop = OptionMenu(self.window, self.muscleClicked, None, *muscle, command=self.getExercises)
                self.muscleDrop.grid(row=2, column=2)
            else:
                muscle = ('Legs', 'Calves')
                self.muscleClicked.set(muscle[0])
                self.muscleDrop = OptionMenu(self.window, self.muscleClicked, None, *muscle, command=self.getExercises)
                self.muscleDrop.grid(row=2, column=2)

    def getExercises(self, x):
        with open('ex.json', 'r+') as file:
            data = json.load(file)
            file.close()
        self.data =data['Exercises'][self.moveTypeClicked.get()][self.regionClicked.get()][self.muscleClicked.get()]
        self.lookupBtn = Button(self.window, text='Lookup', command=self.listEx)
        self.lookupBtn.grid(row=3, column=2)
        
    def listEx(self):
        for x in range(len(self.data)):
            txt = self.data[x]
            Label(self.window, text=txt).grid(row=x+3, column=1)
            btn = Button(self.window, text="Edit", command=lambda: self.editEx(txt))
            btn.grid(row=x+3, column=2)
            btn2 = Button(self.window, text='Delete', command=lambda: self.deleteEx(txt))
            btn2.grid(row=x+3, column=3)

    def editEx(self, text):
        print(text)

    def deleteEx(self, text):
        print(text)


       