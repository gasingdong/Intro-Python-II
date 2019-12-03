# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    name: ""
    description: ""

    def __init__(self, nameIn, descriptionIn):
        self.name = nameIn
        self.description = descriptionIn
