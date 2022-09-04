from setup import start
import re
from builtin import Node, Location, Fight, Run, Player

# the base crpg game

class Game:
    def __init__(self, player: Player = Player(), starting_location: Location = None):
        self.current = starting_location
        self.player = player
        self.name: str = None

        self.nodes: set[Node] = set()
        self.connections: dict[Node, list[Node]] = {}
        
        self.add_node(self.current)

    # establish nodes and connections

    def add_node(self, node: Node):
        self.nodes.add(node)

    def add_oneway_connection(self, node_a: Node, node_b: Node):
        assert node_a in self.nodes
        assert node_b in self.nodes

        # adding node_a to list of connections
        self.connections[node_a] = self.connections.get(node_a, []) + [node_b]

    def add_twoway_connection(self, node_a: Node, node_b: Node):
        self.add_oneway_connection(node_a, node_b)
        self.add_oneway_connection(node_b, node_a) 

    # print connections to node
    def list_next(self):
        _next = self.connections[self.current]
        for i, node in enumerate(_next):
            print(f'{i+1}) {node}')

    # Iterate through graph, ask for choices at each node
    def ask(self, query: str):
        if self.current not in self.connections:
            print("Exhausted all options...")
            exit(0)

        _next = self.connections[self.current]
        if len(_next) > 0: 
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
        self.name = start()
        print(f'Welcome, {self.name}')

        while self.player.hp > 0:
            self.ask('> ')

        print("GAME OVER")


def generate(filename):
    with open(filename, "r") as f:
        contents = f.read()
        nodes, connections = contents.split("\n---\n", maxsplit=1)

        game = Game()

        node_mapping = {}
        n_types = {
            "starting": Location,
            "node": Node,
            "location": Location,
            "fight": Fight,
            "run": Run
        }

        for node in nodes.split("\n"):
            n, n_type, *args = re.split(r"\s*\|\s*", node)

            if n_type == "fight" or n_type == "run":
                args.append(game.player)

            obj = n_types[n_type](*args)
            if n_type == "starting":
                game.current = obj

            game.add_node(obj)
            node_mapping[n] = obj

        for connection in connections.strip("\n").split("\n"):
            connection = re.match(r"^(\d*)\s*([^\s]*)\s*(\d*)$", connection, re.MULTILINE)
            node_a = node_mapping[connection.group(1)]
            node_b = node_mapping[connection.group(3)]
            if connection.group(2) == "<->":
                game.add_twoway_connection(node_a, node_b)
            elif connection.group(2) == "->":
                game.add_oneway_connection(node_a, node_b)

        return game

