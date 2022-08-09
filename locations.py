from crpg import Location, print_options

class Dungeon(Location):
    def __init__(self, name):
        self.fought_troll = False
        self.options = ["fight", "flee"]
        self.name = name
        super(Location, self).__init__()

    def fight_troll(self):
        if not self.fought_troll:
            print("""
            A towering troll stands in your way.
            """)

            print_options(self.options)

            option = int(input("What do you do? "))
            choice = self.options[option - 1]
            if choice == "fight":
                print("""
                You fight the beast
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
