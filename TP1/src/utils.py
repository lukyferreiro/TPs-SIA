import arcade

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell and on the edges of the screen.
MARGIN = 1

SCREEN_TITLE = "FillZone"

# Colors
COLORS = {
    arcade.color.BLUE: 0,
    arcade.color.GREEN: 1,
    arcade.color.RED: 2,
    arcade.color.YELLOW: 3,
    arcade.color.PURPLE: 4,
    arcade.color.ORANGE: 5,
}

# Do the math to figure out our screen dimensions
def get_screen_width(col_count):
    return (WIDTH + MARGIN) * col_count + MARGIN


def get_screen_height(row_count):
    return (HEIGHT + MARGIN) * row_count + MARGIN
