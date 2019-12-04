from command import Command


class HelpCommand(Command):

    def process(self, playerIn, *args):
        for command in Command.commands:
            print(command.get_tooltip())


class LookCommand(Command):

    def process(self, playerIn, *args):
        playerIn.current_room.get_scene()


class InventoryCommand(Command):

    def process(self, playerIn, *args):
        playerIn.get_items()


class MoveCommand(Command):

    def process(self, playerIn, *args):
        playerIn.move(args[0])

    def get_tooltip(self):
        s = "/".join(self.inputs)
        return f"[{s}] {self.tooltip}"


class TakeCommand(Command):

    def process(self, playerIn, *args):
        if args[1] == "it":
            if playerIn.last_item is not None:
                playerIn.take_item(playerIn.last_item.name)
            else:
                print("What's 'it'?")
        else:
            playerIn.take_item(args[1])


class DropCommand(Command):

    def process(self, playerIn, *args):
        if args[1] == "it":
            if playerIn.last_item is not None:
                playerIn.drop_item(playerIn.last_item.name)
            else:
                print("What's 'it'?")
        else:
            playerIn.drop_item(args[1])
