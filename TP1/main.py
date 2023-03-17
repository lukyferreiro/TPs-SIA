import arcade
from src.views.instructionView import InstructionView
from src.utils import SCREEN_TITLE, get_screen_height, get_screen_width

def main():

    N = -1
    N = int(input("BIENVENIDO A FILL ZONE\n\n"
                       "Ingrese el numero de filas y columnas que desee para el tablero: "))
    
    while N <= 3:
        N = int(input("El valor ingresado no es valido. Ingrese un numero entero mayor a 4"))
    
    window = arcade.Window(get_screen_width(N), get_screen_height(N), SCREEN_TITLE)
    
    #Window variables
    window.N = N
    window.algorithm_type = ''
    window.heuristic_type = ''

    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()