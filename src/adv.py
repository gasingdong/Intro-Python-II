import textwrap
from room import Room
from item import Item
from player import Player

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer",
                     ("Dim light filters in from the south. Dusty passages " +
                      "run north and east.")),

    'overlook': Room("Grand Overlook",
                     ("A steep cliff appears before you, falling into the " +
                      "darkness. Ahead to the north, a light flickers in " +
                      "the distance, but there is no way across the chasm.")),

    'narrow':   Room("Narrow Passage",
                     "The narrow passage bends here from west to north. The " +
                     "smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber",
                     "You've found the long-lost treasure chamber! Sadly, " +
                     "it has already been completely emptied by earlier " +
                     "adventurers. The only exit is to the south."),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

rooms['outside'].add_item(Item("lantern", "a lantern with oil"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = {
    'n': 'n_to',
    'w': 'w_to',
    's': 's_to',
    'e': 'e_to',
}

player = Player("player", rooms['outside'])
print("")
player.current_room.get_scene()

while True:
    room = player.current_room
    print("")
    action = input(
        "[n] North  [w] West   [s] South  [e] East  [q] Quit\n").split(" ")
    print("")
    verb = action[0]
    args = len(action)

    if args > 3:
        print("You don't understand that action.")
        continue

    has_object = len(action) > 1
    has_adj = len(action) > 2

    if has_object:
        obj = action[1]
        if verb == "take" or verb == "get":
            player.take_item(obj)
        elif verb == "drop":
            player.drop_item(obj)
        else:
            print("You don't understand that action.")
    else:
        if verb == 'q':
            print("You abandon the adventure.")
            quit()
        elif (verb == 'n' or verb == 'w' or verb == 's' or verb == 'e'):
            player.move(room, directions[verb])
        elif verb == 'l' or verb == 'look':
            room.get_scene()
        elif verb == 'i' or verb == 'inventory':
            player.get_items()
        else:
            print("You don't understand that action.")
