# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

    def __str__(self):
        player_string = f"(player.name) is currently in (self.current_room)"

    def move(self, direction):
        next_room = self.current_room.getdirection(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print("This isn't an exit. Please input again")