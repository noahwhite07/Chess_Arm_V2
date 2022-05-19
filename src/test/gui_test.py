from logging.config import valid_ident
from mimetypes import init
from multiprocessing.sharedctypes import Value
from operator import ge
from tkinter import *
from turtle import right, update
from xmlrpc.client import Boolean
import matplotlib as plt
import cv2 as cv
from matplotlib import scale
from matplotlib.pyplot import grid
from numpy import number, true_divide
#from matplotlib.pyplot import grid 

# Create the window with dimensions and a title
window = Tk()
window.geometry('300x200')
window.resizable(False,False)
window.title("GUI Test")


window.rowconfigure(1, weight=1)

# Column for checkbotton
#window.columnconfigure(2, weight=1)

# Column for labels
window.columnconfigure(0, weight=1)

# Column for sliders
#window.columnconfigure(1, weight=3)

# Params
area = IntVar(value = 100)
areaBool = BooleanVar(value = False)

circularity = DoubleVar(value = .80)
circularityBool = BooleanVar(value = False)

convexivity = DoubleVar(value = .5)
convexivityBool = BooleanVar(value = False)

inertia = DoubleVar(value =.5)
inertiaBool = BooleanVar(value = False)

def onAreaChange(val): 
    area.set(val)
    print(f"area: {area.get()}")
    
def onAreaToggle(): 
    areaBool.set(not areaBool.get())
    print(f"areaBool: {areaBool.get()}")

def onCircChange(val): circularity.set(val)
 
def onCircToggle(): circularityBool.set(not circularityBool.get())
    

def onConvChange(val): convexivity.set(val)
    
def onConvToggle(): convexivityBool.set(not convexivityBool.get())
    

def onInertChange(val):inertia.set(val)
    
def onInertToggle():inertiaBool.set(not inertiaBool.get())
    


def updateParams(val = -1):
    print(f"area: {area.get()}")
    print(f"circularity: {circularity.get()}")
    print(val)
    
# Creates a frame with a label, checkbutton, and slider with specified control variables and command functions
def newParamControlFrame(label, min, max, buttonFunc, sliderFunc, buttonVar, sliderVar):
    
    # Contianer for the label, toggle, and slider
    frame = Frame(master = window)

    # Add the given label to the left side of the frame
    paramLabel = Label(master = frame, text = label)
    paramLabel.pack(side=LEFT, padx= (5,10), pady=(17,0))

    # Create new checkbutton with given function and variable
    cb = Checkbutton(
        master = frame, 
        #variable = buttonVar,
        command = buttonFunc
    )

    # Add the button to the right of the label
    cb.pack(side=LEFT, pady = (17,0))

    sliderVar = IntVar()
    # Create new slider with given function and variable
    paramSlider = Scale(
        frame,
        from_= min,
        to_= max,
        orient='horizontal',
        length = 200,
        variable = sliderVar,
        command = sliderFunc
    )

    # Add the slider to the right of the button
    paramSlider.pack(side=LEFT, padx= 10)
    return frame


def buildControlPanel():

    cf1 = newParamControlFrame("Test",0,100, onAreaToggle, onAreaChange, areaBool, area)
    cf1.grid(row=0)

    # cf2 = newParamControlFrame("Test dsadsa",0,500, circularityBool, circularity)
    # cf2.grid(row=1)


#labels = ["Area", "Circularity", "Convexivity", "Inertia"]


buildControlPanel()
window.mainloop()