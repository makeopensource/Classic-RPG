from typing import Callable, Any # for connection function type hints
import re

from crpg.engine import Game
from crpg.builtin import Connection, BreakingConnection, Node, Location


# connection function mapping
connection_funcs: dict[str, Callable[[Game, Node, Node], None]] = {
    "->": lambda game, node_a, node_b: game.add_connection(node_a, node_b),
    "\\->": lambda game, node_a, node_b: game.add_connection(node_a, node_b, BreakingConnection),
    "<->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b),
    "<-\\->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b, BreakingConnection),
    "<-/->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b, Connection, BreakingConnection),
    "<-/\\->": lambda game, node_a, node_b: game.add_twoway_connection(node_a, node_b, BreakingConnection, BreakingConnection),
}

# node type mapping
node_types = {
    "starting": Location,
    "node": Node,
    "location": Location
}

# check if an attr is a number
def is_number(attr) -> bool:
    return attr[0] == "+" or attr[0] == "-"

# convert an attr into a number (assumes is_number)
def to_number(attr) -> int:
    try:
        n = int(attr[1:])
    except:
        raise ValueError(f"{attr} is not a number")

    if attr[0] == "-":
        n *= -1
    return n


# parse each node chunk into relevant pieces
def parse_node(chunk) -> tuple[str, str, dict[str, Any]]:
    split_chunk: list[str] = chunk.split("\n")
    header, attrs = split_chunk[0], split_chunk[1:]

    node_info = re.split(r"\s*\|\s*", header, maxsplit=1)
    if len(node_info) != 2:
        raise ValueError("Each node must include a \"node id\" and \"node name\"")

    node_id: str = node_info[0]
    node_name: str = node_info[1]
    attr_map: dict[str, Any] = {}
   
    # parse attributes into mapping
    for attr in attrs:
        attr_name, attr_val = re.split(r":\s*", attr, maxsplit=1)
        if is_number(attr_val):
            attr_val = to_number(attr_val)

        attr_map[attr_name] = attr_val

    return (node_id, node_name, attr_map)


def parse_connection(chunk) -> tuple[str, str, str]:
    connection = re.match(r"^\s*(\d+)\s+([^\s]+)\s+(\d+)\s*$", chunk, re.MULTILINE)

    if connection is None or '' in connection.groups():
        raise ConnectionError("Invalid .dl connection input")

    return connection.group(1, 2, 3)


# setup nodes for game
def node_setup(nodes, game) -> dict[str, Node]:
    node_mapping: dict[str, Node] = {}

    for node in nodes:
        # split data for each node
        node_id, node_name, attr_map = parse_node(node)

        # retrieve the node type
        node_type: str = str(attr_map["node_type"])

        # generate the appropriate node object
        # attributes MUST be compliant with kwarg-syntax 
        obj: Node = node_types[node_type](node_name, **attr_map)

        if node_type == "starting":
            game.current = obj

        # add the node to the game
        game.add_node(obj)

        # generate the nodes
        node_mapping[node_id] = obj

    return node_mapping


# setup connections for game
def connection_setup(connection, node_mapping, game):
    for raw_connection in connection:
        node_a_id, node_connection, node_b_id = parse_connection(raw_connection)

        node_a = node_mapping[node_a_id]
        node_b = node_mapping[node_b_id]

        connection_func = connection_funcs.get(node_connection, None)
        if not connection_func:
            raise ConnectionError("Invalid .dl connection input")

        connection_func(game, node_a, node_b)


# setup game with nodes and connections
def setup(nodes, connection, game):
    node_mapping: dict[str, Node] = node_setup(nodes, game)
    connection_setup(connection, node_mapping, game)


def generate(filename):
    with open(filename, "r") as f:
        contents = f.read()

    try:
        meta, nodes, connection = re.split(r"\n+---\n+", contents, re.DOTALL)
    except:
        raise ValueError("Please separate each section with \"---\"")

    meta = re.split("\n*", meta)
    nodes = re.split("\n\n+", nodes)
    connection = [x for x in re.split("\n+", connection) if x != '']
    game = Game()
    setup(nodes, connection, game)
    
    return game
