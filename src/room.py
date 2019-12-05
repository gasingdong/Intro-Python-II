# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap
from item import Item, LightSource


class Room:

    def __init__(self, id_in, name_in, description_in):
        self.id = id_in
        self.name = name_in
        self.description = description_in
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""
        self.items = []
        self.natural_light = False

    def setup(self, playerIn):
        is_lit = self.natural_light
        if not is_lit:
            for item in self.items:
                if isinstance(item, LightSource):
                    is_lit = True
                    break

            if not is_lit:
                for item in playerIn.items:
                    if isinstance(item, LightSource):
                        is_lit = True
                    break

        if is_lit:
            self.get_scene()
        else:
            print("It's pitch dark. You can't see anything.")

    def get_scene(self):
        print(f"{self.name}\n")
        print(f"{textwrap.fill(self.description, 80)}")
        num_items = len(self.items)

        if num_items > 0:
            items_text = ""

            if num_items == 1:
                items_text = textwrap.fill(self.items[0].description, 80)
            elif num_items == 2:
                items_text = textwrap.fill(
                    f"{self.items[0].description} and " +
                    f"{self.items[1].description}", 80
                )
            else:
                items_text = textwrap.fill(
                    ', '.join(item.description for item in self.items[:-1]) +
                    f", and {self.items[-1].description}", 80)
            print(f"\nYou see {items_text}.")

    def add_item(self, itemIn):
        if isinstance(itemIn, Item):
            self.items.append(itemIn)
        else:
            raise Exception(
                f"Attempted to add non-item {itemIn.name} to room.")
