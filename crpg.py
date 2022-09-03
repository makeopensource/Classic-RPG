from builtin import Player, Location, Event, Fight, Run

# the base crpg game

class Game:
    def __init__(self):
        self.current = Location(self, 'castle')
        self.player = Player('Emil')

    def ask(self, query):
        if self.current.children:
            while True:
                self.current.list_children()
                try:
                    choice = int(input(f'{query}'))
                except ValueError:
                    print('Please enter a number. Try again.')
                    continue
                
                break

            self.current = self.current.children[choice - 1]
            self.current.after()
        else:
            print('no options')

    def start(self):
        print(f'Welcome {self.player}')
        while self.current.children and self.player.hp > 0:
            self.ask('> ')

        print('GAME OVER')


game = Game()

# Locations
castle = Location(game, 'castle')
game.current = castle

dungeon = Location(game, 'dungeon', 'Enter Dungeon')
woods = Location(game, 'woods', 'Enter woods')

# Events
dragon_event = Event(game, 'Mysterious Tunnel', 'A gigantic dragon appears')
enter_dungeon = Event(game, 'Dark corridor', 'You follow stairs into a dungeon')

# Actions
fight_dragon = Fight(game, 'Fight dragon', 2)
run_from_dragon = Run(game, 'Run from dragon', 2)

# set connections
game.current.add_children([dragon_event, enter_dungeon])
enter_dungeon.add_child(dungeon)

dragon_event.add_children([fight_dragon, run_from_dragon])

game.start()
