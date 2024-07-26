import random
from cell import Cell
from draw import drawLine
from draw import deleteLine

class MazeGenerator:
    def __init__(self, grid, cell_side_length, cells_per_side, screen):
        self.grid = grid
        self.cell_side_length = cell_side_length
        self.cells_per_side = cells_per_side
        self.screen = screen

    def generate_maze(self, startX, startY, generated):
        # Initialize the grid with walls and draw the walls
        for x in range(self.cells_per_side):
            for y in range(self.cells_per_side):
                cell = self.grid[x][y]
                if y > 0:  # Draw line to the cell above
                    drawLine(cell, self.grid[x][y - 1], self.screen)
                if x > 0:  # Draw line to the cell to the left
                    drawLine(cell, self.grid[x - 1][y], self.screen)

        start_cell = self.grid[startX][startY]
        start_cell.visited = True
        walls = self.get_cell_walls(start_cell)
        
        while walls:
            wall = random.choice(walls)
            cell1, cell2 = wall
            
            if cell2 is not None and not cell2.visited:
                deleteLine(cell1, cell2, self.screen)
                generated.append([cell1, cell2])
                
                cell2.visited = True
                walls.extend(self.get_cell_walls(cell2))
            walls.remove(wall)

    def get_cell_walls(self, cell):
        walls = []
        x, y = cell.x, cell.y
        if y > 0:
            walls.append((cell, self.grid[x][y - 1]))
        if y < self.cells_per_side - 1:
            walls.append((cell, self.grid[x][y + 1]))
        if x > 0:
            walls.append((cell, self.grid[x - 1][y]))
        if x < self.cells_per_side - 1:
            walls.append((cell, self.grid[x + 1][y]))
        return walls
    