#export info to arduino
import tkinter as tk
from tkinter import *

def buttonClick():
    #get the data from and entry box
    time = timeInput.get()
    temp = tempInput.get()
    tk.Canvas(mainLoop, width = 70, height = 54, bg ='#F0F0F0').grid(row=3, pady=3) #makes canvas to cover up prior error or sucess messages
    if(time.isdigit() and temp.isdigit()):
        sucessMessgae = Message(mainLoop, text="Values sent to Arduino",bg='lightgreen').grid(row=3, pady=3)
        exportToArduino(time, temp)
    else:
        errorMessage = Message(mainLoop, text="Please enter valid values",bg='red').grid(row=3, pady=3)
#todo
def exportToArduino(time, temp):
    pass

#sets up tkinter main gui
mainLoop = tk.Tk()
mainLoop.title('Arduino Setup')

#sets time label and entry box
tk.Label(mainLoop, text='Input Time (sec)').grid(row=0, pady=3)
timeInput = tk.Entry(mainLoop)
timeInput.grid(row=0, column=1, pady=3)

#sets temp label and entry box
tk.Label(mainLoop, text='Input Temperature (f)').grid(row=1, pady=3)
tempInput = tk.Entry(mainLoop)
tempInput.grid(row=1, column=1, pady=3)

#sets up export changes button
exportButton = tk.Button(mainLoop, text='Export Specifications', width=25, command = buttonClick).grid(row=2, column=2, pady=3)

#sets up stop button on program
closeButton = Button(mainLoop, text='Close Program', width=25, command=mainLoop.destroy).grid(row=3, column=2, pady=3)

#keeps gui running until interrupt occurs
mainLoop.mainloop()
