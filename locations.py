from crpg import Location, print_options

class Dungeon(Location):
    def __init__(self, **kwargs):
        self.fought_troll = False
        options = ["fight", "flee"]
        super(Location, self).__init__(**kwargs)

    def fight_troll(self):
        if not self.fought_troll:
            print("""
            A towering troll stands in your way.
            What do you do?
            """)
 

    def landing(self):
        print("""
        You have landed in the Dungeon!
        """)

        self.fight_troll()


class Cavern(Location):
    def landing(self):
        print("""
        You have landed in the Cavern!
        """)

class Castle(Location):
    def landing(self):
        print("""
        You have landed in the Cavern!
        """)
