import sys

sys.path.insert(0, "../crpg")

from crpg import Game
from builtin import Player, Location, Node, Fight, Run

player = Player()
starting_location = Location(
    "castle", 
    "You find yourself in the prison cell of an abandoned castle"
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

dragon_event = Node("scale stairs", "A dragon swoops down from the sky, blocking your path")
game.add_node(dragon_event)

fight_dragon = Fight("fight dragon", "You vanquish the dragon", player)
game.add_node(fight_dragon)

run_dragon = Run("run", "You run from the dragon", player)
game.add_node(run_dragon)

# connections
game.add_twoway_connection(starting_location, examine_skeleton)
game.add_connection(starting_location, open_cell_gate)
game.add_connection(open_cell_gate, courtyard)
game.add_connection(open_cell_gate, dungeon)
game.add_connection(courtyard, dragon_event)
game.add_connection(dragon_event, fight_dragon)
game.add_connection(dragon_event, run_dragon)

game.add_connection(fight_dragon, courtyard)
game.add_connection(run_dragon, courtyard)

game.start()
