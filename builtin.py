from __future__ import annotations  # needed for Node type hints


# Base player classes

class Player:
    def __init__(self):
        self.hp = 100
        self.xp = 0
        self.coins_earned = 0

    def summary(self):
        return f'hp: {self.hp} xp: {self.xp} coins: {self.coins_earned}'


# Base connection classes

class Connection:
    def __init__(self, from_node: Node, to_node: Node):
        self.from_node = from_node
        self.to_node = to_node

    def on_select(self):
        pass

    def __str__(self):
        return str(self.from_node) + " -> " + str(self.to_node)


# Breaking connections can only be used once
class BreakingConnection(Connection):
    def __init__(self, from_node: Node, to_node: Node):
        super().__init__(from_node, to_node)

    def on_select(self):
        self.from_node.connections.remove(self)

    def __str__(self):
        return str(self.from_node) + " \\-> " + str(self.to_node)


# Base node classes

class Node:
    def __init__(self, title: str, desc: str, coins: str):
        super().__init__()
        self.title = title
        self.desc = desc
        self.coins = int(coins)
        # self.player = player
        self.connections: list[Connection] = []

    def on_select(self):
        print(self.desc)
        # self.player.coins_earned += self.coins

    def add_connection(self, other: Node, type: Connection = Connection):
        self.connections += [type(self, other)]

    def advance(self, index: int) -> Node:
        connection = self.connections[index]
        connection.on_select()
        connection.to_node.on_select()
        return connection.to_node

    def __str__(self):
        return self.title


# Location behaves exactly like a Node
class Location(Node):
    pass


# Actions include the player for reference (augment player attributes)
class Action(Node):
    def __init__(self, title: str, desc: str, coins: str, player: Player):
        self.player = player
        super().__init__(title, desc, coins)

    def on_select(self):
        print(self.player.summary())
        self.player.coins_earned += self.coins
        super(Action, self).on_select()


class Fight(Action):
    def on_select(self):
        self.player.hp -= 25
        self.player.xp += 10
        self.player.coins_earned += 50

        super().on_select()


class Run(Action):
    def on_select(self):
        self.player.coins_earned += 10
        self.player.xp = max(self.player.xp - 10, 0)

        super().on_select()
