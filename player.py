from cell import Cell
from move import Move

class Player:
    def __init__(self, x, y):
        self.x = x # X coordinate on grid
        self.y = y # Y coordinate on grid

    def moveRight(self): 
        self.x += 1
    
    def moveLeft(self):
        self.x -= 1
    
    def moveUp(self):
        self.y -= 1

    def moveDown(self):
        self.y += 1

    # Takes its occupied cell, and move type as a parameter
    def canMakeMove(self, itsCell, moveType):
        if moveType == Move.UP:
            if itsCell.wallAbove:
                return False
        elif moveType == Move.DOWN:
            if itsCell.wallBelow:
                return False
        elif moveType == Move.LEFT:
            if itsCell.wallLeft:
                return False
        elif moveType == Move.RIGHT:
            if itsCell.wallRight:
                return False
        return True
