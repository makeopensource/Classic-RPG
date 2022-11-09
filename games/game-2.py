import os

from crpg.parser import v1 as v1_parser


filepath = os.path.abspath("games/game-2-layout.dl")
game = v1_parser(filepath)
game.start()
