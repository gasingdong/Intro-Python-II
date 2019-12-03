class Item:

    def __init__(self, name_in, description_in):
        self.name = name_in
        self.description = description_in

    def on_take(self):
        print(f"You have obtained {self.name}!")

    def on_drop(self):
        print(f"You have dropped {self.name}!")
