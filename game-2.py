from crpg import generate
from game_loader import selectDL

dl = selectDL()
if( str(dl) != "-1"):
    game = generate(dl)
    game.start()
else:
    print("Exiting")
    exit()
