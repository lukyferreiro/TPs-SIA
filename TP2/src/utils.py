import numpy as np
from csv import reader

def get_palette(path) -> np.ndarray:
  file = open(path)
  csvreader = reader(file)
  colores = []

  for row in csvreader:
    r, g, b = (int(x) for x in row)
    colores.append( [r, g, b] )

  return np.array(colores)   

def check_target_color(color):
    
    for i in range(len(color)):
       if not type(color[i])==int or color[i] < 0 or color[i] > 255:
          raise ValueError("The target color must be a number between 0 and 255 ")
  
    return color 

def check_positivity(num):
   if not type(num) == int or num < 0:
      raise ValueError("An invalid data on config was assigned")
   
   return num

def destructure_data(data):
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