from tkinter import *
import cv2 as cv

# Create the window with dimensions and a title
window = Tk()
window.geometry('800x300')
window.resizable(False,False)
window.title("GUI Test")

# Split window into 4 equal rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)


#window.columnconfigure(0, weight=1)



# Blob detector params
area = IntVar(value = 100)
areaBool = BooleanVar(value = False)

circularity = DoubleVar(value = .80)
circularityBool = BooleanVar(value = False)

convexivity = DoubleVar(value = .5)
convexivityBool = BooleanVar(value = False)

inertia = DoubleVar(value =.5)
inertiaBool = BooleanVar(value = False)


# Update each param's value when its corresponding toggle/slider are updated by the user
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
    

# Create a new blob detector with given params
def updateParams(val = -1):
    pass
    
# Create a frame with a label, checkbutton, and slider with specified event-handler functions
def newParamControlFrame(label, min, max, buttonFunc, sliderFunc):
    
    # Contianer for the label, toggle, and slider
    frame = Frame(master = window)

    # Add the given label to the left side of the frame
    paramLabel = Label(master = frame, text = label, width=10)
    paramLabel.pack(side=LEFT, padx= (5,10), pady=(17,0))

    # Create new checkbutton with given function and variable
    cb = Checkbutton(
        master = frame, 
        variable = BooleanVar(),
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
        #variable = sliderVar,
        command = sliderFunc,
        
    )

    # Add the slider to the right of the button
    paramSlider.pack(side=LEFT, padx= 10)
    return frame

# Adds a control frame for each parameter to the window
def buildControlPanel():

    cf1 = newParamControlFrame("Area", 0, 1000, onAreaToggle, onAreaChange)
    cf1.grid(row=0)

    cf2 = newParamControlFrame("Circularity", 0, 100, onCircToggle, onCircChange)
    cf2.grid(row=1)

    cf3 = newParamControlFrame("Convexivity", 0, 100, onConvToggle, onConvChange)
    cf3.grid(row=2)

    cf4 = newParamControlFrame("Inertia", 0, 100, onInertToggle, onInertChange)
    cf4.grid(row=3)



#labels = ["Area", "Circularity", "Convexivity", "Inertia"]

# Add all the frames to the window
buildControlPanel()

# Run the gui
window.mainloop()