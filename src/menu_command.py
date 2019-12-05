from command import Command
from adv import start_game_loop


class NewGameCommand(Command):

    def process(self, gameIn, *args):
        start_game_loop()


class LoadGameCommand(Command):

    def process(self, gameIn, *args):
        pass
