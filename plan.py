# 1. Engine requests a move
# 2. Person hits clock
# 3. Take a picture 
# 4. Create board state with picture
# 5. Compute move made by white
# 6. Feed move to engine
# 7. Feed engine move to arm
# loop

# main.py
import sunfish
import Game from game

game = Game()
sunfish.start(game)

# sunfish.py
def start(game):
  while True:
    whiteMove = game.sendToEngine()
    # Engine computes 
    game.receiveFromEngine(blackMove)

# game.py
import BoardManager from board_manager
import arm_manager

class Game:
  def __init__():
    this.manager = BoardManager()

  def sendToEngine(self):
    self.manager.getNewState()
    return self.manager.getMove()

  def receiveFromEngine(self, move):
    arm_manager.do(move)
    
# board_manager.py
import computer_vision as CV

class BoardManager:
  def __init__():
    state = CV.getOccupiedPoints()
    this.states = [state, state]
  
  def getMove(self, selfSquares):
    prevSet = set(self.state[0])
    currSet = set(self.state[1])
    initSquare = list(prevSet - currSet)
    finalSquare = list(currSet - prevSet)
    return (initSquare[0] + finalSquare[0])
  
  # Take image to determine current boardstate 
  def getNewState(self):
    while clockNotHit
      wait()

    state = CV.getOccupiedPoints()
    # shifts board states to the left
    self.states = [self.state[1], state]
    # [prev state, curr state]

# computer_vision.py
import opencv as cv

def getOccupiedPoints():
  img = cv.VideoCapture(0)
  # cv stuff
  return ['a1','b2',...]
