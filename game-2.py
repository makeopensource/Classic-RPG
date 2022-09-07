from crpg import generate
from game_loader import start

dl = start()
if( str(dl) != "-1"):
    game = generate(dl)
    game.start()
else:
    print("Exiting")
    exit()
