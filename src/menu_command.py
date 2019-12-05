from command import Command
from adv import start_game_loop
import json


class NewGameCommand(Command):

    def process(self, gameIn, *args):
        start_game_loop()


class LoadGameCommand(Command):

    def process(self, gameIn, *args):
        data = None
        with open('src/save.txt') as file:
            data = json.load(file)
        start_game_loop(data)
