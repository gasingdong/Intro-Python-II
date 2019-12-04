import copy
from room import Room
from item import Item


class Map:

    rooms = {
        'outside':  Room("Outside Cave Entrance",
                         "North of you, the cave mount beckons."),

        'foyer':    Room("Foyer",
                         ("Dim light filters in from the south. Dusty " +
                          "passages run north and east.")),

        'overlook': Room("Grand Overlook",
                         ("A steep cliff appears before you, falling into " +
                          "the darkness. Ahead to the north, a light " +
                          "flickets in the distance, but there is no " +
                          "way across the chasm.")),

        'narrow':   Room("Narrow Passage",
                         "The narrow passage bends here from west to " +
                         "north. The smell of gold permeates the air."),

        'treasure': Room("Treasure Chamber",
                         "You've found the long-lost treasure chamber! " +
                         "Sadly, it has already been completely emptied " +
                         "by earlier adventurers. The only exit is to " +
                         "the south."),
    }

    def __init__(self):
        self.rooms = copy.deepcopy(Map.rooms)

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
        self.rooms['overlook'].natural_light = True

        self.rooms['outside'].add_item(Item("lantern", "a lantern with oil"))

    def get_starting_room(self):
        return self.rooms['outside']
