import arcade
import random
from src.utils import MARGIN, WIDTH, HEIGHT, COLORS
from src.game_state.board import Board
from src.search_methods.node import Node
from src.utils import COLORS

""" Main application class. """
class FillZone(arcade.View):
   
    def __init__(self):
        """ Set up the application. """

        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        print(self.window.algorithm_type)
        print(self.window.heuristic_type)

        self.board = None
        self.rootNode = None
        

    def setup(self):
        SIZE = self.window.N
        self.board = Board(SIZE, COLORS)
        self.rootNode = Node(self.board, None)


    def on_draw(self):
        """Render the screen """
        self.clear()
        SIZE = self.window.N
        for row in range(SIZE):
            for column in range(SIZE):
                color = self.board.getSquare(row, column).getColor()

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


    def on_key_press(self, key, modifiers):
        #This is an example of how to re-draw the view
        if key == arcade.key.RIGHT:
            #Ejecutar codigo dependiendo algoritmo y heuristica
            self.on_draw()
