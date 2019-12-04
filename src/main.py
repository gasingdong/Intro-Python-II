
from command import QuitCommand
from menu_command import *

commands = [
    QuitCommand("Quit", "q", "quit"),
    NewGameCommand("New Game", "n", "new"),
    LoadGameCommand("Load Game", "l", "load"),
]

while True:
    print("")
    print("Welcome to Lambda Adventure!")
    action = input("[n] New Game [l] Load Game [q] Quit\n")
    print("")

    if action != "":
        for command in commands:
            if action in command.inputs:
                command.process(None, action)
                break
