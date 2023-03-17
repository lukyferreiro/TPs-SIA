import arcade
from src.instructionView import InstructionView
from src.utils import SCREEN_TITLE, get_screen_height, get_screen_width

def main():

    row_count = int(input("BIENVENIDO A FILL ZONE, ANTES DE EMPEZAR\n\n"
                       "Ingrese el numero de filas y columnas que desee para el tablero: "))
    
    col_count = row_count

    window = arcade.Window(get_screen_width(row_count), get_screen_height(col_count), SCREEN_TITLE)
    
    #Window variables
    window.row_count = row_count
    window.col_count = col_count
    window.algorithm_type = ''
    window.heuristic_type = ''

    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()