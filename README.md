<h1>Maze Game</h1> 
<a href="https://skillicons.dev"> <img src="https://skillicons.dev/icons?i=python"/> </a>
<p> This game is built using Python's Pygame library. It features a maze based on a 32x32 grid of cell objects and the lines between some of them that stop the player from going in their direction. Players must navigate through these lines to reach the red circle at 
the bottom of the maze. On the sidebar, players can choose whether they want to play on the default or custom-generated maze. </p>

<h2>Custom Maze Generation</h2>
<p> The custom maze generation uses Prim's algorithm, a popular method for creating mazes. The algorithm starts by initializing a grid of cells where each cell is surrounded by walls. Next, it chooses a random cell and adds all of its adjacent walls to a list. The algorithm then randomly selects a wall from this list and checks the cell on the other side of it. If this cell has not been visited yet, then the wall between this cell and the earlier cell will be removed. The newly visited cell's walls are added to the list. This process repeats until all cells are visited, which means we then have a fully generated maze with a path from start to finish. The actual visual representation of the walls is done using Python's Pygame library. </p>
