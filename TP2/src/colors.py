import math 

"""
Implementar metodos de combinar colores
"""

#TODO chequear si funciona usar este calculo de distancia https://www.compuphase.com/cmetric.htm
#en vez de realizar la distancia "normal"
def get_distance_between_colors(c1, c2):
  r1, g1, b1 = c1
  r2, g2, b2 = c2

  d_r = r1 - r2
  d_g = g1 - g2
  d_b = b1 - b2
  
  d = math.sqrt( (d_r**2) + (d_g**2) + (d_b**2) )

  return d

MAX_DISTANCIA = get_distance_between_colors((0,0,0), (255,255,255))