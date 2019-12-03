# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    room = ""

    def __init__(self, startingRoom):
        self.room = startingRoom
