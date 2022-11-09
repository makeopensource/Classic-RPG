import os

from crpg.parser import v2 as v2_parser


filepath = os.path.abspath("games/game-2-layout.dl")
game = v2_parser(filepath)
game.start()
