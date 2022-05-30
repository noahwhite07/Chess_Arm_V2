import time
from computer_vision import ComputerVision

class BoardManager:
  def __init__(self):
    self.cv     = ComputerVision()
    self.cv.initialize()
    state       = self.cv.get_occupied_squares()
    self.states = [state, state]
    self.states = [['a2','a3','c3'], ['a2','a3','b4']]

  def get_move(self):
    prevSet = set(self.states[0])
    currSet = set(self.states[1])
    initSquare = list(prevSet - currSet)
    finalSquare = list(currSet - prevSet)
    return (initSquare[0] + finalSquare[0])

  # Take image to determine current boardstate
  def get_new_state(self):
    self.get_move()
    # input()
    # state = CV.getOccupiedPoints()
    # shifts board states to the left
    # self.states = [self.state[1], state]

    state = CV.test_fn()
