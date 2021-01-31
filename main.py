from data import entrance
from entrance import Entrance

print(Entrance(entrance))

selection = 0
while selection != len(entrance) + 1:
    selection = input("Please select which door you want to enter")

    try:
        selection = int(selection)
        if selection >= len(entrance) + 1:
            print("You can`t go back, please select the door")
        elif selection > 0 and selection <= len(entrance):
            print(f"You have entered {entrance[selection - 1]}")

    except ValueError:
        print("Please enter your choice as a number.")