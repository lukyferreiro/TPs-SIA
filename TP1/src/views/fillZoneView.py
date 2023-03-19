import arcade
from src.utils import MARGIN, WIDTH, HEIGHT, COLORS, get_screen_height, currentMilliTime
from src.game_state.board import Board
from src.search_methods.node import Node
from src.search_methods.algorithms import bfs, dfs, greedy, astar
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
        self.visited = []
        self.solution = []
        self.drawIndex = 0
        self.time = 0
        self.bfs = False
        

    def setup(self):
        SIZE = self.window.N
        self.board = Board(SIZE, COLORS)
        self.rootNode = Node(self.board, None)

        #TODO: check tiempo que tarda para tableros más grandes
        match self.window.algorithm_type:
            case 'BFS':
                print('Solucion con BFS')
                self.on_draw()
                self.bfs = True
                t0 = currentMilliTime()
                self.solution = bfs(self.visited, self.rootNode)
                self.time = currentMilliTime() - t0
                print('Solucion lista')
            case 'DFS':
                print('Solucion con DFS')
                self.on_draw()
                t0 = currentMilliTime()
                self.solution = dfs(self.visited, self.rootNode)
                self.time = currentMilliTime() - t0
                print('Solucion lista')
            case 'GREEDY':
                print('Solucion con GREEDY')
                self.on_draw()
                t0 = currentMilliTime()
                self.solution = greedy(self.visited, self.rootNode)
                self.time = currentMilliTime() - t0
                print('Solucion lista')
            case 'A*':
                print('Solucion con A*')
                self.on_draw()
                t0 = currentMilliTime()
                self.solution = astar(self.visited, self.rootNode)
                self.time = currentMilliTime() - t0
                print('Solucion lista')
       

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

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT :
            if self.drawIndex < len(self.solution)-1 :
                self.on_draw()
                self.drawIndex += 1
            else:
                results_view = ResultsView(self.visited, self.solution, self.time, self.bfs)
                self.window.show_view(results_view)