from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    commands = []

    def __init__(self, tooltipIn, *inputsIn):
        self.inputs = inputsIn
        self.tooltip = tooltipIn
        Command.commands.append(self)

    def get_tooltip(self):
        return f"[{self.inputs[0]}] {self.tooltip}"

    @abstractmethod
    def process(self, playerIn, *args):
        pass


class QuitCommand(Command):

    def process(self, playerIn, *args):
        action = input(
            "Are you sure you want to abandon the adventure? [y/n]\n")
        print("")

        if action == 'y':
            print("You abandon the adventure.")
            quit()
        else:
            playerIn.current_room.get_scene()
