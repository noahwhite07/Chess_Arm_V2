from tkinter import *
from tkinter.colorchooser import askcolor

import cv2 as cv
import json
import os
import numpy as np


# Create the window with dimensions and a title
window = Tk()
window.geometry('800x400')
window.resizable(False,False)
window.title("GUI Test")

# Split window into 4 equal rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)

window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=2)

# Blob detector params
area = IntVar(value = 50)
areaBool = BooleanVar(value = False)

circularity = DoubleVar(value = .80)
circularityBool = BooleanVar(value = False)

convexivity = DoubleVar(value = .5)
convexivityBool = BooleanVar(value = False)

inertia = DoubleVar(value =.5)
inertiaBool = BooleanVar(value = False)

hsv_low = [IntVar(value=0), IntVar(value=0), IntVar(value=0)]
hsv_high = [IntVar(value=0), IntVar(value=0), IntVar(value=0)]


# Generate path of params file (assumes params.json in same dir as script)
path = os.path.dirname(__file__) + "/params.json"

# Open the JSON file for reading
params_file = open(path, mode= "r")

# Convert JSON to dictionary
params = json.load(params_file)


def load_params():
    
    areaBool.set(params["area"][0])
    area.set(params["area"][1])

    circularityBool.set(params["circularity"][0])
    circularity.set(params["circularity"][1])

    convexivityBool.set(params["convexivity"][0])
    convexivity.set(params["convexivity"][1])

    inertiaBool.set(params["inertia"][0])
    inertia.set(params["inertia"][1])

    # Close the file
    params_file.close()

    

load_params()

def save_params():
    # Open the JSON file for writing
    params_file = open(path, mode= "w")

    # Update the JSON object with current parameter values
    params["area"][0] = areaBool.get()
    params["area"][1] = area.get()

    params["circularity"][0] = circularityBool.get()
    params["circularity"][1] = circularity.get()

    params["convexivity"][0] = convexivityBool.get()
    params["convexivity"][1] = convexivity.get()

    params["inertia"][0] = inertiaBool.get()
    params["inertia"][1] = inertia.get()

    params["colorBounds"] = [
        getHSVBounds(0),
        getHSVBounds(1)
    ]
    # Overwrite the existing JSON file with modified data
    params_file.write(json.dumps(params))

    # Close the file
    params_file.close()

    pass

def on_closing():
    save_params()
    window.destroy()


# Update each param's value when its corresponding toggle/slider are updated by the user
def onAreaChange(val): area.set(val)
  
def onAreaToggle(): areaBool.set( areaBool.get())

def onCircChange(val): circularity.set(val)
def onCircToggle(): circularityBool.set(circularityBool.get())
    
def onConvChange(val): convexivity.set(val)  
def onConvToggle(): convexivityBool.set(convexivityBool.get())
    
def onInertChange(val):inertia.set(val)  
def onInertToggle():inertiaBool.set(inertiaBool.get())
    

# Create a new blob detector with given params
def updateParams(val = -1):
    # This function will eventually be necessary
    pass

# Set either the low or high hsv bounds
def setHSVBounds(hi_lo, hsv):
    if(hi_lo == 0):
        for i, val in enumerate(hsv):
            hsv_low[i].set(val)
    else:
        for i, val in enumerate(hsv):
            hsv_high[i].set(val)

# Returns the low or high hsv bounds a list
def getHSVBounds(hi_lo):
    if hi_lo == 0:
        return [hsv_low[0].get(), hsv_low[1].get(), hsv_low[2].get()]
    else: 
        return [hsv_high[0].get(), hsv_high[1].get(), hsv_high[2].get()]


# Displays color chooser widget on hsv bound button press
def changeColor(event, button, hi_lo):
    colors = askcolor(title = "Choose Color for Bound")
    print(colors)
    button.configure(bg= colors[1])
    rgb = np.uint8([[np.asarray(colors[0])]])
 
    hsv = cv.cvtColor(rgb, cv.COLOR_RGB2HSV)[0][0]


    setHSVBounds(hi_lo, hsv)
    
            
    print(f"HSV low bound: {getHSVBounds(0)}")
    print(f"HSV high bound: {getHSVBounds(1)}")
    


