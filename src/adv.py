import textwrap
from room import Room
from item import Item
from player import Player
from map import Map
from game import Game
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
    SaveCommand("Save", "save"),
]


def start_game_loop(data=None):
    map = Map()
    map.setup()

    player = Player("player", map.get_starting_room())
    print("")
    game = Game(player, map)
    player.current_room.get_scene()

    while True:
        print("")
        action = input(
            "[n/w/s/e] Move  [h] Help [save] Save [q] Quit\n"
        ).split(" ")
        print("")
        verb = action[0]
        processed = False

        if len(action) <= 3 and verb != "":
            for command in commands:
                if verb in command.inputs:
                    command.process(game, *action)
                    processed = True
                    break

        if not processed:
            print("You don't understand that action.")
