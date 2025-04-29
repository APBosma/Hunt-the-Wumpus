import unittest
from character import Character

class TestWumpus(unittest.TestCase):
    
    def setUp(self):
        self.game = Character()
        
        
        
    # Test getters
    def testLocation(self):
        self.assertEqual("1", self.game.getLocation())
        
    def testArrows(self):
        self.assertEqual(5, self.game.getArrows())
        
        
        
    # Testing movement, moveRooms(self, possibleRooms)
#     def testMovement(self):
#         self.game.moveRooms(["2", "3", "4"])
#         if self.game.getLocation() not in ["2", "3", "4"]:
#             success = False
#         else:
#             success = True
#         self.assertEqual(success, True)
    
    
    
    # Testing wumpus, rollWumpus(self, wumpusLocation, possibleLocations)
    # Wumpus doesn't move
    def testWumpusNothing(self):
        self.game.setLocation("1")
        self.assertEqual(self.game.rollWumpus("2", ["3","4","5"]), "2")
        
    # Hit wumpus
    def testWumpusMoveKill(self):
        roll = self.game.rollWumpus("1", ["3","4","5"])
        if roll in ["3", "4", "5", "21"]:
            success = True
        else:
            sucess = False
        self.assertEqual(success, True)
        
        
        
    # Test shooting, shootArrow(self, room, possibleRooms, wumpus)
    def testShootingWin(self):
        self.assertEqual("win", self.game.shootArrow("3", ["3", "5", "6"], "3"))
        
    def testShootingLose(self):
        self.assertEqual("no win", self.game.shootArrow("3", ["3", "5", "6"], "100"))
        
    
    
    # Test set Location, setLocation(self, newSpot)
    def locationChange(self):
        self.game.setLocation("12")
        self.assertEqual("12", self.game.getLocation())
        
        
        
if __name__ == '__main__':
    unittest.main()