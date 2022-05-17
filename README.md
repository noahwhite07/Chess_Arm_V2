# Chess_Arm_V2
A rewrite of the Chess_Arm repository for controlling a robotic arm to play chess against a human autonomously 

The program runs on the [Sunfish chess engine](https://github.com/thomasahle/sunfish) written by Thomas Dybdahl Ahle
## Project Status
The program works on single-frame input from an onboard camera. It takes user input to capture an image of the board before and after a player move. It will use these images to determine the player move and feed that move to the engine. The engine move will then be displayed in the output for the player to see.

## Goals
The next step will be designing and assembling an arm, after which software can be written to handle the inverse kinematics of the arm. The engine move will then be fed into a `moveArm` function and the entire game should happen autonomusly.

In the completed version, the only user input should be physically moving the pieces and hitting a clock. 

Right now, the computer vision software is designed around an overhead camera, but ideally, the camera should be affixed to the arm and the warped image will be perspective transformed to correct for the angle.

The final goal is to have a completely self contained chess-playing robot arm. It should only be connected to wall power. It should be able to be set in front of a chessboard, calibrate itself, and play autonomously 

## Setup
The chessboard should be marked with magenta spots at the corners. This color can be toggled between a list of a few predefined colors in `board.getSquarePositions`. The color of the chessboard is not significant so long as it is not white. Otherwise, it will interfere with the detection of the white pieces. White pieces should of course, be white, but this could be changed in `board_state.getOccupiedSquares`to recognize pieces of another color.

The computer vision only tracks the white pieces, so the color of the engines pieces is not significant. The player will always play as white.

Run `cameraTest.py` to check the video feed and center the board under the camera, making sure that the corner markers are in view and well lit. Run the `board_test.py` file to check what the computer vision functions have identified as corners and pieces. Note the orientation of the board; the top left corner of the board (a8) should be in the top left corner of the image in order for the move to be interpreted correctly.

## Run It
Rewrite this later 
