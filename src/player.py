# Write a class to hold player information, e.g. what room they are in
# currently.
import textwrap
from item import Item


class Player:

    def __init__(self, name_in, starting_room):
        self.name = name_in
        self.current_room = starting_room
        self.items = []

    def move(self, roomIn, directionIn):
        new_room = getattr(roomIn, directionIn, "")
        if new_room == "":
            print("You cannot go there.")
        else:
            self.current_room = new_room
            self.current_room.get_scene()

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
                self.current_room.items.append(item)
                item.on_drop()
                break
        if not found:
            print("You don't have that item.")
