import sys
sys.path.insert(0, "../crpg")

from crpg import generate

game = generate("game-2-layout.dl")
game.start()
