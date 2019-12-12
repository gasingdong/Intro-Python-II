class Item:

    def __init__(self, id_in, name_in, description_in):
        self.id = id_in
        self.name = name_in
        self.description = description_in

    def on_take(self):
        print(f"You have obtained {self.name}!")

    def on_drop(self):
        print(f"You have dropped {self.name}!")


class LightSource(Item):

    def on_take(self):
        super().on_take()
        print("There's light emanating from it.")

    def on_drop(self):
        super().on_drop()
        print("Are you sure about that? It's dark around here.")


class Weapon(Item):
    pass


class Treasure(Item):
    pass
