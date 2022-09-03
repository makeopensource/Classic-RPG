# A list of built-in nodes

# A generic node. The node is the building block for the entire 
# decision graph
class Node:
    def __init__(self, game, text):
        self.text = text
        self.parent = None
        self.children = []
        self.game = game

    def list_children(self):
        if self.children:
            for i, child in enumerate(self.children):
                print(f'{i + 1}) {child}')
        else:
            print('no options')

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def add_children(self, nodes):
        for child in nodes:
            self.children.append(child)
            child.parent = self

    def rewind(self, n = 1):
        for _ in range(n):
            self.game.current = self.game.current.parent

    def after(self):
        raise NotImplementedError
           
    def __repr__(self):
        return self.text


# A generic player in the game. Adding features here exposes them
# to the crpg API
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.xp = 0

    def print_stats(self):
        print(f'hp: {self.hp} xp: {self.xp}')

    def __str__(self):
        return self.name


# A location node. This node introduces the location (description)
# when you enter the location
class Location(Node):
    def __init__(self, game, text, description = ''):
        self.description = description
        super().__init__(game, text)

    def after(self):
        print(f'Welcome to {self.text}')

    def __str__(self):
        return self.description


# A generic event. Events are the base of all player interactions.
# Most interactions are event interactions
class Event(Node):
    def __init__(self, game, text, description):
        self.description = description
        super().__init__(game, text)

    def after(self):
        print(self.description)


# A type of action. Fighting reduces the hp, and increases the xp.
# the param "rewind" tells the action how many places back to go.

# Ideally, this implementation should not rely on rewinds, rather,
# we should make new connections and follow them

# hp and xp could also be taken in as arguments for additional
# customization
class Fight(Node):
    def __init__(self, game, text, rewind):
        self.r = rewind
        super().__init__(game, text)

    def after(self):
        player = self.game.player
        player.hp -= 25
        player.xp += 10
        player.print_stats()
        
        self.rewind(self.r)


# Similar to the "Fight" action, Run prevents the player from incurring
# damage, at a cost to xp (and maybe money in the future?)

# Similarly to Fight, rewind should not exist (ideally)

# We also want to be able to *close* connections
class Run(Node):

    def __init__(self, game, text, rewind):
        self.r = rewind
        super().__init__(game, text)

    def after(self):
        player = self.game.player
        player.xp = max(player.xp - 5, 0)

        self.rewind(self.r)


