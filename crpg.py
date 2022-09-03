from setup import start
import os

# the base crpg game

class Game:
    def __init__(self, player, starting_location):
        self.current = starting_location
        starting_location.on_select()
        self.player = player

        self.nodes = set()
        self.connections = {}

        self.add_node(starting_location)

    def add_node(self, node):
        self.nodes.add(node)

    def add_oneway_connection(self, node_a, node_b):
        assert node_a in self.nodes
        assert node_b in self.nodes

        # adding node_a to list of connections
        self.connections[node_a] = self.connections.get(node_a, []) + [node_b]

    def add_twoway_connection(self, node_a, node_b):
        self.add_oneway_connection(node_a, node_b)
        self.add_oneway_connection(node_b, node_a) 

    def list_next(self):
        _next = self.connections[self.current]
        for i, node in enumerate(_next):
            print(f'{i+1}) {node}')

    def ask(self, query):
        if self.current not in self.connections:
            print("Exhausted all options...")
            exit(0)

        _next = self.connections[self.current]
        if len(_next) == 1:
            self.current = _next[0] 

        elif len(_next) > 1: 
            while True:
                self.list_next()
                try:
                    choice = int(input(f'{query}'))
                except ValueError:
                    print('Please enter a number. Try again.')
                    continue 
                break

            self.current = _next[choice - 1]
            self.current.on_select()

        else:
            print('Dead end')

    def start(self):
        name = start()
        self.player.name = name
       
        os.system("clear")
        print(f'Welcome, {self.player}')
        while self.player.hp > 0:
            self.ask('> ')

        print("GAME OVER")


