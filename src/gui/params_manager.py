# A module for reading and writing to the params.json file
import json
import os


# Give these logical default values
params = None
params_file = None
path = None

# Load the parameters from params.json into the params dictionary 
def load_from_json():   
    global params
    global params_file
    global path
    # Generate path of params file (assumes params.json in same dir as script)
    path = os.path.dirname(__file__) + "/params.json"

    # Open the JSON file for reading
    params_file = open(path, mode= "r")

    # Convert JSON to dictionary
    params = json.load(params_file)


    # Close the file
    params_file.close()


# Writes params.json with the contents of the given dictionary
def write_to_json():
    global params
    global params_file
    global path
    # Open the JSON file for writing
    params_file = open(path, mode= "w")

    # Overwrite the existing JSON file with modified data
    params_file.write(json.dumps(params))

    # Close the file
    params_file.close()


#################################################################################

# Set parameter filters

def set_area_filter(filter):
    """Set filterByArea parameter of cv.SimpleBlobDetector

    Arguments:
        filter -- a boolean to set the filter on or off
    """    
    global params
    params["area"][0] = filter

def toggle_area_filter():
    global params
    params["area"][0] = not params["area"][0]

def set_circularity_filter(filter):
    """Set filterByCircularity parameter of cv.SimpleBlobDetector

    Arguments:
        filter -- a boolean to set the filter on or off
    """
    global params
    params["circularity"][0] = filter

# Set parameter filters
def toggle_circularity_filter():
    global params
    params["circularity"][0] = not params["circularity"][0]

def set_convexivity_filter(filter):
    """Set filterByConvexivity parameter of cv.SimpleBlobDetector

    Arguments:
        filter -- a boolean to set the filter on or off
    """
    global params
    params["convexivity"][0] = filter

def toggle_convexivity_filter():
    global params
    params["convexivity"][0] = not params["convexivity"][0]

def set_inertia_filter(filter):
    """Set filterByInertia parameter of cv.SimpleBlobDetector

    Arguments:
        filter -- a boolean to set the filter on or off
    """
    global params
    params["inertia"][0] = filter

def toggle_inertia_filter():
    global params
    params["inertia"][0] = not params["inertia"][0]

def set_area_value(value):
    """Set minArea parameter of cv.SimpleBlobDetector

    Arguments:
        value -- integer representing minimum area of a blob to be detected
    """
    global params
    params["area"][1] = value

def set_circularity_value(value):
    """Set minCircularity parameter of cv.SimpleBlobDetector

    Arguments:
        value -- float representing minimum circularity of a blob to be detected in range [0,1]
    """
    global params
    params["circularity"][1] = value

def set_convexivity_value(value):
    """Set minConvexivity parameter of cv.SimpleBlobDetector

    Arguments:
        value -- float representing minimum convexivity of a blob to be detected in range [0,1]
    """
    global params
    params["convexivity"][1] = value

def set_inertia_value(value):
    """Set minInertia parameter of cv.SimpleBlobDetector

    Arguments:
        value -- float representing minimum inertia of a blob to be detected in range [0,1]
    """
    global params
    params["inertia"][1] = value

# Set color bounds

def set_corner_bounds(bounds):
    global params
    params["colorBounds"]["corner"] = bounds

def set_piece_bounds(bounds):
    global params
    params["colorBounds"]["piece"] = bounds

def set_corner_bounds_low(lower_bound):
    global params
    params["colorBounds"]["corner"][0] = lower_bound
    
def set_corner_bounds_high(upper_bound):
    global params
    params["colorBounds"]["corner"][1] = upper_bound 
 
def set_piece_bounds_low(lower_bound):
    global params
    params["colorBounds"]["piece"][0] = lower_bound
    thing = params["colorBounds"]["piece"][0]
    print(f"lower bound: {thing}")

def set_piece_bounds_high(upper_bound):
    global params
    params["colorBounds"]["piece"][1] = upper_bound 

    thing = params["colorBounds"]["piece"][1]
    print(f"upper bound: {thing}")

#################################################################################

# Get parameter filters

def get_area_filter():
    global params
    return params["area"][0]
     
def get_circularity_filter():
    global params
    return params["circularity"][0]
     
def get_convexivity_filter():
    global params
    return params["convexivity"][0]
     
def get_inertia_filter():
    global params
    return params["inertia"][0]
    
# Get parameter values

def get_area_value():
    global params
    return params["area"][1]

def get_circularity_value():
    global params
    return params["circularity"][1]

def get_convexivity_value():
    global params
    return params["convexivity"][1]    

def get_inertia_value():
    global params
    return params["inertia"][1]

# Get color bounds 

def get_corner_bounds():
    global params
    return params["colorBounds"]["corner"]

def get_piece_bounds():
    global params
    return params["colorBounds"]["piece"] 

def get_corner_bounds_low():
    global params
    return params["colorBounds"]["corner"][0]
    
def get_corner_bounds_high():
    global params
    return params["colorBounds"]["corner"][1] 
 
def get_piece_bounds_low():
    global params
    return params["colorBounds"]["piece"][0] 

def get_piece_bounds_high():
    global params
    return params["colorBounds"]["piece"][1] 