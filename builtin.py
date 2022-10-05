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

#To initialize another potion type, create another if statement in init. Define what happens on select in on_select. 
class Potion(Node):
    def __init__(self, title:str, desc:str, player:Player):
        super().__init__(title, desc)
        self.desc = desc
        self.player = player
        if "health" in title:
            Health.init_health(self,title)
        if "speed" in title:
            Speed.init_speed(self,title)

    def on_select(self):
        self.player.bag.append(self)
        showBag(self)

class Health():
    def init_health(self,title):
        self.amount_health = extract_number(title)
        if "potion" in title:
            self.objectType = "Health Potion"
        self.category = "Health"
        self.title = self.objectType + " " + str(self.amount_health)+ " awarded"

class Speed():
    def init_speed(self,title):
        self.amount_speed = extract_number(title)
        if "potion" in title:
            self.objectType = "Speed Potion"
        self.category = "Speed"
        self.title = self.objectType + " " + str(self.amount_speed )+ " awarded"

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

def showBag(self):
    objTypeToCount = {}
    for obj in self.player.bag:
        if obj.objectType not in objTypeToCount:
            objTypeToCount[obj.objectType]=1
        else:
            objTypeToCount[obj.objectType]+=1
    print()
    print("Inventory")
    print(objTypeToCount)
    print()

def extract_number(title):
    c = 0
    h,t = 0,0
    ret = 0
    while c < len(title):
        if title[c] == "[":
            h = c 
            while c < len(title):
                if title[c] == "]":
                    t = c
                    ret = int(title[h+1:t])
                    break
                c += 1
        c += 1
    return ret