import arcade
from src.instructionView import InstructionView
from src.utils import SCREEN_TITLE, get_screen_height, get_screen_width

def main():

    row_num = int(input("BIENVENIDO A FILL ZONE, ANTES DE EMPEZAR\n\n"
                       "Ingrese el numero de filas que desee para el tablero: "))
    col_num = int(input("Ingrese el numero de columnas que desee para el tablero: "))

    

    window = arcade.Window(get_screen_width(row_num), get_screen_height(col_num), SCREEN_TITLE)
    start_view = InstructionView()
    window.algorithm_type = 0
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()