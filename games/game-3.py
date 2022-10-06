import sys
sys.path.insert(0, "../crpg")

import parser

game = parser.v2("game-3.dl")
game.start()
