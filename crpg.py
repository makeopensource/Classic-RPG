import os


def clear():
    if os.name == "posix": 
        os.system('clear')
    else: 
        os.system('cls')


def print_options(options):
    options = list(options)
    listed_options = [f'{i+1}] {x}' for i, x in enumerate(options)]
    print('\n'.join(listed_options))


class Input:
    def __init__(self, text, _type):
        self.text = text
        self.type = _type

    def __enter__(self):
        try:
            retval = self.type(input(self.text))
            clear()
            assert retval
            return retval

        except (TypeError,ValueError):
            print("Invalid value")

        except KeyboardInterrupt:
            print("\nThanks for playing!")
            exit(0)

    def __exit__(self):
        pass



class Location:
    def __init__(self, name):
        self.name = name

    def landing(self):
        print("""
        This is the landing site
        """)


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
        self.current_location.landing()

    def start(self):

        assert self.current_location

        while True:
            if len(self.adjacent_locations()) == 0:
                print("You reached a dead end, Game Over!")
                exit(0)

            print_options(self.adjacent_locations()) 

            with Input("Pick a path", int) as user_input:
                n = user_input
                new_location = self.adjacent_locations()[n - 1]
                self.move_to_location(new_location)

