print("Welcome to Hunt the Wumpus!")

while True:
    choice = input("Type 1 to read the instructions, 2 to play the game, or 3 to quit.\n")
    
    if choice == "1":
        print("The wumpus lives in a cave of 20 rooms. Each room has 3 tunnels leading to other rooms. (Look at a dodecahedron to see how this works - if you don't know what a dodecahedron is, ask someone).\n\n")
        print("Hazards")
        print("Bottomless pits - two rooms have bottomless pits in them. If you go there, you fall into the pit (& lose!)")
        print("Super bats - two other rooms have super bats. If you go there, a bat grabs you and takes you to some other room at random. (Which may be troublesome).\n\n")
        print("Wumpus")
        print("The wumpus is not bothered by hazards (he has sucker feet and is too big for a bat to lift). Usually he is asleep. Two things wake him up: you shooting an arrow or you entering his room.\n")
        print("If the wumpus wakes he moves (p=.75) one room or stays still (p=.25). After that, if he is where you are, he eats you up and you lose!\n\n")
        print("You")
        print("Each turn you may move or shoot a crooked arrow.")
        print("Moving: you can move one room (thru one tunnel).")
        print("Arrows: you have 5 arrows. You lose when you run out. Each arrow can go from 1 to 5 rooms. You aim by telling the computer the rooms you want the arrow to go to. If the arrow can't go that way (if no tunnel) it moves at random to the next room. If the arrow hits the wumpus, you win. If the arrow hits you, you lose.\n\n")
        print("Warnings")
        print("When you are one room away from a wumpus or hazard, the computer says:\n")
        print("Wumpus: \"I smell a wumpus\"\nBat: \"Bats nearby\"\nPit: \"I feel a draft\"\n\n")
    elif choice == "2":
        print("Okay")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid input, please try again.")
    