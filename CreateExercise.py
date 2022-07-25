from tkinter import *

def createExercise1(frame):
    global moveDrop
    global moveTypeClicked

    for widget in frame.winfo_children():
        widget.destroy()
    txt="""This is the createExercise screen. Here you can create an exercise
     that can be stored for later use."""
    Label(frame, text=txt).grid(row=0, column=0)
    txt="Build an exercise"
    myLab = Label(frame, text=txt).grid(row=1, column=0)

    #region Dropdown
    def regionFn(x):  
        global regionDrop
        global regionClicked  

            #muscle Dropdown
        def muscleFn(y):
            global muscleClicked
            global muscleDrop

            if moveTypeClicked.get() == 'Compound':
                if regionClicked.get() == 'Upper':
                    muscle = ('Chest', 'Back', 'Shoulders')
                    muscleClicked = StringVar()
                    muscleClicked.set(muscle[0])
                    muscleDrop = OptionMenu(frame, muscleClicked, None, *muscle).grid(row=2, column=2)
                else:
                    muscleClicked = StringVar()
                    muscleClicked.set('Legs')
                    muscleDrop = OptionMenu(frame, muscleClicked, 'Legs').grid(row=2, column=2)
            elif moveTypeClicked.get() == 'Accessory':
                if regionClicked.get() == 'Upper':
                    muscle = ('Chest', 'Back', 'Shoulders', 'Biceps', 'Triceps')
                    muscleClicked = StringVar()
                    muscleClicked.set(muscle[0])
                    muscleDrop = OptionMenu(frame, muscleClicked, None, *muscle).grid(row=2, column=2)
                else:
                    muscle = ('Legs', 'Calves')
                    muscleClicked = StringVar()
                    muscleClicked.set(muscle[0])
                    muscleDrop = OptionMenu(frame, muscleClicked, None, *muscle).grid(row=2, column=2)
            print(muscleClicked.get())
            print(moveTypeClicked.get())
            print(regionClicked.get())

        region = ('Upper', 'Lower')
        regionClicked = StringVar()
        regionClicked.set(region[0])
        regionDrop = OptionMenu(frame, regionClicked, None, *region, command=muscleFn).grid(row=2, column=1)

    #moveType Dropdwon
    moveType = ("Compound", "Accessory")
    moveTypeClicked = StringVar()
    moveTypeClicked.set(moveType[0])
    moveDrop = OptionMenu(frame, moveTypeClicked, None, *moveType, command=regionFn).grid(row=2, column=0)

    
    


    
    

    


