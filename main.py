import pygame
import sys
from cell import Cell
from player import Player
from move import Move
from draw import drawDefault
from draw import drawLine
from draw import deleteLine
from maze_generator import MazeGenerator

pygame.init()

# Basics window constants
HEIGHT = 825
WIDTH = 825
CELL_SIDE_LENGTH = 25
CELLS_PER_SIDE = 33

SIDEBAR_WIDTH = 250
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20

# Basic game constants and variables
WIN_POS_X = 16
WIN_POS_Y = 32
gameEnded = False

screen = pygame.display.set_mode((WIDTH + SIDEBAR_WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Set up the grid of cells (2D list, 33x33)
theGrid = [[Cell(x, y) for y in range(CELLS_PER_SIDE)] for x in range(CELLS_PER_SIDE)]
for x in range(CELLS_PER_SIDE):
    for y in range(CELLS_PER_SIDE):
        theGrid[x][y].x = x 
        theGrid[x][y].y = y 


def drawButton(width, height, x, y, name):
    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (100, 100, 100), button)
    font = pygame.font.Font(None, 24)
    text_surface = font.render(name, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=button.center)
    screen.blit(text_surface, text_rect)
    return button

quitButton = drawButton(BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 100, "Quit")
defaultButton = drawButton(BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 775, "Default")
customButton = drawButton(BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 700, "Custom")


def drawBackground(gameStarted, gameDefault, isGenerated, generated):
    screen.fill((255, 255, 255)) # Makes it white

    # Sidebar
    pygame.draw.rect(screen, (200, 200, 200), (WIDTH, 0, SIDEBAR_WIDTH, HEIGHT))
    pygame.draw.circle(screen, (255, 0, 0), (16 * CELL_SIDE_LENGTH + (CELL_SIDE_LENGTH // 2) + 1, 32 * CELL_SIDE_LENGTH + (CELL_SIDE_LENGTH // 2)), CELL_SIDE_LENGTH // 2 - 1)
    if gameStarted:
        quitButton = drawButton(BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 100, "Quit")
        if gameDefault:
            # Draw vertical grid lines and update cell wall flags    
            drawDefault(theGrid, screen)
        elif isGenerated:
            for x in range(CELLS_PER_SIDE):
                for y in range(CELLS_PER_SIDE):
                    cell = theGrid[x][y]
                    if y > 0:  # Draw line to the cell above
                        drawLine(cell, theGrid[x][y - 1], screen)
                    if x > 0:  # Draw line to the cell to the left
                        drawLine(cell, theGrid[x - 1][y], screen)

            for x in generated:
                deleteLine(x[0], x[1], screen)
            

    else:
        defaultButton = drawButton(BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 775, "Default")
        customButton = drawButton(BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 700, "Custom")
        quitButton = drawButton(BUTTON_WIDTH, BUTTON_HEIGHT, WIDTH + (200 - BUTTON_WIDTH), HEIGHT - 100, "Quit")


drawBackground(False, False, False, [])

# Initialize and draws the Player
player = Player(16, 0) # 16, 0 should be top middle
new_x = player.x * CELL_SIDE_LENGTH + (CELL_SIDE_LENGTH // 2) + 1
new_y = player.y * CELL_SIDE_LENGTH + (CELL_SIDE_LENGTH // 2)
pygame.draw.circle(screen, (0, 0, 0), (new_x, new_y), CELL_SIDE_LENGTH // 2 - 1)

won = False

def runGame():
    # Running the actual game
    running = True
    gameStarted = False
    gameDefault = False

    mazeGenerated = False
    mazeGenerator = MazeGenerator(theGrid, CELL_SIDE_LENGTH, CELLS_PER_SIDE, screen)
    generated = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN and gameStarted:
                # Move the player using arrow keys
                if event.key == pygame.K_UP:
                    if player.y > 0:
                        if player.canMakeMove(theGrid[player.x][player.y], Move.UP):
                            player.moveUp()
    
                elif event.key == pygame.K_DOWN:
                    if player.y < CELLS_PER_SIDE - 1:
                        if player.canMakeMove(theGrid[player.x][player.y], Move.DOWN):
                            player.moveDown()
        
                elif event.key == pygame.K_LEFT:
                    if player.x > 0:
                        if player.canMakeMove(theGrid[player.x][player.y], Move.LEFT):
                            player.moveLeft()  
        
                elif event.key == pygame.K_RIGHT:
                    if player.x < CELLS_PER_SIDE - 1:
                        if player.canMakeMove(theGrid[player.x][player.y], Move.RIGHT):
                            player.moveRight() 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # For game buttons
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if quitButton.collidepoint(pos):
                        sys.exit()
                    elif defaultButton.collidepoint(pos) and (not gameStarted):
                        gameStarted = True
                        gameDefault = True
                    elif customButton.collidepoint(pos) and (not gameStarted):
                        gameStarted = True
                        gameDefault = False
                        if not mazeGenerated:
                            mazeGenerator.generate_maze(16, 0, generated)
                            mazeGenerated = True
 
            drawBackground(gameStarted, gameDefault, mazeGenerated, generated)
            new_x = player.x * CELL_SIDE_LENGTH + (CELL_SIDE_LENGTH // 2) + 1
            new_y = player.y * CELL_SIDE_LENGTH + (CELL_SIDE_LENGTH // 2)
            pygame.draw.circle(screen, (0, 0, 0), (new_x, new_y), CELL_SIDE_LENGTH // 2 - 1)

            # Check if player has won the game
            if player.x == WIN_POS_X and player.y == WIN_POS_Y:
                gameEnded = True
                running = False
                break

        pygame.display.flip()

runGame()