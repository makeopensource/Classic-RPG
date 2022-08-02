from crpg import Game
import locations as loc


game = Game("my custom game")

# init locations
dungeon = loc.Dungeon("The spooky dungeon")
cavern = loc.Cavern("The dangerous cavern")
castle = loc.Castle("The majestic castle")

game.add_location(dungeon, True)
game.add_location(cavern)
game.add_location(castle)

game.add_twoway_connection(dungeon, cavern)
game.add_twoway_connection(cavern, castle)
game.add_twoway_connection(dungeon, castle)

game.start()
