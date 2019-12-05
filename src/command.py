from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    def __init__(self, tooltipIn, *inputsIn):
        self.inputs = inputsIn
        self.tooltip = tooltipIn

    def get_tooltip(self):
        return f"[{'/'.join(self.inputs[:6])}] {self.tooltip}"

    @abstractmethod
    def process(self, *args):
        pass


class GameCommand(Command, metaclass=ABCMeta):

    def __init__(self, gameIn, tooltipIn, *inputsIn):
        super().__init__(tooltipIn, *inputsIn)
        self.game = gameIn
