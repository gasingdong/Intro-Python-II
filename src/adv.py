import textwrap
from room import Room
from item import Item
from player import Player
from command import *

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

commands = [
    QuitCommand("Quit", "q", "quit"),
    TakeCommand("Take Item", "take", "get"),
    DropCommand("Drop Item", "drop", "lose"),
    LookCommand("Look Around", "l", "look"),
    InventoryCommand("Inventory", "i", "inventory"),
    MoveCommand("Move", "n", "w", "s", "e"),
]

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
    processed = False

    if len(action) <= 3 and verb != "":
        for command in commands:
            if verb in command.inputs:
                command.process(player, *action)
                processed = True
                break

    if not processed:
        print("You don't understand that action.")
