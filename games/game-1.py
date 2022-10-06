import sys
sys.path.insert(0, "../crpg")

from crpg import Game
from builtin import Location, Node

starting_location = Location("castle")
starting_location.add_attr(
    "interaction", "You find yourself in the prison cell of an abandoned castle"
)

game = Game(starting_location)

# nodes
examine_skeleton = Node("examine skeleton")
examine_skeleton.add_attr("interaction", "You examine the skeleton of a corpse.")
game.add_node(examine_skeleton)

open_cell_gate = Node("open cell gate")
open_cell_gate.add_attr("interaction", "The cell gate is unlocked. You push it open.")
game.add_node(open_cell_gate)

dungeon = Location("left corridor")
dungeon.add_attr("interaction", "The corridor leads to a large flight of stairs to the dungeon")
game.add_node(dungeon)

courtyard = Location("right corridor")
courtyard.add_attr("interaction", "The corridor leads to an open door to the castle's courtyard")
game.add_node(courtyard)

dragon_event = Node("scale stairs")
dragon_event.add_attr("interaction", "A dragon swoops down from the sky, blocking your path")
game.add_node(dragon_event)

# connections
game.add_twoway_connection(starting_location, examine_skeleton)
game.add_connection(starting_location, open_cell_gate)
game.add_connection(open_cell_gate, courtyard)
game.add_connection(open_cell_gate, dungeon)
game.add_connection(courtyard, dragon_event)

game.start()
