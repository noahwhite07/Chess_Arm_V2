import cv2 as cv
import numpy as np

#incredibly lazy global variable for testing
keyPointsList = []

class ComputerVision:
    def __init__(self):
        self.params   = defaultBlobParameters()
        self.bounds   = defaultColorBounds()
        self.detector = cv.SimpleBlobDetector_create(self.params)

    def initialize(self):
        pass

    def getBlobPoints(self, img, color):
        boardHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        # holds mask for color in ROYGBIV format
        colorMask = cv.inRange(boardHSV, self.bounds[color][0], self.bounds[color][1])

        # holds the image with the color mask applied
        maskedImage = cv.bitwise_and(img, img, mask = colorMask)

        # converts masked image to greyscale
        gray = cv.cvtColor(maskedImage, cv.COLOR_BGR2GRAY)

        # does an inversed binary threshold of the greyscale masked image
        # threshold is inverted because blob detector works best on black blobs on white
        threshold, blobImage = cv.threshold(gray, 55, 255, cv.THRESH_BINARY_INV)

        # A list to hold the key points given by detector.detect()
        keyPoints = self.detector.detect(blobImage)

        points = [[kp.pt[0], kp.pt[1]] for kp in keyPoints]

        return points

        # stores image of the board with the blobs of the color highlighted
        # board = cv.drawKeypoints(img, keyPoints, np.array([]), (0,255,0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        # show(board)



    def drawBlobPoints(self, boardImg, color):
        boardsWithKeypoints = []

        for keyPoints in keyPointsList:
            boardsWithKeypoints.append(cv.drawKeypoints(boardImg, keyPoints, np.array([]), (0,0,0), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS))
            points = []

        cv.imshow(f'keypoints of color {color}',boardsWithKeypoints[color])

    def getOccupiedPoints(self, img, color):
        blobPoints = self.getBlobPoints(img, color)
        print(blobPoints)
        print("Not implemented")
        pass

    def find_chessboard(self, frame):
        chessboard_flags = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_FAST_CHECK + cv.CALIB_CB_NORMALIZE_IMAGE
        small_frame = cv.resize(frame, (0, 0), fx=0.3, fy=0.3)
        return (cv.findChessboardCorners(small_frame, (7, 7), chessboard_flags)[0],
               cv.findChessboardCorners(frame, (7, 7), chessboard_flags)[0])


def defaultColorBounds():
    return {
        "white": [np.array([0,0,160]), np.array([255,25,255])],
        "pink" : [np.array([140,40,40]), np.array([169,255,255])],
    }

def defaultBlobParameters():
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


def show(img):
    cv.imshow("test", blobPost)
    cv.waitKey(0)
    cv.destroyAllWindows()
