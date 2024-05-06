from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

matrix = [
  [1, 1, 1, 1, 1, 1],
  [1, 0, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1]]
  
# 1. create a grid
grid = Grid(matrix = matrix)

# 2. create a start cell and end cell
start = grid.node(0, 0)
end = grid.node(5, 2)

# 3. create a finder with the movement style 
finder = AStarFinder(diagonal_movement = DiagonalMovement.always) 

# 4. returns a list with the path and the amount of times the finder had to run to get the path 
path,runs = finder.find_path(start, end, grid)

# print the result 
print(path)
print(runs)

