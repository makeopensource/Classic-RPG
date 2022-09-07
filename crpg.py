from typing import Callable # for connection function type hints
from setup import start
import re
from builtin import Connection, BreakingConnection, Node, Location, Fight, Run, Player
# the base crpg game

class Game:
    def __init__(self, gameTitle,  player: Player = Player(), starting_location: Location = None):
        self.current: Node = starting_location
        self.player = player
        self.name: str = None
        self.gameTitle = gameTitle
        self.nodes: set[Node] = set()
        
        self.add_node(self.current)

    # establish nodes and connections
    def add_node(self, node: Node):
        self.nodes.add(node)

    def add_connection(self, from_node: Node, to_node: Node, connection_type: Connection = Connection):
        assert from_node in self.nodes
        assert to_node in self.nodes

        from_node.add_connection(to_node, connection_type)

    def add_twoway_connection(self, node_a: Node, node_b: Node, connection_type_a: Connection = Connection, connection_type_b: Connection = Connection):
        assert node_a in self.nodes
        assert node_b in self.nodes

        node_a.add_connection(node_b, connection_type_a)
        node_b.add_connection(node_a, connection_type_b)

    # print connections to node
    def list_next(self):
        _next = self.current.connections
        for i, connection in enumerate(_next):
            print(f'{i+1}) {connection.to_node}')

    # Iterate through graph, ask for choices at each node
    def ask(self, query: str):
        if len(self.current.connections) == 0:
            print("Exhausted all options...")
            exit(0)

        _next = self.current.connections
        while True:
            self.list_next()
            try:
                choice = int(input(f'{query}'))
            except ValueError:
                print('Please enter a number. Try again.')
                continue 

            # check for valid choice
            if (choice <= len(_next) and choice > 0):
                break
            else:
                print('Please enter a valid number. Try again.')
        self.current = self.current.advance(choice - 1)

    def start(self):
        self.name = start(self.gameTitle)
        print(f'Welcome, {self.name}')

        while self.player.hp > 0:
            self.ask('> ')

        print("GAME OVER")


def generate(filename):
    with open(filename, "r") as f:
        contents = f.read()
        nodes, connections = contents.split("\n---\n", maxsplit=1)

        if(filename.find('/')!=-1):
            game = Game(filename[filename.find('/')+1:-3])
        else:
            game = Game(filename[:-3])

        node_mapping: dict[str, Node] = {}
        n_types = {
            "starting": Location,
            "node": Node,
            "location": Location,
            "fight": Fight,
            "run": Run
        }

        c_funcs: dict[str, Callable[[Game, Node, Node], None]] = {
            "->": lambda game, node_a, node_b: game.add_connection(node_a, node_b),
            "\->": lambda game, node_a, node_b: game.add_connection(node_a, node_b, BreakingConnection),
            "<->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b),
            "<-\->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b, BreakingConnection),
            "<-/->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b, Connection, BreakingConnection),
            "<-/\->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b, BreakingConnection, BreakingConnection),
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
            connection = re.match(r"^(\d*)\s*([^\s]*)\s*(\d*)\s*$", connection, re.MULTILINE)

            if connection is None or '' in connection.groups():
                raise ConnectionError("Invalid .dl connection input")

            node_a = node_mapping[connection.group(1)]
            node_b = node_mapping[connection.group(3)]

            c_func = c_funcs.get(connection.group(2))
            if c_func is not None:
                c_func(game, node_a, node_b)
            else:
                raise ConnectionError("Invalid .dl connection input")

        return game