from dataclasses import dataclass
from sqlite3 import Row
from tkinter import *
from tkinter.ttk import *
import json
from tkcalendar import Calendar, DateEntry
import datetime

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

        self.routineClicked = StringVar()

        self.getDays()
        # self.buildWorkout()
        self.buildCalendar()
        
    def getDays(self):
        with open(path, 'r') as file:
            data = json.load(file)
            self.exercise = data['Exercises']
            self.routines = data['Routines']
            self.exerciseLog = data['ExerciseLog']
            file.close()
        
    def buildCalendar(self):
        self.cal = Calendar(self.calendarFrame)

        for year in self.exerciseLog:
            for month in self.exerciseLog[year]:
                for day in self.exerciseLog[year][month]:
                    year, month, day = int(year), int(month), int(day)
                    calD = datetime.datetime(year, month, day)
                    self.cal.calevent_create(calD, 'Workout', 'workout')
        self.cal.grid(row=0, column=0)
        Button(self.calendarFrame, text="View Day", command=self.viewDay).grid(row=1, column=0)

    def viewDay(self):
        eventID = self.cal.get_calevents(date=self.cal.selection_get()) # event id if available
        if len(eventID) > 0:
            self.viewWorkout()
        else:
            self.buildWorkout()

    def buildWorkout(self):
 
        temp = []
        for x in self.routines:
            temp.append(x)
        Label(self.workoutFrame, text="Choose a routine template!").grid(row=0, column=0)
        OptionMenu(self.workoutFrame, self.routineClicked, None, *temp, command=None).grid(row=0, column=1)

    def viewWorkout(self):
        pass