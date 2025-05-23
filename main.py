from character import Character

cave = { "1": ["5", "8", "13"], 
    "2": ["6", "8", "14"],
    "3": ["13", "17", "16"],
    "4": ["5", "8", "13"],
    "5": ["1", "4", "9"],
    "6": ["2", "8", "12"],
    "7": ["15", "12", "18"],
    "8": ["1", "2", "6"],
    "9": ["4", "5", "11"],
    "10": ["16", "17", "18"],
    "11": ["9", "15", "19"],
    "12": ["6", "7", "14"],
    "13": ["1", "3", "17"],
    "14": ["2", "12", "20"],
    "15": ["7", "11", "19"],
    "16": ["3", "10", "20"],
    "17": ["3", "10", "13"],
    "18": ["7", "10", "18"],
    "19": ["4", "11", "15"],
    "20": ["14", "16", "18"],
    "Bats": ["4", "17"],
    "Pitfalls": ["20", "2"],
    "Wumpus": "9"
}

def printInstructions():
    '''
    No input, no return
    Outputs the directions
    '''
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
    

print("Welcome to Hunt the Wumpus!")
while True:
    choice = input("Type 1 to read the instructions, 2 to play the game, or 3 to quit.\n")
    # Instructions
    if choice == "1":
        printInstructions()
    # Start game
    elif choice == "2":
        bats = cave["Bats"]
        pitfalls = cave["Pitfalls"]
        wumpusLocation = cave["Wumpus"]
        character = Character()
        
        # While game is running
        while True:
            print("\nYou are now in room", character.getLocation(), "of the cave.")
            possibleRooms = cave[character.getLocation()]
            character.checkRooms(bats, pitfalls, wumpusLocation, possibleRooms)
            move = input("Would you like to shoot, move, or quit? Input S for shoot, M for move, or Q for quit.\n")
            
            if move.upper() == "M":
                print("You can move to the following rooms:")
                print(possibleRooms[0], possibleRooms[1], possibleRooms[2])
                character.moveRooms(possibleRooms)
            # Shoot arrows
            elif move.upper() == "S":
                success = ""
                numArrows = 0
                while True:
                    numArrows = int(input("How many arrows would you like to use?\n"))
                    if numArrows > character.getArrows():
                        print("You don't have that many arrows.")
                    elif numArrows < 1:
                        print("That is not a valid number of arrows. Please try again.")
                    else:
                        break
                print("Nearby Rooms:", possibleRooms[0], possibleRooms[1], possibleRooms[2]) 
                for shot in range(numArrows):
                    room = input("\nWhere would you like to shoot your arrow?\n")
                    success = character.shootArrow(room, possibleRooms, wumpusLocation)
                    if success == "win":
                        print("You have shot and killed the wumpus!")
                        print("YOU WIN\n")
                        break
                if success == "win":
                    break
            # quit
            elif move.upper() == "Q":
                print("Coward")
                break
            else:
                print("Invalid input. Please try again.")
            
            if character.getArrows() < 1:
                print("You are out of arrows!")
                print("GAME OVER\n")
                break
            
            # Location checks for traps/wumpus
            if character.getLocation() in bats:
                character.batTrap()
            if character.getLocation() in pitfalls:
                print("You fell down a pit!")
                print("GAME OVER\n")
                break
            wumpusLocation = character.rollWumpus(wumpusLocation, cave[wumpusLocation])
            if wumpusLocation == "21":
                print("The wumpus has found you and will now eat you!")
                print("GAME OVER\n")
                break
    # Exit
    elif choice == "3":
        print("Goodbye!")
        break
    # Bad input
    else:
        print("Invalid input, please try again.")
    