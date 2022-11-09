from .setup import start
from .builtin import Connection, Node, Location, Player

# the base crpg game

class Game:
    def __init__(self, starting: Location = Location("Castle"), player: Player = Player()):
        self.current: Node = starting
        self.player: Player = player
        self.name: str
        self.nodes: set[Node] = set()
        self.add_node(starting)
 
    # establish nodes and connections
    def add_node(self, node: Node):
        self.nodes.add(node)

    def add_connection(self, 
        from_node: Node, 
        to_node: Node,
        connection_type: type = Connection
    ):
        assert from_node in self.nodes
        assert to_node in self.nodes

        from_node.add_connection(to_node, connection_type)

    def add_twoway_connection(self, 
        node_a: Node, 
        node_b: Node, 
        connection_type_a: type = Connection, 
        connection_type_b: type = Connection
    ):
        assert node_a in self.nodes
        assert node_b in self.nodes

        node_a.add_connection(node_b, connection_type_a)
        node_b.add_connection(node_a, connection_type_b)

    # print connections to node
    def list_next(self):
        assert self.current

        _next = self.current.connections
        for i, connection in enumerate(_next):
            print(f'{i+1}) {connection.to_node}')

    # Iterate through graph, ask for choices at each node
    def ask(self, query: str):
        assert self.current

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

