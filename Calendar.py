from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import json
from tkcalendar import Calendar
import datetime
from GenerateRandom import GenRand
from micro import partnersClient as client
import random

path = "C:/OSU/CS 361 Software Engineering I/VScode/361App/ex.json"

class BuildCalendar:
    def __init__(self, frame):
        
        self.calendarFrame = Frame(frame)
        self.workoutFrame = Frame(frame)
        self.calendarFrame.grid(row=0, column=1)
        self.workoutFrame.grid(row=0, column=0)

        self.exerciseLog = None
        self.exercise = None
        self.routines = None
        self.date = None
        self.randomize = None
        self.builtTemplate = []

        self.routineClicked = StringVar()

        self.getData()
        self.getMain()
        self.getAccessory()
        self.buildWorkout()
        self.buildCalendar()

    #get main exercises
    def getMain(self):
        self.main = []
        for position in self.exercise['Compound']:
            for group in self.exercise['Compound'][position]:
                for lift in self.exercise['Compound'][position][group]:
                    self.main.append(lift)

    #get accessory exercises
    def getAccessory(self):
        self.accessory = []
        for position in self.exercise['Accessory']:
            for group in self.exercise['Accessory'][position]:
                for lift in self.exercise['Accessory'][position][group]:
                    self.accessory.append(lift)

    #get saved db/json file
    def getData(self):
        with open(path, 'r') as file:
            data = json.load(file)
            self.exercise = data['Exercises']
            self.routines = data['Routines']
            self.exerciseLog = data['ExerciseLog']
            file.close()
        
    def buildCalendar(self):
        self.cal = Calendar(self.calendarFrame)
        for year in self.exerciseLog:
            for month in self.exerciseLog[str(year)]:
                for day in self.exerciseLog[str(year)][str(month)]:
                    year, month, day = int(year), int(month), int(day)
                    calD = datetime.datetime(year, month, day)
                    self.cal.calevent_create(calD, 'Workout', 'workout')
        self.cal.grid(row=0, column=0, columnspan=2, sticky='E')
        Button(self.calendarFrame, text="View Day", command=self.viewDay).grid(row=1, column=0)
        Button(self.calendarFrame, text='Refresh Calendar', command=self.refresh).grid(row=1, column=1)

    #refresh calendar after update
    def refresh(self):
        self.getData()
        self.buildCalendar()

    def viewDay(self):
        self.date = self.cal.selection_get()
        eventID = self.cal.get_calevents(date=self.date) 
        if len(eventID) > 0:
            self.viewWorkout()
        else:
            self.buildWorkout()

    def buildWorkout(self):
        for widget in self.workoutFrame.winfo_children():
            widget.destroy()
        temp = []
        for x in self.routines:
            temp.append(x)
        Label(self.workoutFrame, text="Selected day from the calendar: ").grid(row=0, column=0)
        Label(self.workoutFrame, text=self.date).grid(row=0, column=1)
        Label(self.workoutFrame, text="Choose a routine template!").grid(row=1, column=0)
        OptionMenu(self.workoutFrame, self.routineClicked, None, *temp, command=self.template).grid(row=1, column=1)
        Button(self.workoutFrame, text="Generate Random Workout!", command=self.getRand).grid(row=2, column=0, columnspan=2)
        self.templateFrame = Frame(self.workoutFrame)
        self.templateFrame.grid(row=3, column=0)

    #template allows users to make exercise selections
    def template(self, x):
        for widget in self.templateFrame.winfo_children():
            widget.destroy()
        main = self.routines[x]['Main']
        accessory = self.routines[x]['Accessory']
        Label(self.templateFrame, text=f'Select {main} main lift(s).').grid(row=0, column=0, ipady=10)
        self.mainDict={}
        self.accessoryDict={}
        x=0
        while x < main:
            self.mainDict[x]=StringVar()
            temp = OptionMenu(self.templateFrame, self.mainDict[x], None, *self.main, command=None)
            temp.grid(row=x+1, column=0)
            x+=1
        x=0
        Label(self.templateFrame, text=f'Select {accessory} accessory lift(s)').grid(row=main+1, column=0, ipady=10)
        while x < accessory:
            self.accessoryDict[x]=StringVar()
            temp = OptionMenu(self.templateFrame, self.accessoryDict[x], None, *self.accessory, command=None)
            temp.grid(row=x+2+main, column=0)
            x+=1
        Button(self.templateFrame, text="Save Workout", command=self.saveWorkout).grid(row=main+accessory+2, column=0)

    #temp exercise dict used for saving workout
    def createDict(self):
        self.mLift={}
        self.aLift={}
        i=0
        for _ in self.mainDict:
            self.mLift[i]=self.mainDict[_].get()
            i+=1
        i=0
        for _ in self.accessoryDict:
            self.aLift[i]=self.accessoryDict[_].get()
            i+=1

    def saveWorkout(self):
        self.createDict()
        if self.date is None:
            messagebox.showerror('No Date Error', 'Please select a date from the calendar.')
        if len(self.aLift) > 0 and len(self.mLift) > 0:
            with open(path, 'r+') as file:
                data = json.load(file)
                add = True
                workoutLog = data['ExerciseLog']
                while add:
                    if str(self.date.year) in workoutLog:
                        if str(self.date.month) in workoutLog[str(self.date.year)]:
                            workoutLog[str(self.date.year)][str(self.date.month)][str(self.date.day)]={
                                'Routine':self.routineClicked.get(),
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

    #view previously saved workout
    def viewWorkout(self):
        for widget in self.workoutFrame.winfo_children():
            widget.destroy()
        Label(self.workoutFrame, text=f'Workout from {self.date}:').grid(row=0, column=0, ipadx=10)
        temp = self.exerciseLog[str(self.date.year)][str(self.date.month)][str(self.date.day)]
        Label(self.workoutFrame, text=f"Routine: {temp['Routine']}").grid(row=1, column=0)
        i=2
        for _ in temp['Main']:
            Label(self.workoutFrame, text=temp['Main'][_]).grid(row=i, column=0)
            i+=1
        for _ in temp['Accessory']:
            Label(self.workoutFrame, text=temp['Accessory'][_]).grid(row=i, column=0)
            i+=1

    #build list for random microservice
    def getRand(self):
        mainNum = self.routines[self.routineClicked.get()]['Main']
        accNum = self.routines[self.routineClicked.get()]['Accessory']
        result = self.buildMain(mainNum) + self.buildAcc(accNum)
        GenRand(self.templateFrame, self.date, self.routineClicked.get(), result, mainNum, accNum)
        
    # main exercises for getRand
    def buildMain(self, mainNum):
        result = []
        x=0
        while x < mainNum:
            request = ['Compound']
            region = random.choice(list(self.exercise['Compound'].keys()))
            request.append(region)
            group = random.choice(list(self.exercise['Compound'][region].keys()))
            request.append(group)
            temp =client.send_list(request)
            result.append(temp)
            x += 1
        return result

    # accessory exercises for getRand
    def buildAcc(self, accNum):
        result = []
        x = 0
        while x < accNum:
            request = ['Accessory']
            region = random.choice(list(self.exercise['Accessory'].keys()))
            request.append(region)
            group = random.choice(list(self.exercise['Accessory'][region].keys()))
            request.append(group)
            temp =client.send_list(request)
            result.append(temp)
            x += 1
        return result
