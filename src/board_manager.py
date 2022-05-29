import time
from computer_vision import ComputerVision

class BoardManager:
  def __init__(self):
    self.cv     = ComputerVision()
    self.cv.initialize()
    state       = self.cv.getOccupiedPoints()
    self.states = [state, state]
    self.states = [['a2','a3','c3'], ['a2','a3','b4']]

  def getMove(self):
    prevSet = set(self.states[0])
    currSet = set(self.states[1])
    initSquare = list(prevSet - currSet)
    finalSquare = list(currSet - prevSet)
    return (initSquare[0] + finalSquare[0])

  # Take image to determine current boardstate
  def getNewState(self):
    # input()
    # state = CV.getOccupiedPoints()
    # shifts board states to the left
    # self.states = [self.state[1], state]

    state = CV.testFn()
