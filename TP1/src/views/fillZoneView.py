import arcade
import random
from src.utils import MARGIN, WIDTH, HEIGHT, COLORS
from src.game_state.board import Board
from src.search_methods.node import Node
from src.utils import COLORS
from src.search_methods.algorithms import bfs

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
                print('Solucion con BFS papa')
                self.on_draw()
                #TODO: check tiempo que tarda para tableros más grandes
                self.solution = bfs(self.visited, self.rootNode)
                print('Solucion lista')

                #Codigo bfs
        #     case 'DFS':
        #         #
        #     case 'GREEDY':
        #         #
        #     case 'A*':
        #
        #     case _:

    def on_draw(self):
        """Render the screen """
        self.clear()
        SIZE = self.window.N
        for row in range(SIZE):
            for column in range(SIZE):
                # color = self.board.getSquare(row, column).getColor()
                if len(self.solution) == 0:
                    color = self.board.getSquare(row, column).getColor()
                else:
                    color = self.solution[self.drawIndex].getSquare(row, column).getColor()

                # Do the math to figure out where the box is

                #TODO: check dibujo de abajo-izquierda -> arriba-derecha
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT and self.drawIndex < len(self.solution):
        # if key == arcade.key.RIGHT :
            self.on_draw()
            self.drawIndex += 1
            # Imprimir un resumen de los pasos.
            # Pasos
            # Nodos expandidos
            # Nodos frontera
            # Solución --> array mostrando los colores elegidos
            # Tiempo de Procesamiento
