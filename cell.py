class Cell:
    def __init__(self, x, y):
        self.x = x  # X coordinate on grid
        self.y = y  # Y coordinate on grid
        self.wallAbove = False  # No walls on default
        self.wallBelow = False
        self.wallRight = False
        self.wallLeft = False
        self.visited = False  
