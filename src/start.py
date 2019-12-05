
from menu_command import *

commands = [
    QuitMenuCommand("Quit", "q", "quit"),
    NewGameCommand("New Game", "n", "new"),
    ContinueCommand("Continue", "c", "continue", "load"),
]

while True:
    print("")
    print("Welcome to Lambda Adventure!")
    action = input("[n] New Game [c] Continue [q] Quit\n")
    print("")

    if action != "":
        for command in commands:
            if action in command.inputs:
                command.process()
                break
