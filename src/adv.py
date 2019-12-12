import textwrap
from room import Room
from item import Item
from player import Player
from map import Map
from game import Game
from game_command import *


def start_game_loop(data=None):
    map = None
    player = None

    if data is None:
        map = Map()
        map.setup()
        player = Player("player", map.get_starting_room())
    else:
        map = Map(data['rooms'])
        player = Player("player", map.get_starting_room())
        player.load_player_data(data['player'])

    game = Game(player, map)
    game.commands = [
        QuitCommand(game, "Quit", "q", "quit"),
        TakeCommand(game, "Take Item", "take", "get"),
        DropCommand(game, "Drop Item", "drop", "lose"),
        LookCommand(game, "Look Around", "l", "look"),
        InventoryCommand(game, "Inventory", "i", "inventory"),
        MoveCommand(game, "Move", "n", "w", "s", "e"),
        HelpCommand(game, "Help", "h", "help"),
        SaveCommand(game, "Save", "v", "save"),
    ]
    print("")
    player.current_room.get_scene()

    while True:
        print("")
        action = input("What will you do? ").split(" ")
        print("")
        verb = action[0]
        processed = False

        if verb != "":
            for command in game.commands:
                if verb in command.inputs:
                    command.process(*action)
                    processed = True
                    break

        if not processed:
            print("You don't know how to do that.")
