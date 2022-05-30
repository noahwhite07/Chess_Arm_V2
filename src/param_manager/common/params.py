def default_color_bounds():
    return {
        "white": [np.array([0,0,160]), np.array([255,25,255])],
        "pink" : [np.array([140,40,40]), np.array([169,255,255])],
    }

def default_blob_parameters():
    params = cv.SimpleBlobDetector_Params()

    params.minThreshold = 50
    params.maxThreshold = 200
    params.filterByArea = True
    params.minArea = 10
    params.filterByCircularity = False
    params.minCircularity = 0.1
    params.filterByConvexity = False
    params.minConvexity = 0.87
    params.filterByInertia = False
    params.minInertiaRatio = 0.01

    return params
