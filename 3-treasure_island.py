print("Welcome to treasure island, your mission is to find the treasure!")

choice = input("You're at a cross road. Where do you want to go? (type \"left\" or \"right\") ").lower()

if choice == "left":
    choice = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.").lower()
    if choice == "wait":
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?").lower()
        if choice == "yellow":
            print("You win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")