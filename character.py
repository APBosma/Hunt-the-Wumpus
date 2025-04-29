import random

class Character:
    
    def __init__(self, arrows = 5, location = "1"):
        self.arrows = arrows
        self.location = location
        
    def getLocation(self):
        return self.location
    
    def getArrows(self):
        return self.arrows
    
    # Output messages that there is a trap, bats, or wumpus nearby
    def checkRooms(self, bats, pitfalls, wumpus, possibleRooms):
        if (possibleRooms[0] in bats or possibleRooms[1] in bats or possibleRooms[2] in bats):
            print("Bats nearby")
        if (possibleRooms[0] == wumpus or possibleRooms[1] == wumpus or possibleRooms[2] == wumpus):
            print("I smell a wumpus")
        if (possibleRooms[0] in pitfalls or possibleRooms[1] in pitfalls or possibleRooms[2] in pitfalls):
            print("I feel a draft")

    # Got hit by bats
    def batTrap(self):
        print("Uh oh! Bats!")
        newSpot = random.randint(1, 20)
        print("After being carried away by bats you find yourself at", newSpot)
        self.location = str(newSpot)
        
    # Character movement
    def moveRooms(self, possibleRooms):
        while True:
            newLocation = input("Where would you like to move?\n")
            if (newLocation in possibleRooms):
                self.location = newLocation
                break
            else:
                print("Invalid location. Try again.")
    
    # Hit wumpus
    def rollWumpus(self, wumpusLocation, possibleLocations):
        if wumpusLocation != self.location:
            return wumpusLocation
        
        wakeUp = random.randint(1, 4)
        if wakeUp < 4:
            print("You scared away the wumpus!")
            return possibleLocations[wakeUp-1]
        else:
            return "21"
        
    # Shooting arrows
    def shootArrow(self, room, possibleRooms, wumpus):
        if room in possibleRooms:
            if wumpus == room:
                return "win"
            self.arrows -= 1
        else:
            newRoom = random.randint(1,20)
            if wumpus == newRoom:
                return "win"
            self.arrows -= 1
        return "no win"
    
    # Set location of character for testing
    def setLocation(self, newSpot):
        self.location = newSpot
        
        
        
