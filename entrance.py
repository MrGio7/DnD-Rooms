from rooms import Rooms

class Entrance(Rooms):
    def __init__(self, doors) -> None:
        self.doors = doors

    def __str__(self) -> str:
        dodo = ""
        for i, d in enumerate(self.doors):
            dodo += str(i + 1) + ": " + d + "\n"

        return dodo