import arcade
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell and on the edges of the screen.
MARGIN = 1

SCREEN_TITLE = "FillZone"

# Colors
COLORS = {
    0: arcade.color.BLUE,
    1: arcade.color.GREEN,
    2: arcade.color.RED,
    3: arcade.color.YELLOW,
    4: arcade.color.PURPLE,
    5: arcade.color.ORANGE
}


# Do the math to figure out our screen dimensions
def get_screen_width(col_count):
    return (WIDTH + MARGIN) * col_count + MARGIN


def get_screen_height(row_count):
    return (HEIGHT + MARGIN) * row_count + MARGIN


def get_dimensions(visited):
    dim = ''
    dim += str(visited[0].getState().N)
    dim += 'x'
    dim += str(visited[0].getState().N)
    return dim


def get_frontier_nodes(visited):
    total = 0
    for state in visited:
        total += len(state.getNeighbors())
    return total


def get_solution_steps(visited):
    steps = ''
    for node in visited:
        steps += steps[node.getState().getPlayerColor()]
        if node != visited[len(visited) - 1]:
            steps += ' ---> '
    return steps


def print_all(visited):
    turns = []
    cmap = ListedColormap(visited[0].getState().getColorDict().keys())
    for node in visited:
        grid = node.getState().getGrid()
        dimension = node.getState().N
        matrix = np.zeros(dimension * dimension, dtype=int)
        matrix = matrix.reshape((dimension, dimension))
        for i in range(dimension):
            for j in range(dimension):
                matrix[i][j] = grid[i][j].tileColor
        turns.append(matrix)
        plt.matshow(matrix, cmap=cmap, vmin=0, vmax=len(visited[0].getState().getColorDict().keys()) - 1)
        plt.show()
