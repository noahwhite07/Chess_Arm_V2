import cv2 as cv
# import cv2.SimpleBlobDetector_create
import numpy as np
from param_manager.params_manager import ParamManager
from param_manager.params import Params

class ComputerVision:
    def __init__(self):
        # Dictionary holding current detectors and parameter managers
        colors = ["pink", "white"]
        self.colors = { c : constructor(c) for c in colors }

    def next(self, color):
        """
        Iterate to next set of parameters and create new detector

        Arguments:
            color -- color to iterate the parameter manager for
                     "pink" or "white"
        """
        c = self.colors[color]
        c["detector"] = cv.SimpleBlobDetector_create(c["manager"].next(""))

    def save(self, color):
        """
        Save the current set of parameters as working

        Arguments:
            color -- color to save the parameters for
                     "pink" or "white"
        """
        self.colors[color]["manager"].save()

    def get_blob_points(self, img, color):
        print(self.colors)
        manager = self.colors[color]["manager"]
        bounds  = manager.colorInfo("bounds")

        boardHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        # Holds mask for color in ROYGBIV format
        colorMask = cv.inRange(boardHSV, bounds[0], bounds[1])

        # Holds the image with the color mask applied
        maskedImage = cv.bitwise_and(img, img, mask = colorMask)

        # Converts masked image to greyscale
        gray = cv.cvtColor(maskedImage, cv.COLOR_BGR2GRAY)

        # Does an inversed binary threshold of the greyscale masked image
        # Threshold is inverted because blob detector works best on black blobs on white
        threshold, blobImage = cv.threshold(gray, 55, 255, cv.THRESH_BINARY_INV)

        # A list to hold the key points given by detector.detect()
        keyPoints = self.colors[color]["detector"].detect(blobImage)

        points = [[kp.pt[0], kp.pt[1]] for kp in keyPoints]

        return points

        # Stores image of the board with the blobs of the color highlighted
        # board = cv.drawKeypoints(img, keyPoints, np.array([]), (0,255,0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # show(board)

    def get_occupied_squares(self):
        """
        Get next set of parameters from switcher
        """
        print("NOT IMPLEMENTED")

        # Should take a picture with camera
        # img = None
        img = cv.imread("test/test_image.png")

        # find image corners
        corners = self.get_blob_points(img, "pink")
        while len(corners) != 4:
            self.next("pink")
            corners = self.get_blob_points(img, "pink")
        self.save("pink")
        pass

    def find_chessboard(self, frame):
        chessboard_flags = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_FAST_CHECK + cv.CALIB_CB_NORMALIZE_IMAGE
        small_frame = cv.resize(frame, (0, 0), fx=0.3, fy=0.3)
        return (cv.findChessboardCorners(small_frame, (7, 7), chessboard_flags)[0],
               cv.findChessboardCorners(frame, (7, 7), chessboard_flags)[0])


def default_color_bounds():
    return {
        "white": [np.array([0,0,160]), np.array([255,25,255])],
        "pink" : [np.array([140,40,40]), np.array([169,255,255])],
    }

def constructor(color):
    """
    Creates a dictionary holding a param manager and a blob detector
    for a given color

    Arguments:
        color -- color to create the parameter manager for
                 "pink" or "white"
    """
    manager = ParamManager()

    return {
        "manager": manager,
        "detector": cv.SimpleBlobDetector_create(manager.current())
    }

def show(img):
    cv.imshow("test", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