def newColorRangeFrame(label, hi_lo, boxFuncs = -1, boxVars = -1):
    frame = Frame(master=window)

    # Add the given label to the left side of the frame
    boxLabel = Label(master=frame, text=label, width= 15)
    boxLabel.pack(side=LEFT, padx= (5,10))

    # A comma label to seperate the boxes
    commaLabel = Label(master=frame, text=",")

    button = Button(
        master=frame
        )
    button.pack(side=LEFT, padx= (5,10))
    button.bind("<ButtonRelease-1>", func= lambda event, b = button: changeColor(event, b, hi_lo))
    # Create spinbox for each arg of HSV 
    hue = Spinbox(
        master=frame, 
        to=179, 
        from_=0, 
        width = 5
        )
    sat = Spinbox(
        master=frame, 
        to=255, 
        from_=0, 
        width = 5
        )
    val = Spinbox(
        master=frame, 
        to=255, 
        from_=0, 
        width = 5
        )

    hue.pack(side=LEFT, padx= (5,27))
    sat.pack(side=LEFT, padx= (5,27))
    val.pack(side=LEFT, padx= (5,27))
    
    
    return frame


# Create a frame with a label, checkbutton, and slider with specified event-handler functions
def newParamControlFrame(label, min, max, buttonFunc, sliderFunc, buttonVar, sliderVar):
    
    # Contianer for the label, toggle, and slider
    frame = Frame(master = window)

    # Add the given label to the left side of the frame
    paramLabel = Label(master = frame, text = label, width=10)
    paramLabel.pack(side=LEFT, padx= (5,10), pady=(17,0))

    # Create new checkbutton with given function and variable
    cb = Checkbutton(
        master = frame, 
        variable = buttonVar,
        command = buttonFunc
    )

    # Add the button to the right of the label
    cb.pack(side=LEFT, pady = (17,0))

    # Create new slider with given function and variable
    paramSlider = Scale(
        frame,
        from_= min,
        to_= max,
        orient='horizontal',
        length = 200,
        variable = sliderVar,
        command = sliderFunc,
        
    )
    #paramSlider.bind(sequence="<ButtonRelease-1>", func = sliderFunc)
    


    # Add the slider to the right of the button
    paramSlider.pack(side=LEFT, padx= 10)
    return frame

# Adds a control frame for each parameter to the window
def buildControlPanel():

    cf1 = newParamControlFrame("Area", 0, 1000, onAreaToggle, onAreaChange, areaBool, area)
    cf1.grid(column=0, row=0, sticky= "W")

    cf2 = newParamControlFrame("Circularity", 0, 100, onCircToggle, onCircChange, circularityBool, circularity)
    cf2.grid(column=0,row=1, sticky= "W")

    cf3 = newParamControlFrame("Convexivity", 0, 100, onConvToggle, onConvChange, convexivityBool, convexivity)
    cf3.grid(column=0,row=2, sticky= "W")

    cf4 = newParamControlFrame("Inertia", 0, 100, onInertToggle, onInertChange, inertiaBool, inertia)
    cf4.grid(column=0, row=3, sticky= "W")

    colorFrame1 = newColorRangeFrame("HSV Low Bound", hi_lo=0)
    colorFrame1.grid(column= 0, row=4, sticky= "W")

    colorFrame2 = newColorRangeFrame("HSV High Bound", hi_lo=1)
    colorFrame2.grid(column= 0, row=5, sticky= "W")

# Add all the frames to the window
buildControlPanel()


#sb.grid(column=0, row = 4)

# Set the current params to be saved on window close
window.protocol("WM_DELETE_WINDOW", on_closing)

# Run the gui
window.mainloop()