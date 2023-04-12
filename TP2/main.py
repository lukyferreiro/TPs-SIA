from src.colors import get_palette
from src.utils import get_target_color
from src.genetic_algorithm import genetic_algorithm

def main(): 
    print("-------------TP2-------------")
    palette = get_palette("./src/colores.csv")
    print("Paleta de colores")
    print(palette)

    target_color = get_target_color()
    print(target_color)

    # Llamar a función que corra el algoritmo de aprendizaje genético
    N = 100     # Poblacion
    genetic_algorithm(palette, target_color, N)

if __name__ == "__main__":
    main()