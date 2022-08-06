from tkinter import *
from tkinter.ttk import *
import json
from tkinter import messagebox

from Scroll import ScrollableFrame

path = "C:/OSU/CS 361 Software Engineering I/VScode/361App/ex.json"

class LookupExercise:
    def __init__(self, frame):
        self.window = frame
        self.label = Label(self.window, text="Lookup An Exercise!").grid(row=0, column=0)


        
        self.lookUpList = Frame(self.window, borderwidth=3)
        self.lookUpList.grid(row=4, column=0, columnspan=3)
        

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
                muscle = ('Legs', 'Legs')
                self.muscleClicked.set(muscle[0])
                self.muscleDrop = OptionMenu(self.window, self.muscleClicked, None, *muscle, command=self.getExercises)
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
        for widget in self.lookUpList.winfo_children():
            widget.destroy()
        with open(path, 'r+') as file:
            data = json.load(file)
            file.close()
        self.data =data['Exercises'][self.moveTypeClicked.get()][self.regionClicked.get()][self.muscleClicked.get()]
        self.lookupBtn = Button(self.window, text='Lookup', command=self.listEx)
        self.lookupBtn.grid(row=3, column=2)
        
    def listEx(self):
        scroll = ScrollableFrame(self.lookUpList)

        for i in range(len(self.data)):
            txt = self.data[i]
            Label(scroll.scrollable_frame, text=txt).grid(row=i, column=1)
            temp = [self.moveTypeClicked.get(), self.regionClicked.get(), self.muscleClicked.get(), self.data]
            btn2 = Button(scroll.scrollable_frame, text='Delete', command=lambda x=i: self.deleteEx(temp, x+1))
            btn2.grid(row=i, column=3)

        scroll.pack()

    def deleteEx(self, text, x):
        popup = messagebox.askokcancel('Confirm', f'Are you sure you want to delete {text[3][x-1]}')
        if popup == 1:
            with open(path, 'r+') as file:
                data = json.load(file)
                data['Exercises'][text[0]][text[1]][text[2]].remove(text[3][x-1])
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                file.close()
            self.data=data['Exercises'][self.moveTypeClicked.get()][self.regionClicked.get()][self.muscleClicked.get()]
            self.getExercises(x)
            


    


       