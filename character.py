import random

class Character:
    
    def __init__(self, arrows = 5, location = "1"):
        self.arrows = arrows
        self.location = location
        
    def getLocation(self):
        return self.location
    
    # Output messages that there is a trap, bats, or wumpus nearby
    def checkRooms(self, bats, pitfalls, wumpus, possibleRooms):
        # If bats nearby
        if (possibleRooms[0] in bats or possibleRooms[1] in bats or possibleRooms[2] in bats):
            print("Bats nearby")
        # If nearby Wumpus
        if (possibleRooms[0] == wumpus or possibleRooms[1] == wumpus or possibleRooms[2] == wumpus):
            print("I smell a wumpus")
        # If nearby pitfall
        if (possibleRooms[0] in pitfalls or possibleRooms[1] in pitfalls or possibleRooms[2] in pitfalls):
            print("I feel a draft")

    # Got hit by bats
    def batTrap(self):
        print("Uh oh! Bats!")
        newSpot = random.randint(0, 20)
        print("After being carried away by bats you find yourself at", newSpot)
        self.location = str(newSpot)
        
    def moveRooms(self, possibleRooms):
        while True:
            newLocation = input("Where would you like to move?\n")
            if (newLocation in possibleRooms):
                self.location = newLocation
                break
            else:
                print("Invalid location. Try again.")
        
        
        
