import os
import yaml


class Location:
    def __init__(self, config):
        self.title = config['title']
        self.events = config['events']

    def landing(self):
        while True:
            print("You arrive at the " + self.title)
            print("What would you like to do?")
            event_list = [f"{i}] {x['title']}" for i, x in enumerate(self.events)]
            print("\n".join(event_list))

            chosen_event = input("Enter the event: ")
            


class Board:
    def __init__(self):
        self.current_location = None
        self.locations = {}
        self.connections = {}

    def add_location(self, location: Location, starting=False):
        if starting:
            self.current_location = location  # set current location

        self.locations[location.title] = location  # create location mapping
        self.connections[location.title] = set()  # init location connections

    def add_oneway_connection(self, location_a: str, location_b: str):
        self.connections[location_a].add(location_b)  # add location_a -> location_b

    def add_twoway_connection(self, location_a: str, location_b: str):
        self.connections[location_a].add(location_b)  # add location_a -> location_b
        self.connections[location_b].add(location_a)  # add location_b -> location_a

    def adjacent_locations(self):
        return list(self.connections[self.current_location.title])

    def move_to_location(self, new_location):
        assert new_location in self.locations  # check new_location exists
        assert new_location in self.connections[self.current_location.title]  # check current_location -> new_location exists
        self.current_location = self.locations[new_location]
        self.current_location.landing()


class Game:
    def __init__(self, filename):
        self.config = yaml.safe_load(open(filename, 'r'))
        self.board = Board()
        self.title = self.config['title']
        print(self.config)
        for location in self.config['locations']:

            # add location to board
            new_location: Location = Location(location)
            self.board.add_location(new_location, location['starting'])

            # add nearby connections to board
            for nearby in location['nearby']:
                self.board.add_oneway_connection(location['title'], nearby)
        print(self.config)

    def start(self):
        while True:
            adjacent_locations = self.board.adjacent_locations()
            if len(adjacent_locations) == 0:
                print("You reached a dead end, Game Over!")
                exit(0)

            locations = [f'{i+1}] {x}' for i, x in enumerate(adjacent_locations)]
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
                new_location = adjacent_locations[n - 1]
                self.board.move_to_location(new_location)

            except AssertionError:
                print("Invalid input")

