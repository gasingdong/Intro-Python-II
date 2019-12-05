from command import Command


class HelpCommand(Command):

    def process(self, gameIn, *args):
        for command in Command.commands:
            print(command.get_tooltip())


class LookCommand(Command):

    def process(self, gameIn, *args):
        gameIn.player.current_room.get_scene()


class InventoryCommand(Command):

    def process(self, gameIn, *args):
        gameIn.player.get_items()


class MoveCommand(Command):

    def process(self, gameIn, *args):
        gameIn.player.move(args[0])

    def get_tooltip(self):
        s = "/".join(self.inputs)
        return f"[{s}] {self.tooltip}"


class TakeCommand(Command):

    def process(self, gameIn, *args):
        player = gameIn.player
        if args[1] == "it":
            if player.last_item is not None:
                player.take_item(player.last_item.name)
            else:
                print("What's 'it'?")
        else:
            player.take_item(args[1])


class DropCommand(Command):

    def process(self, gameIn, *args):
        player = gameIn.player
        if args[1] == "it":
            if player.last_item is not None:
                player.drop_item(player.last_item.name)
            else:
                print("What's 'it'?")
        else:
            player.drop_item(args[1])
