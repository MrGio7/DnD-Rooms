import random

class Rooms:
    def __init__(self, doors) -> None:
        self.doors = doors

    def __str__(self) -> str:
        rtn = "\n"
        for i, d in enumerate(self.doors):
            rtn += "  " + str(i + 1) + ": " + d + "\n"

        return rtn

    def my_choice(self):
        selection = 0

        while selection != len(self.doors) + 1:
            selection = input("Please select which door you want to enter: ")

            try:
                selection = int(selection)
                if selection >= len(self.doors) + 1:
                    print("You can`t go back, please select the door")
                elif selection > 0 and selection <= len(self.doors):
                    rnd = random.randrange(1, len(self.doors) + 1)
                    if selection == rnd:
                        return (f"\n You have entered {self.doors[selection - 1]} and you see some other doors, please select next door")
                    else:
                        print(f"\n You have entered TRAP ROOM, RIP, correct path was {str(rnd)} please try again")
                        exit()

            except ValueError:
                print("Please enter your choice as a number.")