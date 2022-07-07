from cv2 import SimpleBlobDetector_Params as Params

class ParamSwitcher:
    def __init__(self):
        # TODO: implement default parameters
        self.detector  = None
        self.current   = default_params()
        self.colorInfo = default_color_info()

    # def current(self):
        # """
        # Get current parameters
        # """
        # return self.current

    def next(self, info):
        """
        Compute new parameters

        Arguments:
            info -- error information from blob detection to better compute
                    next set of parameters (unused for now). schema TBD
        """
        print("NOT IMPLEMENTED")
        return self.current


def default_params():
	params = Params()
	params.filterByArea = True
	params.filterByCircularity = False
	params.filterByColor = False
	params.filterByConvexity = False
	params.filterByInertia = False
	params.maxArea = 600
	params.maxCircularity = 1.0
	params.maxConvexity = 1.0
	params.maxInertiaRatio = 1.0
	params.maxThreshold = 200
	params.minArea = 10
	params.minCircularity = 0.1
	params.minConvexity = 0.87
	params.minDistBetweenBlobs = 1.0
	params.minInertiaRatio = 0.01
	params.minThreshold = 50
	
def default_color_info():
	return {
		"bounds": [120, 255]
	}