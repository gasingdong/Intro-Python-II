# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name_in, starting_room):
        self.name = name_in
        self.current_room = starting_room
        self.items = []
