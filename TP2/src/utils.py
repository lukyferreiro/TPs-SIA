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

def get_target_color() -> np.ndarray:

    print("Ingrese el color objetivo en formato RGB:")
    R = input("R: ")
    while not R.isdigit() or int(R) < 0 or int(R) > 255:
        R = input("Proporcion invalida\nR:")
    G = input("G: ")
    while not G.isdigit() or int(G) < 0 or int(G) > 255:
        G = input("Proporcion invalida\nG:")
    B = input("B: ")
    while not B.isdigit() or int(B) < 0 or int(B) > 255:
        B = input("Proporcion invalida\nB:")
  
    return np.array([int(R),int(G),int(B)])
