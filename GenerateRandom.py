from sqlite3 import Row
from tkinter import *
from tkinter.ttk import *
import json
import datetime
from tkcalendar import DateEntry


path = "C:/OSU/CS 361 Software Engineering I/VScode/361App/ex.json"

class GenRand:
    def __init__(self, frame, date, routine, randWorkout, main, acc):
        self.window = frame
        self.workout = randWorkout
        self.main = main
        self.acc = acc
        self.date = date
        self.routine = routine

        for widget in self.window.winfo_children():
            widget.destroy()
        Label(self.window, text="Here is your random workout for the day!").grid(row=0, column=0)

        self.createMain()
        self.createAcc()
        self.createDict()
        Button(self.window, text=f'Save Workout for {self.date}', command=self.submit).grid(row=self.main+self.acc+5, column=0, columnspan=2)
        

    def createMain(self):
        x=0
        Label(self.window, text="Main Lift(s): ").grid(row=1, column=0)
        while x < self.main:
            Label(self.window, text=self.workout[x]).grid(row=x+2, column=1)
            x += 1

    def createAcc(self):
        x=0
        Label(self.window, text="Accessory Lift(s): ").grid(row=self.main + x + 2, column=0)
        while x < self.acc:
            Label(self.window, text=self.workout[self.main + x]).grid(row=self.main + x + 3, column=1)
            x += 1

    def createDict(self):
        self.mLift={}
        self.aLift={}
        i=0
        for lift in self.workout[:self.main]:
            self.mLift[i]=lift
            i+=1
        i=0
        for lift in self.workout[self.main:]:
            self.aLift[i]=lift
            i+=1

    def submit(self):
        
        if self.date is None:
            self.pickDate()
        else:
            with open(path, 'r+') as file:
                data = json.load(file)
                add = True
                workoutLog = data['ExerciseLog']
                while add:
                    if str(self.date.year) in workoutLog:
                        if str(self.date.month) in workoutLog[str(self.date.year)]:
                            workoutLog[str(self.date.year)][str(self.date.month)][str(self.date.day)]={
                                'Routine':self.routine,
                                'Main': self.mLift,
                                'Accessory': self.aLift
                                }
                            add = False 
                        else:
                            workoutLog[str(self.date.year)][str(self.date.month)]={}
                    else:
                        workoutLog[str(self.date.year)] = {}
                data['ExerciseLog'] = workoutLog
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                file.close()
            for widget in self.window.winfo_children():
                widget.destroy()
            Label(self.window, text='Nice job, workout saved!').grid(row=0, column=0)

    def pickDate(self):
        self.top = Toplevel()
        self.top.title("Select a date")
        Label(self.top, text="Please select a date to save your workout.").grid(row=0, column=0)
        self.cal = DateEntry(self.top)
        self.cal.grid(row=1, column=0)
        
        Button(self.top, text='Select Date',command=self.back).grid(row=1, column=1)
        
    def back(self):
        self.date = self.cal.get_date()
        self.top.destroy()
        self.submit()

