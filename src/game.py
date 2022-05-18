from board_manager import BoardManager
import arm_manager

class Game:
  def __init__(self):
    self.manager = BoardManager()

  def sendToEngine(self):
    self.manager.getNewState()
    return self.manager.getMove()

  def receiveFromEngine(self, move):
    arm_manager.do(move)
    pass
