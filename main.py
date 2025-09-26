import tkinter as tk
from tkinter import *
import serial   #need to pip install pyserial for this to work
import time

def buttonClick():
    #get the data from entry box
    global current_message
    inputTime = timeInput.get()
    temp = tempInput.get()
    if current_message is not None:
        current_message.destroy()
    if inputTime.isdigit() and temp.isdigit():
        current_message = Message(mainLoop, text="Values sent to Arduino", bg='lightgreen').grid(row=3, pady=3)
        exportToArduino(inputTime, temp)
    else:
        current_message = Message(mainLoop, text="Please enter valid values", bg='red').grid(row=3, pady=3)

def exportToArduino(inputTime, temp): #BIG NOTE, DO NOT USE ARDUINO SERIAL MONITOR WHILE RUNNING
    #sends both time and temp data to the arduno 
    arduino.write(bytes(inputTime,'utf-8'))
    time.sleep(0.005)
    arduino.write(bytes(temp,'utf-8'))
    pass

#sets up tkinter main gui
mainLoop = tk.Tk()
mainLoop.title('Arduino Setup')

#set up arduino connection
arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1) #this depends on how the arduino is set up physicaly ie change com port if needed

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
