# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
from item import Item


class Room:

    def __init__(self, name_in, description_in):
        self.name = name_in
        self.description = description_in
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""
        self.items = []
        self.natural_light = False

    def setup(self, playerIn):
        if self.natural_light:
            self.get_scene()
        else:
            print("It's pitch dark. You can't see anything.")

    def get_scene(self):
        print(f"{self.name}\n")
        print(f"{textwrap.fill(self.description, 80)}")

        if (len(self.items) > 0):
            items_text = textwrap.fill(
                ', '.join(item.description for item in self.items), 80)
            print(f"\nYou see {items_text}.")

    def add_item(self, itemIn):
        if isinstance(itemIn, Item):
            self.items.append(itemIn)
        else:
            raise Exception(
                f"Attempted to add non-item {itemIn.name} to room.")
