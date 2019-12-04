import textwrap
from room import Room
from item import Item
from player import Player
from map import Map
from command import QuitCommand
from game_command import *

commands = [
    QuitCommand("Quit", "q", "quit"),
    TakeCommand("Take Item", "take", "get"),
    DropCommand("Drop Item", "drop", "lose"),
    LookCommand("Look Around", "l", "look"),
    InventoryCommand("Inventory", "i", "inventory"),
    MoveCommand("Move", "n", "w", "s", "e"),
    HelpCommand("Help", "h", "help"),
]


def start_game_loop(data=None):
    map = Map()
    map.setup()

    player = Player("player", map.get_starting_room())
    print("")
    player.current_room.get_scene()

    while True:
        print("")
        action = input(
            "[n] North  [w] West   [s] South  [e] East  [h] Help [q] Quit\n"
        ).split(" ")
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
