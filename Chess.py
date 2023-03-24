import array as arr



def board():
    BOARD = arr.array('i'[1])

class pieces():
    def __innit__(self, position, name, movement):
        self.position = position
        self.name = name
        self.movement = movement 
#position2 är positionen efter att pjäsen har rört sig 
    def move(self, position2):
        self.position = position2 
        
class King(pieces): 
    def __innit__(self,movementK):
        super().__innit__(position,name)
        self.movementK = movementK
    def movement()
class Queen(pieces):
    
class Pawn(pieces):
    
class Bishop(pieces):
    
class Knight(pieces): 
        