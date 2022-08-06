from tkinter import *
from tkinter.ttk import *
import json
from tkinter import messagebox


path = "C:/OSU/CS 361 Software Engineering I/VScode/361App/ex.json"

class UpdateRoutine:
    def __init__(self, frame, routine):
        self.window = Frame(frame)
        self.window.grid(row=1, column=1)
        self.routineName = routine

        self.warningLabel = Label(self.window)

        self.get_routines()
        self.create_labels()
        self.create_entry()
        self.create_buttons()

    def get_routines(self):
        with open(path, 'r+') as file:
            data = json.load(file)
            file.close()
        self.routinesList = data["Routines"]
        self.routinesList=self.routinesList[self.routineName]

    def create_labels(self):
        Label(self.window, text=f"Update {self.routineName}").grid(row=0, column=0)
        daysLabel = Label(self.window, text='Days: ')
        daysLabel.grid(row=2, column=0)
        mainLabel = Label(self.window, text='# of Main Lifts: ')
        mainLabel.grid(row=3, column=0)
        accessoryLabel = Label(self.window, text='# of Accessory LIfts: ')
        accessoryLabel.grid(row=4, column=0)
        experienceLabel = Label(self.window, text='Experience Level: ')
        experienceLabel.grid(row=5, column=0)

    def create_entry(self):
        self.daysEntry = Entry(self.window, width=20)
        self.daysEntry.insert(0, self.routinesList['Days'])
        self.daysEntry.grid(row=2, column=1)
        self.mainEntry = Entry(self.window, width=20)
        self.mainEntry.insert(0, self.routinesList['Main'])
        self.mainEntry.grid(row=3, column=1)
        self.accessoryEntry = Entry(self.window, width=20)
        self.accessoryEntry.insert(0, self.routinesList['Accessory'])
        self.accessoryEntry.grid(row=4, column=1)
        self.experienceEntry = Entry(self.window, width=20)
        self.experienceEntry.insert(0, self.routinesList['Level'])
        self.experienceEntry.grid(row=5, column=1)

    def create_buttons(self):
        Button(self.window, text='Submit', command=self.save_new).grid(row=6, column=0)
        Button(self.window, text='Cancel', command=self.close).grid(row=6, column=1)

    def save_new(self):
        if self.verify():
            options = {'Days': int(self.daysEntry.get()), 'Main': int(self.mainEntry.get()), 'Accessory': int(self.accessoryEntry.get()), 'Level':self.experienceEntry.get()}
            popup = messagebox.askokcancel('Confirm', f'Are you sure you want to update {self.routineName}?')
            if popup == 1:
                with open(path, 'r+') as file:
                    data = json.load(file)
                    data['Routines'][self.routineName] = options
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                    file.close()
                self.close()
            else:
                self.close()

    def close(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def verify(self):
        try:
            int(self.daysEntry.get())
            int(self.mainEntry.get())
            int(self.accessoryEntry.get())
            self.warningLabel.grid_forget()
            return True
        except ValueError:
            self.warningLabel= Label(self.window, text='Days and number of lifts must be integers.')
            self.warningLabel.grid(row=7, columnspan=2)
            return False
        