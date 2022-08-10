import os
import yaml


class Location:
    def __init__(self, config):
        self.title = config['title']
        self.events = config['events']


class Board:
    def __init__(self):
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


class Game:
    def __init__(self, filename):
        self.config = yaml.safe_load(open(filename, 'r'))
        self.board = Board()
        self.title = self.config['title']
        for location in self.config['locations']:

            # add location to board
            new_location = Location(location)
            self.board.add_location(new_location)

            # add nearby connections to board
            for nearby in location['nearby']:
                self.board.add_oneway_connection(location, nearby)
        print(self.config)

    def start():
        while True:

