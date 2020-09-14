# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None

    def __repr__(self):
        return f"{self.name}: {self.description}"

    def add_item(self,item):
        self.items.append(item)

    def drop_item(self,item):
        self.items.remove(item)

    def __str__(self):
        output = "\n"
        output += f"{self.name}\n"
        output += f"{self.description}\n"
        output += "Exits to the: "
        output += " [North] " if hasattr(self, "n_to") else ""
        output += " [South] " if hasattr(self, "s_to") else ""
        output += " [East] " if hasattr(self, "e_to") else ""
        output += " [West] " if hasattr(self, "w_to") else ""

        return output
