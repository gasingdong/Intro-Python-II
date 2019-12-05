# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap
from item import Item
from map import Map


class Player:
    directions = {
        'n': 'n_to',
        'w': 'w_to',
        's': 's_to',
        'e': 'e_to',
    }

    def __init__(self, name_in, starting_room):
        self.name = name_in
        self.current_room = starting_room
        self.items = []
        self.last_item = None

    def load_player_data(self, dataIn):
        self.name = dataIn['name']
        self.current_room = Map.rooms[dataIn['current_room']]
        self.items = list(map(lambda item: Map.items[item], dataIn['items']))

    def move(self, directionIn):
        new_room = getattr(self.current_room,
                           Player.directions[directionIn], "")
        if new_room == "":
            print("You cannot go there.")
        else:
            self.current_room = new_room
            self.current_room.setup(self)

    def get_items(self):
        if (len(self.items) > 0):
            items_text = textwrap.fill(
                ', '.join(item.description for item in self.items), 80)
            print(f"You have {items_text}.")
        else:
            print("You have no items.")

    def add_item(self, itemIn):
        if isinstance(itemIn, Item):
            self.items.append(itemIn)
            itemIn.on_take()
        else:
            raise Exception(
                f"Attempted to add non-item {itemIn.name} to player.")

    def take_item(self, itemIn):
        found = False
        for item in self.current_room.items:
            if (item.name == itemIn):
                found = True
                self.current_room.items = [
                    x for x in self.current_room.items if not x.name == itemIn]
                self.add_item(item)
                self.last_item = item
                break
        if not found:
            print("That item isn't in this room.")

    def drop_item(self, itemIn):
        found = False
        for item in self.items:
            if (item.name == itemIn):
                found = True
                self.items = [
                    x for x in self.items if not x.name == itemIn]
                self.current_room.add_item(item)
                self.last_item = item
                item.on_drop()
                break
        if not found:
            print("You don't have that item.")
