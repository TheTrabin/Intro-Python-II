# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.bag = []
        self.hp = 100
        # self.equip.armor = []
        # self.equip.weapon = []
        # self.defence = (5 + self.equip.armor[0].defence)
        # self.attack = (5 + self.equip.weapon[0].attack)
        


    def __refr__(self):
        return f"{self.name} is currently in {self.current_room}"

    def move(self, direction):
        next_room = self.current_room.getdirection(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print("This isn't an exit. Please input again")

    # def equip(self, item):
    #     if self.equip.armor > 0:
    #         self.equip.armor.append(item)
    #     if self.equip.armor <= 1:
    #         askarmor = input(f"Do you want to switch out {self.equip.armor} with this? y/n")
    #         if askarmor == "y":
    #             self.bag.append(self.equip.armor)
    #             self.equip.armor.append(item)
    #         if askarmor == "n":
    #             print(f"{item} was placed back in bag.")

    #     if self.equip.weapon > 0:
    #         self.equip.weapon.append(item)
    #     if self.equip.weapon <= 1:
    #         askweapon = input(f"Do you want to switch out {self.equip.weapon} with this? y/n")
    #         if askweapon == "y":
    #             self.bag.append(self.equip.weapon)
    #             self.equip.weapon.append(item)
    #         if askweapon == "n":
    #             print(f"{item} was placed back in bag.")

    def take_item(self, item):
        self.bag.append(item)
    
    def drop_item(self, item):
        self.bag.remove(item)