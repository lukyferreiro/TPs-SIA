from src.utils import get_palette, check_target_color, check_positivity
from src.genetic.genetic_algorithm import genetic_algorithm
import json

def destructre_data(data):
    palette = get_palette(data['palette_csv_path'])
    population = check_positivity(data['population'])
    max_generations= check_positivity(data['max_generations'])
    target_color = check_target_color(data['target_color'])
    selection_method = data['selection_method']
    crossing_type = data['crossing_type']
    mutation_type = data['mutation_type']
    k = check_positivity(data['k'])
    
    if not type(data['d_error']) == float or data['d_error'] < 0:
        raise ValueError("Delta error must by a positive float")
    else:
        d_error = data['d_error']
    

    return palette, population, max_generations, target_color, selection_method, crossing_type, mutation_type, k, d_error

def main(): 

    with open('./config.json', 'r') as f:
        data = json.load(f)

    palette, population, max_generations, target_color, selection_method, crossing_type, mutation_type, k, d_error = destructre_data(data)

    print(f"-------------TP2-------------\n"
          "Paleta de colores\n"
          "{palette}\n"
          "Color deseado\n"
          "{target_color}"
          )

    #todo: ver despues que sera necesario pasarle a genetic_algorithm
    #genetic_algorithm(palette, target_color, population, data)

if __name__ == "__main__":
    main()