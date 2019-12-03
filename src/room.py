# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    name: ""
    description: ""
    n_to: ""
    s_to: ""
    e_to: ""
    w_to: ""
    items: []

    def __init__(self, name_in, description_in):
        self.name = name_in
        self.description = description_in
