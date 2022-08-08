from tkinter import *
from tkinter.ttk import *
import json
from tkinter import messagebox

from UpdateRoutine import UpdateRoutine
from Scroll import ScrollableFrame


path = "C:/OSU/CS 361 Software Engineering I/VScode/361App/ex.json"

class LookupRoutine:
    def __init__(self, frame):
        self.window = frame
        self.label = Label(self.window, text="Update A Routine!").grid(row=0, column=0)

        self.lookupList = Frame(self.window, width=300, height=400, borderwidth=3)
        self.lookupList.grid_propagate(0)
        self.lookupList.grid(row=1, column=0)

        self.updateList = Frame(self.window, width=300, height=400, borderwidth=3)
        self.updateList.grid_propagate(0)
        self.updateList.grid(row=1, column=3)

        self.routines = None

        self.display_routines()
        
    def display_routines(self):
        for widget in self.lookupList.winfo_children():
            widget.destroy()
        self.get_routines()
        self.create_widget()
        
    def get_routines(self):
        with open(path, 'r+') as file:
            data = json.load(file)
            file.close()
        self.routines = data["Routines"]

    def create_widget(self):
        temp = ScrollableFrame(self.lookupList)
        nameList = []
        i = 0
        for routineName in self.routines:
            options = self.routines[routineName]
            
            nameList.append(routineName)
            x = LabelFrame(temp.scrollable_frame, text=routineName)
            x.grid(row=i, column=0)
            Label(x, text=f'Days: {options["Days"]}').grid(row=0, column=0)
            Label(x, text=f'Main Lifts: {options["Main"]}').grid(row=1, column=0)
            Label(x, text=f'Accessory Lifts: {options["Accessory"]}').grid(row=2, column=0)
            Label(x, text=f'Experience Level: {options["Level"]}').grid(row=3, column=0)
            
            Button(x, text='Edit', command=lambda x=i: self.editRoutine(nameList, x)).grid(row=2, column=1)
            Button(x, text='Delete', command=lambda x=i: self.deleteRoutine(nameList, x)).grid(row=1, column=1)
            
            i+=1

        temp.pack()

    def deleteRoutine(self, routine, x):

        popup = messagebox.askokcancel('Confirm', f'Are you sure you want to delete {routine[x]}?')
        if popup == 1:
            with open(path, 'r+') as file:
                data = json.load(file)
                routine_data = data['Routines']
                del routine_data[routine[x]]
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                file.close()
        self.display_routines()

    def editRoutine(self, routine, x):
        UpdateRoutine(self.window, routine[x])
    




    

