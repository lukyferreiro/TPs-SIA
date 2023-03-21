import arcade
from src.utils import MARGIN, WIDTH, HEIGHT, get_screen_height
from src.game_state.board import Board
from src.search_methods.node import Node
from src.search_methods.algorithms import chooseAlgorithm
from src.views.resultsView import ResultsView

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
        self.visited = set()
        self.solution = []
        self.drawIndex = 0
        self.time = 0
        

    def setup(self):
        SIZE = self.window.N
        self.board = Board(SIZE, self.window.count_colors)
        self.rootNode = Node(self.board, None, 0)

        self.solution, self.visited, self.time = chooseAlgorithm(
            self.window.algorithm_type, self.window.heuristic_type,
            self.solution, self.visited, self.rootNode, self.time)
       
    def on_draw(self):
        """Render the screen """
        self.clear()
        SIZE = self.window.N
        screen_height = get_screen_height(SIZE)
        for row in range(SIZE):
            for column in range(SIZE):
                if self.drawIndex == 0:
                    color = self.board.getSquare(row, column).getColor()
                else:
                    color = self.solution[self.drawIndex].getSquare(row, column).getColor()

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = screen_height - ((MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2)
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            if self.drawIndex < len(self.solution)-1 :
                self.drawIndex += 1
                self.on_draw()
            else:
                results_view = ResultsView(self.visited, self.solution, self.time, self.board.N)
                self.window.show_view(results_view)

        if key == arcade.key.LEFT:
            if self.drawIndex > 0:
                self.drawIndex -= 1
                self.on_draw()


        if key == arcade.key.ENTER:
            results_view = ResultsView(self.visited, self.solution, self.time, self.board.N)
            self.window.show_view(results_view)