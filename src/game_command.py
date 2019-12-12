from command import GameCommand
from map import Map
from room import Room
import json


class SaveCommand(GameCommand):
    def process(self, *args):
        player = self.game.player
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
        print("Your adventure has been saved.")


class HelpCommand(GameCommand):

    def process(self, *args):
        for command in self.game.commands:
            print(command.get_tooltip())


class LookCommand(GameCommand):

    def process(self, *args):
        self.game.player.current_room.get_scene()


class InventoryCommand(GameCommand):

    def process(self, *args):
        self.game.player.get_items()


class MoveCommand(GameCommand):

    def process(self, *args):
        self.game.player.move(args[0])

    def get_tooltip(self):
        s = "/".join(self.inputs)
        return f"[{s}] {self.tooltip}"


class TakeCommand(GameCommand):

    def process(self, *args):
        player = self.game.player
        if args[1] == "it":
            if player.last_item is not None:
                player.take_item(player.last_item.name)
            else:
                print("What's 'it'?")
        else:
            full_name = " ".join(args[1:])
            possible_matches = []
            found = False
            for item in player.current_room.items:
                if full_name == item.name:
                    found = True
                    player.take_item(full_name)
                    break
                elif full_name in item.name:
                    possible_matches.append(item.name)
            if not found and possible_matches:
                if len(possible_matches) == 1:
                    player.take_item(possible_matches[0])
                else:
                    print(f"I don't know which you mean: {possible_matches}")


class DropCommand(GameCommand):

    def process(self, *args):
        player = self.game.player
        if args[1] == "it":
            if player.last_item is not None:
                player.drop_item(player.last_item.name)
            else:
                print("What's 'it'?")
        else:
            player.drop_item(args[1])


class QuitCommand(GameCommand):

    def process(self, *args):
        action = input(
            "Are you sure you want to abandon the adventure? [y/n]\n")
        print("")

        if action == 'y':
            print("You abandon the adventure.")
            quit()
        else:
            self.game.player.current_room.get_scene()
