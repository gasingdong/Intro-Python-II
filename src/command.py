class Command:

    def __init__(self, tooltipIn, *inputsIn):
        self.inputs = inputsIn
        self.tooltip = tooltipIn

    def get_tooltip(self):
        return f"[{self.inputs[0]}] {self.tooltip}"

    def process(self, playerIn, *args):
        raise NotImplementedError


class LookCommand(Command):

    def process(self, playerIn, *args):
        playerIn.current_room.get_scene()


class InventoryCommand(Command):

    def process(self, playerIn, *args):
        playerIn.get_items()


class MoveCommand(Command):

    def process(self, playerIn, *args):
        playerIn.move(args[0])


class TakeCommand(Command):

    def process(self, playerIn, *args):
        playerIn.take_item(args[1])


class DropCommand(Command):

    def process(self, playerIn, *args):
        playerIn.drop_item(args[1])


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
