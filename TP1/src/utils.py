import arcade
import time
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

COLORS_2 = {
    arcade.color.BLUE : 'blue',
    arcade.color.GREEN: 'green',
    arcade.color.RED: 'red',
    arcade.color.YELLOW: 'yellow',
    arcade.color.PURPLE: 'purple',
    arcade.color.ORANGE: 'orange'
}


# Do the math to figure out our screen dimensions
def get_screen_width(col_count):
    return (WIDTH + MARGIN) * col_count + MARGIN


def get_screen_height(row_count):
    return (HEIGHT + MARGIN) * row_count + MARGIN

def currentMilliTime():
    return round(time.time() * 1000)

def get_dimensions(visited):
    dim = ''
    dim += str(visited[0].getBoard().N)
    dim += 'x'
    dim += str(visited[0].getBoard().N)
    return dim


def get_frontier_nodes(visited):
    total = 0
    for state in visited:
        total += len(state.getChildren())
    return total


def get_solution_steps(visited):
    steps = ''
    for node in visited:
        steps += transform_color(node.getBoard().getPlayerColor())
        if node != visited[len(visited) - 1]:
            steps += ' ---> '
    return steps

def transform_color(arcade_color):
    for color in COLORS_2.keys():
        if arcade_color == color:
            return COLORS_2[color]
