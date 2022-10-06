from crpg import Game
from typing import Callable # for connection function type hints
import re
from builtin import Connection, BreakingConnection, Node, Location 


n_types = {
    "starting": Location,
    "node": Node,
    "location": Location,
}


builtin_args = [
    'interaction',
    'health',
    'xp',
    'coins'
]


c_funcs: dict[str, Callable[[Game, Node, Node], None]] = {
    "->": lambda game, node_a, node_b: game.add_connection(node_a, node_b),
    "\\->": lambda game, node_a, node_b: game.add_connection(node_a, node_b, BreakingConnection),
    "<->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b),
    "<\\->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b, BreakingConnection),
    "<-/->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b, Connection, BreakingConnection),
    "<-/\\->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b, BreakingConnection, BreakingConnection),
}


# parses all individual nodes of the graph
def parse_nodes(chunks, game):
    node_mapping: dict[str, Node] = {}
    starting: Location = Location("Castle")
    for chunk in chunks.split("\n"):
        n_alias, n_type, title, args = re.split(r"\s*\|\s*", chunk)
        kwargs = args_to_kwargs(args) 
        obj = n_types[n_type](title, **kwargs)
        if n_type == "starting":
            starting = obj

        node_mapping[n_alias] = obj
        game.add_node(obj)

    return starting, node_mapping


def args_to_kwargs(args):
    print(args)
    if type(args) == str:
        args = [args]
    if len(args) > len(builtin_args):
        raise ValueError("Invalid number of arguments")
    retval = {}
    for i, elem in enumerate(args):
        retval[builtin_args[i]] = elem
    return retval


def parse_connections(chunks, node_mapping, game):
    for connection in chunks.strip("\n").split("\n"):
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


def generate(filename):
    with open(filename, "r") as f:
        contents = f.read()
        nodes, connections = contents.split("\n+---\n+", maxsplit=1) 

        game = Game()
        starting, node_mapping = parse_nodes(nodes, game)
        game.current = starting
        parse_connections(connections, node_mapping, game)
        
        return game
