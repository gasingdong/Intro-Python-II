import copy
from room import Room
from item import *


class Map:

    rooms = {
        'outside':  Room("outside", "Outside Cave Entrance",
                         "North of you, the cave mount beckons."),

        'foyer':    Room("foyer", "Foyer",
                         ("Dim light filters in from the south. Dusty " +
                          "passages run north and east.")),

        'overlook': Room("overlook", "Grand Overlook",
                         ("A steep cliff appears before you, falling into " +
                          "the darkness. Ahead to the north, a light " +
                          "flickers in the distance, but there is no " +
                          "way across the chasm.")),

        'narrow':   Room("narrow", "Narrow Passage",
                         "The narrow passage bends here from west to " +
                         "north. The smell of gold permeates the air."),

        'treasure': Room("treasure", "Treasure Chamber",
                         "You've found the long-lost treasure chamber! " +
                         "Sadly, it has already been completely emptied " +
                         "by earlier adventurers. The only exit is to " +
                         "the south."),
    }

    items = {
        'lantern': LightSource("lantern", "lantern", "a lit lantern"),
        'rusty_sword': Weapon("rusty_sword", "rusty sword", "a rusty sword"),
        'silver_sword': Weapon("silver_sword", "silver sword",
                               "a silver sword"),
    }

    def __init__(self, roomsIn=None):
        if roomsIn is None:
            self.rooms = copy.deepcopy(Map.rooms)
        else:
            def load_room(roomDataIn):
                room = Map.rooms[roomDataIn['id']]
                directions = ['n_to', 'w_to', 's_to', 'e_to']
                for x in directions:
                    dir_room = roomDataIn[x]
                    setattr(
                        room, x, Map.rooms[dir_room] if dir_room else "")
                room.items = list(map(
                    lambda item: Map.items[item], roomDataIn['items']))
                return room
            self.rooms = {}
            for room in roomsIn:
                self.rooms[room['id']] = load_room(room)

    def setup(self):
        self.rooms['outside'].n_to = self.rooms['foyer']
        self.rooms['foyer'].s_to = self.rooms['outside']
        self.rooms['foyer'].n_to = self.rooms['overlook']
        self.rooms['foyer'].e_to = self.rooms['narrow']
        self.rooms['overlook'].s_to = self.rooms['foyer']
        self.rooms['narrow'].w_to = self.rooms['foyer']
        self.rooms['narrow'].n_to = self.rooms['treasure']
        self.rooms['treasure'].s_to = self.rooms['narrow']

        self.rooms['outside'].natural_light = True
        self.rooms['foyer'].natural_light = True

        self.rooms['outside'].add_item(Map.items['lantern'])
        self.rooms['narrow'].add_item(Map.items['rusty_sword'])
        self.rooms['narrow'].add_item(Map.items['silver_sword'])

    def get_starting_room(self):
        return self.rooms['outside']
