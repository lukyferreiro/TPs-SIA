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