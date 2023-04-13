from src.utils import get_palette, check_target_color, check_positivity, destructure_data
from src.genetic.genetic_algorithm import genetic_algorithm
import json

def main(): 

    with open('./config.json', 'r') as f:
        data = json.load(f)

    palette, population, max_generations, target_color, selection_method, crossing_type, mutation_type, k, d_error = destructure_data(data)

    print("-------------TP2-------------\n"
          "Paleta de colores\n"
          f"{palette}\n"
          "Color deseado\n"
          f"{target_color}"
          )

    #todo: ver despues que sera necesario pasarle a genetic_algorithm
    genetic_algorithm( palette, population, max_generations, target_color, selection_method, crossing_type, mutation_type, k, d_error)

if __name__ == "__main__":
    main()