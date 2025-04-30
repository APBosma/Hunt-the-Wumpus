import random

class Character:
    
    def __init__(self, arrows = 5, location = "1"):
        self.arrows = arrows
        self.location = location
        
    def getLocation(self):
        '''
        No inputs
        Returns character's location
        '''
        return self.location
    
    def getArrows(self):
        '''
        No inputs
        Returns the number of arrows left
        '''
        return self.arrows
    
    def checkRooms(self, bats, pitfalls, wumpus, possibleRooms):
        '''
        Inputs: bat locations, pitfall locations, wumpus location, and possible rooms the character could enter
        Returns nothing
        Outputs warnings for nearby monsters
        '''
        if (possibleRooms[0] in bats or possibleRooms[1] in bats or possibleRooms[2] in bats):
            print("Bats nearby")
        if (possibleRooms[0] == wumpus or possibleRooms[1] == wumpus or possibleRooms[2] == wumpus):
            print("I smell a wumpus")
        if (possibleRooms[0] in pitfalls or possibleRooms[1] in pitfalls or possibleRooms[2] in pitfalls):
            print("I feel a draft")

    # Got hit by bats
    def batTrap(self):
        '''
        No inputs
        Returns nothing
        Changes the character's location to a random room
        '''
        print("Uh oh! Bats!")
        newSpot = random.randint(1, 20)
        print("After being carried away by bats you find yourself at", newSpot)
        self.location = str(newSpot)
        
    # Character movement
    def moveRooms(self, possibleRooms):
        '''
        Inputs: Possible rooms character could enter
        Returns nothing
        Moves character to wherever they select, with input validation
        '''
        while True:
            newLocation = input("Where would you like to move?\n")
            if (newLocation in possibleRooms):
                self.location = newLocation
                break
            else:
                print("Invalid location. Try again.")
    
    # Hit wumpus
    def rollWumpus(self, wumpusLocation, possibleLocations):
        '''
        Inputs: Wumpus location, possible location for wumpus to go
        Returns either the character's death, or where the wumpus moved
        You ran into the wumpus
        '''
        if wumpusLocation != self.location:
            return wumpusLocation
        
        wakeUp = random.randint(1, 4)
        if wakeUp < 4:
            print("You scared away the wumpus!")
            return possibleLocations[wakeUp-1]
        else:
            return "21"
        
    def shootArrow(self, room, possibleRooms, wumpus):
        '''
        Inputs: The room the arrow will be shot to, possible rooms the character can enter, and wumpus location
        Returns if you won or not
        '''
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
    
    def setLocation(self, newSpot):
        '''
        Inputs: New location to set the character at
        Returns nothing
        Only used in testing
        '''
        self.location = newSpot
        
        
        
