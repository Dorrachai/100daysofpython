print('''     ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         \
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ;''')

print("Alone in on an island, under a burning sun, you are stranded on an island trying to survive. \nWould you like "
      "to go further in or walk towards the beach?\n")


def island_adventure():
    location = input("You're on an island. Do you want to go 'in' or to the 'beach'?\n ").lower()
    if location == "in":
        forest_adventure()
    elif location == "beach":
        beach_adventure()
    else:
        print("Invalid input.")
        island_adventure()


def forest_adventure():
    choice = input("You're in a forest. Do you want to climb a 'tree' or go 'deeper'?\n ").lower()
    if choice == "tree":
        print("You climb a tall tree and fell to your death.")
    elif choice == "deeper":
        print("You venture deeper into the forest and find a hidden cave.")
        cave_adventure()
    else:
        print("Invalid input.")
        forest_adventure()


def cave_adventure():
    choice = input("In the deep cave you either go 'deeper' or 'climb' the cave wall\n").lower()
    if choice == "deeper":
        print("You went deeper into the cave and found fruits in a basket. Congratulations you survived this day!")
    elif choice == "climb":
        print("A spider bit you, it was fatal and your adventure ended.")
    else:
        print("Invalid input.")
        cave_adventure()


def beach_adventure():
    choice = input("You're at the beach. Do you want to go for a 'swim' or go 'back'?\n ").lower()
    if choice == "swim":
        print("You swim in the ocean and a shark ate you!")
    elif choice == "back":
        print("You go back to the island.")
        island_adventure()
    else:
        print("Invalid input.")
        beach_adventure()


island_adventure()
