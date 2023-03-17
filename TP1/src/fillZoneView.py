import arcade
import random
from src.utils import MARGIN, WIDTH, HEIGHT

# Colors
COLORS = [
    arcade.color.BLUE,
    arcade.color.GREEN,
    arcade.color.RED,
    arcade.color.YELLOW,
    arcade.color.PURPLE,
    arcade.color.ORANGE,
]

class FillZone(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """
        Set up the application.
        """

        super().__init__()
        print(self.window.algorithm_type)
        print(self.window.heuristic_type)
        self.grid = None

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        COLUMN_COUNT = self.window.col_count
        ROW_COUNT = self.window.row_count
        # Create a 2 dimensional array. A two-dimensional
        self.grid = [[None for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row][column] = random.choice(COLORS)  # Append a cell

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        COLUMN_COUNT = self.window.col_count
        ROW_COUNT = self.window.row_count

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                color = self.grid[row][column]

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            self.setup()
        #This is an example of how to re-draw the view
        elif key == arcade.key.F:
            self.grid[9][0] = arcade.color.PURPLE
            self.on_draw()
