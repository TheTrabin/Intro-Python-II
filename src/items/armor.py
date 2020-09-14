  
from item import Item
class Armor(Item):
    def __init__(self, name, description, defence):
        super().__init__(name, description)
        self.defence = defence

    def __str__(self):
        return f"{self.name}\n{self.description}\n with an attack boost of {self.defence}"