# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 1

SCREEN_TITLE = "FillZone"

# Do the math to figure out our screen dimensions

def get_screen_width(col_count):
    return (WIDTH + MARGIN) * col_count + MARGIN


def get_screen_height(row_count):
    return (HEIGHT + MARGIN) * row_count + MARGIN
