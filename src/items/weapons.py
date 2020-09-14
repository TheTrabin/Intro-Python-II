  
from item import Item
class Weapon(Item):
    def __init__(self, name, description, attack):
        super().__init__(name, description)
        self.attack = attack

    def __str__(self):
        return f"{self.name}\n{self.description}\n with an attack boost of {self.attack}"