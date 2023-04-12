import numpy as np
from csv import reader

"""
Implementar metodos de combinar colores
"""

def get_palette(path) -> np.ndarray:
  file = open(path)
  csvreader = reader(file)
  colores = []

  for row in csvreader:
    r, g, b = (int(x) for x in row)
    colores.append( [r, g, b] )

  return np.array(colores)