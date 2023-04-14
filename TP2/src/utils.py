import numpy as np
from csv import reader
import time

def currentMilliTime():
    return round(time.time() * 1000)

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
          raise ValueError("El color objetivo debe ser un arreglo [R,G,B] con valores entre 0 y 255")
  
    return color 

def check_positivity(num, str):
   if not type(num) == int or num < 0:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return num

def check_prob(num, str):
   if not type(num) == float or num < 0 or num > 1:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return num

def check_type(type, array, str):
   if type not in array:
      raise ValueError(f"Valor de {str} invalido")
   
   return type

def destructure_data(data):
    palette = get_palette(data['palette_csv_path'])
    N = check_positivity(data['N'], "N (poblacion)")
    target_color = check_target_color(data['target_color'])
    selection_type = check_type(data['selection_type'], data['selection_options'], "seleccion")
    crossing_type = check_type(data['crossing_type'], data['crossing_options'], "cruza")
    mutation_type = check_type(data['mutation_type'], data['mutation_options'], "mutacion")
    mutation_pm = check_prob(data['mutation_pm'], "Pm")
    select_new_generation_type = check_type(data['select_new_generation_type'], data['select_new_generation_options'], "seleccion de nueva generacion")
    K = check_positivity(data['K'], "K (indiviudos a seleccionar)")
    max_generations= check_positivity(data['max_generations'], "generaciones maximas")
    d_error = check_prob(data['d_error'], "delta de error minimo")
    time = check_positivity(data['time'], "tiempo maximo")
    
    return palette, N, target_color, selection_type, crossing_type, mutation_type, mutation_pm, select_new_generation_type, K, max_generations, d_error, time