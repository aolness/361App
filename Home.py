from tkinter import *


class HomePage:
    def __init__(self, frame):
        self.window = frame

        self.createText()

    def createText(self):
        
        welcome = """
        Welcome to this Tkinter fitness app.

        To create or lookup already created exercises, click the Exercises tab.
            Exercises are used in a routine template to build a workout.

        To create or lookup already created routines, click the Routines tab.
            Routines are templates to help build workouts. You can create one from
            scratch, or use one of the pre-built routines.

        To view previously saved workouts or to save a new workout, click the Calendar tab.
            Be sure to check out the random workout generator on the calendar page too!

        Try creating an exercise, then add it to a routine template and save a workout.
        """
        T = Label(self.window, text=welcome, font=('Times', '14', 'bold'))
        T.grid(row=0, column=0)

        Label(self.window, text='Andrew Olness 2022').grid(row=2, column=0)
        



