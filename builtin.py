# Base player classes

class Player:
    def __init__(self):
        self.hp = 100
        self.xp = 0

    def summary(self):
        return f'hp: {self.hp} xp: {self.xp}'

# Base node classes

class Node:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc

    def on_select(self):
        print(self.desc)

    def __str__(self):
        return self.title


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

