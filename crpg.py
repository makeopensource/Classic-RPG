import os


def clear():
    if os.name == "posix": 
        os.system('clear')
    else: 
        os.system('cls')


class Location:
    def __init__(self, name):
        self.name = name


class Game:
    def __init__(self, name):
        self.name = name
        self.current_location = None
        self.locations = {}
        self.connections = {}

    def add_location(self, location, starting=False):
        if starting:
            self.current_location = location  # set current location

        self.locations[location.name] = location  # create location mapping
        self.connections[location.name] = set()  # init location connections

    def add_oneway_connection(self, location_a, location_b):
        assert location_a.name in self.connections  # ensure location_a exists
        assert location_b.name in self.connections  # ensure location_b exists

        self.connections[location_a.name].add(location_b.name)  # add location_a -> location_b

    def add_twoway_connection(self, location_a, location_b):
        assert location_a.name in self.connections  # ensure location_a exists
        assert location_b.name in self.connections  # ensure location_b exists

        self.connections[location_a.name].add(location_b.name)  # add location_a -> location_b
        self.connections[location_b.name].add(location_a.name)  # add location_b -> location_a

    def adjacent_locations(self):
        return list(self.connections[self.current_location.name])

    def move_to_location(self, new_location_name):
        assert new_location_name in self.locations  # check new_location exists
        assert new_location_name in self.connections[self.current_location.name]  # check current_location -> new_location exists
        self.current_location = self.locations[new_location_name]

    def start(self):
        while True:
            clear()
            if len(self.adjacent_locations()) == 0:
                print("You reached a dead end, Game Over!")
                exit(0)

            locations = [f'{i+1}] {x}' for i, x in enumerate(self.adjacent_locations())]
            print('\n'.join(locations))

            try:
                n = int(input("Pick a path: "))

            except KeyboardInterrupt:
                print("\nThanks for playing!")
                exit(0)

            except (TypeError,ValueError):
                n = 0

            try:
                assert n > 0
                new_location = self.adjacent_locations()[n - 1]
                print(new_location)
                self.move_to_location(new_location)

            except AssertionError:
                print("Invalid input")



