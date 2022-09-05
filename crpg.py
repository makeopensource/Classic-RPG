from setup import start
import re
from builtin import Connection, BreakingConnection, Node, Location, Fight, Run, Player

# the base crpg game

class Game:
    def __init__(self, player: Player = Player(), starting_location: Location = None):
        self.current: Node = starting_location
        self.player = player
        self.name: str = None

        self.nodes: set[Node] = set()
        
        self.add_node(self.current)

    # establish nodes and connections
    def add_node(self, node: Node):
        self.nodes.add(node)

    def add_connection(self, from_node: Node, to_node: Node, connection_type: Connection = Connection):
        assert from_node in self.nodes
        assert to_node in self.nodes

        from_node.add_connection(to_node, connection_type)

    # print connections to node
    def list_next(self):
        _next = self.current.connections
        for i, node in enumerate(_next):
            print(f'{i+1}) {node}')

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

        node_mapping: dict[str, Node] = {}
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
            if "\->" in connection.group(2):
                game.add_connection(node_a, node_b, BreakingConnection)
            elif "->" in connection.group(2):
                game.add_connection(node_a, node_b)

            if "<-/" in connection.group(2):
                game.add_connection(node_b, node_a, BreakingConnection)
            elif "<-" in connection.group(2):
                game.add_connection(node_b, node_a)
           

        return game

# .dl connection cheatsheet
#
# a -> b    basic connection from a to b
# a <- b    basic connection from b to a
# a <-> b   two-way connection between a and b
# a \-> b   breaking connection from a to b
# a <-/ b   breaking connection from b to a
#
#
# compound connections
#
# a <-\-> b     basic from b to a, breaking from a to b
# a <-/-> b     basic from a to b, breaking from b to a
# a <-/\-> b    breaking connections between a and b
#
#
# abnormal syntaxes (do not use)
#
# a -><- b  two-way connection between a and b
# a \-><-/  breaking connections between a and b
# a <->\->  basic from b to a, breaking from a to b
# etc...