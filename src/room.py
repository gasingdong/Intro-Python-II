# Implement a class to hold room information. This should have name and
# description attributes.


class Room:

    def __init__(self, name_in, description_in):
        self.name = name_in
        self.description = description_in
        self.n_to = ""
        self.s_to = ""
        self.e_to = ""
        self.w_to = ""
        self.items = []
