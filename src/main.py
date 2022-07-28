from threading import Thread
from queue import Queue

# create sunfish instance
import sunfish as sf
to_engine, from_engine = Queue(), Queue()
sunfish = Thread(target = sf.start, args = (to_engine, from_engine, ))

sunfish.start()

# create Game instance
from game import Game
game = Game()

# while the engine is still accepting moves
# feed it the move by white
while sunfish.is_alive():
    # get white's move
    move = game.getMove()
    # feed it to sunfish
    to_engine.put(move)
    # get black's move
    toPlay = from_engine.get()
    # feed it to the arm
    print(toPlay)
    game.play(toPlay)
