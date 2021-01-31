class Rooms:
    def __init__(self, doors) -> None:
        self.doors = doors

    def __str__(self) -> str:
        dodo = ""
        for i, d in enumerate(self.doors):
            dodo += str(i + 1) + ": " + d + "\n"

        return dodo

    def my_choice(self):
        selection = 0
        while selection != len(self.doors) + 1:
            selection = input("Please select which door you want to enter")

            try:
                selection = int(selection)
                if selection >= len(self.doors) + 1:
                    print("You can`t go back, please select the door")
                elif selection > 0 and selection <= len(self.doors):
                    return (f"You have entered {self.doors[selection - 1]} and you see some other doors, please select next door")

            except ValueError:
                print("Please enter your choice as a number.")