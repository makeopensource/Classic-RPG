from __future__ import annotations #needed for Node type hints
# Base player classes

class Player:
    def __init__(self):
        self.hp = 100
        self.xp = 0
        self.bag = []
        self.money = 0

    def summary(self):
        return f'hp: {self.hp} xp: {self.xp} money: {self.money}'

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
        return str(self.from_node) + " \-> " + str(self.to_node)


# Base node classes

class Node:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc
        self.connections: list[Connection] = []

    def on_select(self):
        print(self.desc)

    def add_connection(self, other: Node, type: Connection = Connection):
        self.connections += [type(self, other)]

    def advance(self, index: int) -> Node:
        connection = self.connections[index]
        connection.on_select()
        connection.to_node.on_select()
        return connection.to_node

    def __str__(self):
        return self.title

class Obj(Node):
    def __init__(self, title:str, desc:str, player:Player):
        super().__init__(title, desc)
        self.desc = desc
        self.player = player
        if title.isnumeric(): #initializing money
            self.amount_Money = int(title)
        elif title[:2] == "po": #if first 2 characters are po then its a potion
            if title[2:] == "health":
                self.amount_Hp = 25
                self.potionType = "Health potion"

class Potion(Obj):
    def on_select(self):
        if self in self.player.bag:
            if self.amount_Hp:
                self.player.hp += self.amount_Hp
                self.player.bag.remove(self)
        else:
            self.player.bag.append(self)
        for i in self.player.bag:
            print(i.potionType)

class Currency(Obj):
    def on_select(self):
        self.player.money += self.amount_Money
        print(self.player.summary())


# Location behaves exactly like a Node
class Location(Node):
    pass


# Actions include the player for reference (augment player attributes)
class Action(Node):
    def __init__(self, title: str, desc: str, player: Player):
        self.player = player
        super().__init__(title, desc)

    def on_select(self):
        print(self.player.summary())


class Fight(Action):
    def on_select(self):
        self.player.hp -= 25
        self.player.xp += 10

        super().on_select()


class Run(Action):
    def on_select(self):
        self.player.xp = max(self.player.xp - 10, 0)

        super().on_select()