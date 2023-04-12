import math 
import numpy as np

# Formula found at https://www.compuphase.com/cmetric.htm
# More accurate comparison than linear distance between two 3D points
def get_distance_between_colors(c1, c2):
  r1, g1, b1 = c1
  r2, g2, b2 = c2

  rmean = (r1 + r2) / 2

  d_r = r1 - r2
  d_g = g1 - g2
  d_b = b1 - b2
  
  return math.sqrt( ((2+(rmean/256))*(d_r**2)) + (4*(d_g**2)) + ((2+((255-rmean)/256))*(d_b**2)) )

MAX_DISTANCE = get_distance_between_colors((0,0,0), (255,255,255))

def mix_color(color_proportions, palette) -> np.ndarray:
  total_proportion = np.sum(color_proportions)

  r = round(np.sum(palette[:, 0] * color_proportions) / total_proportion)
  g = round(np.sum(palette[:, 1] * color_proportions) / total_proportion)
  b = round(np.sum(palette[:, 2] * color_proportions) / total_proportion)

  return np.array([r,g,b])