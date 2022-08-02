from crpg import Game
import locations as loc


game = Game("my custom game")

# init locations
starting, cavern, castle = loc.starting, loc.cavern, loc.castle

game.add_location(starting, True)
game.add_location(cavern)
game.add_location(castle)

game.add_twoway_connection(starting, cavern)
game.add_twoway_connection(cavern, castle)
game.add_twoway_connection(starting, castle)

game.start()
