from abc import ABCMeta, abstractmethod
from map import Map
from room import Room
import json


class Command(metaclass=ABCMeta):
    commands = []

    def __init__(self, tooltipIn, *inputsIn):
        self.inputs = inputsIn
        self.tooltip = tooltipIn
        Command.commands.append(self)

    def get_tooltip(self):
        return f"[{self.inputs[0]}] {self.tooltip}"

    @abstractmethod
    def process(self, game, *args):
        pass


class QuitCommand(Command):

    def process(self, gameIn, *args):
        player = gameIn.player
        if player is not None:
            action = input(
                "Are you sure you want to abandon the adventure? [y/n]\n")
            print("")

            if action == 'y':
                print("You abandon the adventure.")
                data = {}
                data['player'] = {
                    'name': player.name,
                    'current_room': player.current_room.id,
                    'items': list(map(lambda item: item.id, player.items)),
                }
                data['rooms'] = []
                rooms = gameIn.map.rooms
                for room in rooms:
                    n_to = rooms[room].n_to
                    w_to = rooms[room].w_to
                    s_to = rooms[room].s_to
                    e_to = rooms[room].e_to
                    data['rooms'].append({
                        "id": room,
                        "n_to": n_to.id if isinstance(n_to, Room) else "",
                        "w_to": w_to.id if isinstance(w_to, Room) else "",
                        "s_to": s_to.id if isinstance(s_to, Room) else "",
                        "e_to": e_to.id if isinstance(e_to, Room) else "",
                        "items": list(map(lambda item: item.id,
                                          rooms[room].items))
                    })
                with open('src/save.txt', 'w+') as outfile:
                    json.dump(data, outfile)
                quit()
            else:
                player.current_room.get_scene()
        else:
            quit()
