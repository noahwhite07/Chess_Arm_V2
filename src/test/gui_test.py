from tkinter import *
import cv2 as cv
import json
import os

from matplotlib import container

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

def newColorRangeFrame(label, boxFuncs = -1, boxVars = -1):
    frame = Frame(master=window)

    # Add the given label to the left side of the frame
    boxLabel = Label(master=frame, text=label, width= 15)
    boxLabel.pack(side=LEFT, padx= (5,10))

    # A comma label to seperate the boxes
    commaLabel = Label(master=frame, text=",")

    button = Button(master=frame, )
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

    colorFrame = newColorRangeFrame("HSV Low Bound")
    colorFrame.grid(column= 0, row=4, sticky= "W")

    colorFrame = newColorRangeFrame("HSV High Bound")
    colorFrame.grid(column= 0, row=5, sticky= "W")

# Add all the frames to the window
buildControlPanel()


#sb.grid(column=0, row = 4)

# Set the current params to be saved on window close
window.protocol("WM_DELETE_WINDOW", on_closing)

# Run the gui
window.mainloop()