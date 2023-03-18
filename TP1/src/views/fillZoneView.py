import arcade
import random
from src.utils import MARGIN, WIDTH, HEIGHT, COLORS
from src.game_state.board import Board
from src.search_methods.node import Node
from src.utils import COLORS
from src.utils import get_screen_height
from src.search_methods.algorithms import bfs
from src.search_methods.algorithms import dfs
from TP1.src.utils import get_frontier_nodes, get_dimensions, get_solution_steps, print_all

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
        

    def setup(self):
        SIZE = self.window.N
        self.board = Board(SIZE, COLORS)
        self.rootNode = Node(self.board, None)

        #
        match self.window.algorithm_type:
            case 'BFS':
                print('Solucion con BFS')
                self.on_draw()
                #TODO: check tiempo que tarda para tableros más grandes
                self.solution = bfs(self.visited, self.rootNode)
                print('Solucion lista')
            case 'DFS':
                print('Solucion con DFS')
                self.on_draw()
                # TODO: check tiempo que tarda para tableros más grandes
                self.solution = dfs(self.visited, self.rootNode)
                print('Solucion lista')
        #     case 'GREEDY':
        #         #
        #     case 'A*':
        #
        #     case _:

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
        if key == arcade.key.RIGHT and self.drawIndex < len(self.solution) -1 :
            self.on_draw()
            self.drawIndex += 1
        # else:

            # Imprimir un resumen de los pasos.
            # Pasos
            # Nodos expandidos
            # Nodos frontera
            # Solución --> array mostrando los colores elegidos
            # Tiempo de Procesamiento



        def show_data(visited, time, solution, bfs, plot):
            print('board dimension: ', get_dimensions(visited))
            print('result: success')
            if bfs:
                print('solution cost: ', len(solution), ' turns')
            else:
                print('solution cost: ', len(visited), ' turns')
            print('frontier nodes: ', get_frontier_nodes(visited), ' nodes')
            print('expanded nodes: ', len(visited), ' nodes')
            print('processing time: ', time, ' ms')
            if bfs:
                print('solution steps:\n', get_solution_steps(solution))
                if plot == 1:
                    print_all(solution)
            else:
                print('solution steps:\n', get_solution_steps(visited))
                if plot == 1:
                    print_all(visited)
