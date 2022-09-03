from crpg import Game
from builtin import Player, Location, Action, Node

player = Player()
starting_location = Location(
    "castle", 
    "You wake up in the prison cell of an abandoned castle"
)

game = Game(player, starting_location)

# nodes
examine_skeleton = Node("examine skeleton", "You examine the skeleton of a corpse.")
game.add_node(examine_skeleton)

open_cell_gate = Node("open cell gate", "The cell gate is unlocked. You push it open.")
game.add_node(open_cell_gate)

dungeon = Location("left corridor", "The corridor leads to a large flight of stairs to the dungeon")
game.add_node(dungeon)

courtyard = Location("right corridor", "The corridor leads to an open door to the castle's courtyard")
game.add_node(courtyard)

# connections
game.add_twoway_connection(starting_location, examine_skeleton)
game.add_oneway_connection(starting_location, open_cell_gate)
game.add_oneway_connection(open_cell_gate, courtyard)
game.add_oneway_connection(open_cell_gate, dungeon)

game.start()
