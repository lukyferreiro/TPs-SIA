import arcade
import time

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell and on the edges of the screen.
MARGIN = 1

SCREEN_TITLE = "FillZone"

COLORS = {
    0: arcade.color.BLUE,
    1: arcade.color.GREEN,
    2: arcade.color.RED,
    3: arcade.color.YELLOW,
    4: arcade.color.PINK,
    5: arcade.color.ORANGE,
    6: arcade.color.VIOLET,
    7: arcade.color.AQUA,
    8: arcade.color.WHITE
}

COLORS_2 = {
    arcade.color.BLUE : 'B',
    arcade.color.GREEN: 'G',
    arcade.color.RED: 'R',
    arcade.color.YELLOW: 'Y',
    arcade.color.PINK: 'P',
    arcade.color.ORANGE: 'O',
    arcade.color.VIOLET: 'V',
    arcade.color.AQUA: 'A',
    arcade.color.WHITE: 'W'
}


# Do the math to figure out our screen dimensions
def get_screen_width(col_count):
    return (WIDTH + MARGIN) * col_count + MARGIN


def get_screen_height(row_count):
    return (HEIGHT + MARGIN) * row_count + MARGIN

def currentMilliTime():
    return round(time.time() * 1000)

def get_frontier_nodes(visited):
    total = 0
    for state in visited:
        total += len(state.getChildren())
    return total


def get_solution_steps(solution):
    steps = ''
    for node in solution:
        steps += transform_color(node.getBoard().getPlayerColor())
        if node != solution[len(solution) - 1]:
            steps += ' -> '
    return steps

def transform_color(arcade_color):
    for color in COLORS_2.keys():
        if arcade_color == color:
            return COLORS_2[color]
