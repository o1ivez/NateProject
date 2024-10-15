#------------------------------------------------------------Functions------------------------------------------------------------
#this function opens a widget which lets you select a file to read and then returns each line of the data read
def readFile():
    root = tk.Tk()
    root.withdraw()
    data = []
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, 'r') as file:
            for i in file:
                data.append(i)
    return data

#creates a dictionary of numbers counting from 0 to the data from each line in the read
def createDataDick(data):
    i = 0
    dataDict = {}
    for i in data:
        print(i)
        splitData = i.strip().split(',')
        dataDict.update({splitData[0]: splitData[1]})
    return dataDict
#----------------------------------------------------------Start of Main----------------------------------------------------------

import numpy as np
#import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

dataDict = createDataDick(readFile())
print(dataDict)
#make code work based on input file perameters
