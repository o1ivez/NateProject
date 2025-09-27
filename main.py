import tkinter as tk
from tkinter import *
import serial   #need to pip install pyserial for this to work
import time

def sendTimeAndTemp():
    #get the data from entry box
    inputTime = timeInput.get()
    temp = tempInput.get()
    global timeTempSucessOrFail
    if timeTempSucessOrFail is not None:
        timeTempSucessOrFail.destroy()
    if inputTime.isdigit() and temp.isdigit():
        timeTempSucessOrFail = Message(root, text="Values sent to Arduino", bg='lightgreen', width=75)
        timeTempSucessOrFail.grid(row=3, pady=3)
        exportToArduino(inputTime, temp)
    else:
        timeTempSucessOrFail = Message(root, text="Please enter valid values", bg='red', width=75)
        timeTempSucessOrFail.grid(row=3, pady=3)

def exportToArduino(inputTime, temp): #BIG NOTE, DO NOT USE ARDUINO SERIAL MONITOR WHILE RUNNING
    #sends both time and temp data to the arduno 
    arduino.write(bytes(inputTime,'utf-8'))
    time.sleep(0.005)
    arduino.write(bytes(temp,'utf-8'))
    pass

#sets up tkinter main gui
root = tk.Tk()
root.title('Arduino Setup')
root.geometry('500x500')

#set up message vars, there is prob a better way of doing this
timeTempSucessOrFail = None

#set up arduino connection
arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1) #this depends on how the arduino is set up physicaly ie change com port if needed

#sets time label and entry box
tk.Label(root, text='Input Time (sec)').grid(row=0, pady=3)
timeInput = tk.Entry(root)
timeInput.grid(row=0, column=1, pady=3)

#sets temp label and entry box
tk.Label(root, text='Input Temperature (f)').grid(row=1, pady=3)
tempInput = tk.Entry(root)
tempInput.grid(row=1, column=1, pady=3)

#sets up export changes button
exportButton = tk.Button(root, text='Export Specifications', width=25, command = sendTimeAndTemp).grid(row=2, column=2, pady=3)

#sets up stop button on program
closeButton = Button(root, text='Close Program', width=25, command=root.destroy).grid(row=3, column=2, pady=3)

#keeps gui running until interrupt occurs
root.mainloop()
