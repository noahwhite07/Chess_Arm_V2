from board_manager import BoardManager
import arm_manager

class Game:
  def __init__(self):
    # self.manager = BoardManager()
    pass

  def getMove(self):
    # return self.manager.getMove()
    return input("Your move")

  def play(self, move):
    arm_manager.do(move)
    pass
