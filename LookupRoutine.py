from tkinter import *
from tkinter.ttk import *
import json
from tkinter import messagebox

from Scroll import ScrollableFrame


path = "C:/OSU/CS 361 Software Engineering I/VScode/361App/ex.json"

class LookupRoutine:
    def __init__(self, frame):
        self.window = frame
        self.label = Label(self.window, text="Update A Routine!").grid(row=0, column=0)

        self.lookupList = Frame(self.window)
        self.lookupList.grid(row=1, column=0)


        self.updateList = Frame(self.window, width=300, height=400, borderwidth=3)
        self.updateList.propagate(0)
        self.updateList.grid(row=1, column=3)

        self.routines = None

        self.display_routines()
        


    def display_routines(self):
        self.get_routines()
        self.create_widget()
        
        
    def get_routines(self):
        with open(path, 'r+') as file:
            data = json.load(file)
            file.close()
        self.routines = data["Routines"]


    def create_widget(self):
        temp = ScrollableFrame(self.lookupList)

        i = 0
        for routineName in self.routines:
            options = self.routines[routineName]
            x = LabelFrame(temp.scrollable_frame, text=routineName)
            x.grid(row=i, column=0)
            Label(x, text=f'Days: {options["Days"]}').grid(row=0, column=0)
            Label(x, text=f'Main Lifts: {options["Main"]}').grid(row=1, column=0)
            Label(x, text=f'Accessory Lifts: {options["Accessory"]}').grid(row=2, column=0)
            Label(x, text=f'Experience Level: {options["Level"]}').grid(row=3, column=0)
            
            Button(x, text='Edit', command=None).grid(row=1, column=1)
            Button(x, text='Delete', command=None).grid(row=2, column=1)
            i+=1

        temp.pack()




    

