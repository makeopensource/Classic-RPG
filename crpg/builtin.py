from __future__ import annotations #needed for Node type hints
# Base player classes

class Player:
    def __init__(self):
        self.hp = 100
        self.xp = 0

    def summary(self):
        return f'hp: {self.hp} xp: {self.xp}'


# Base connection classes

class BaseConnection:
    def __init__(self, from_node: Node, to_node: Node):
        self.from_node = from_node
        self.to_node = to_node

    def on_select(self):
        pass

class Connection(BaseConnection):
    def __str__(self):
        return str(self.from_node) + " -> " + str(self.to_node)


# Breaking connections can only be used once
class BreakingConnection(BaseConnection):        
    def on_select(self):
        self.from_node.connections.remove(self)

    def __str__(self):
        return f"{self.from_node} \\-> {self.to_node}"


# Base node classes
class Node:
    def __init__(self, title: str, **kwargs):
        self.title = title
        self.attrs: dict[str, str] = kwargs
        self.connections: list[BaseConnection] = []

    def on_select(self):
        print(self.attrs["interaction"])

    def add_connection(self, other: Node, conn: type = BaseConnection):
        self.connections += [conn(self, other)]

    def advance(self, index: int) -> Node:
        connection = self.connections[index]
        connection.on_select()
        connection.to_node.on_select()
        return connection.to_node
    
    def add_attr(self, key, value):
        self.attrs[key] = value

    def __str__(self):
        return self.title


# Location behaves exactly like a Node
class Location(Node):
    pass


# Actions include the player for reference (augment player attributes)
class Action(Node):
    def __init__(self, title: str, player: Player):
        self.player = player
        super().__init__(title)

    def on_select(self):
        print(self.player.summary())

