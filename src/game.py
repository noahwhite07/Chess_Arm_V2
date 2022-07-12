from board_manager import BoardManager
import arm_manager

class Game:
  def __init__(self):
    self.manager = BoardManager()

  def send_to_engine(self):
    return self.manager.getMove()

  def receive_from_engine(self, move):
    arm_manager.do(move)
    pass
