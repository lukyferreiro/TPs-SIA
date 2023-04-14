import numpy as np
import math
from src.genetic.subject import Subject

def crossover(parents, crossover_method, palette, target_color):
    switcher = {
        "ONE_POINT": cross_one_point,
        "DOUBLE_POINT": cross_double_point,
        "ANGULAR": cross_angular,
        "UNIFORM": cross_uniform,
    }

    cross_selected = switcher.get(crossover_method, "Metodo de cruza invalido")

    children = []
    for i in range(0, len(parents) // 2 + 1, 2):
        child1, child2 = cross_selected(parents[i], parents[i+1], palette, target_color)
        children.append(child1)
        children.append(child2)

    return children
 

"""
Se elige un locus al azar y se intercambian los alelos a partir de ese
locus. Sea S la cantidad de genes:
P=[0,S-1]
"""
def cross_one_point(parent1, parent2, palette, target_color):
    color_props1 = parent1.get_color_proportions()
    color_props2 = parent2.get_color_proportions()
    generation = parent1.get_generation() + 1 

    S = len(color_props1)
    P = np.random.default_rng().integers(0, S-1)

    child1_props = np.concatenate((color_props1[:P], color_props2[P:]), axis=0)
    child2_props = np.concatenate((color_props2[:P], color_props1[P:]), axis=0)

    child1 = Subject(palette, generation, target_color, child1_props)
    child2 = Subject(palette, generation, target_color, child2_props)

    return child1, child2


"""
Se elige dos locus al azar y se intercambian los alelos entre ellos. 

P_1=[0,S-1]  P_2=[0,S-1] ; P_1 <= P_2
"""
def cross_double_point(parent1, parent2, palette, target_color):
    color_props1 = parent1.get_color_proportions()
    color_props2 = parent2.get_color_proportions()
    generation = parent1.get_generation() + 1 

    S = len(color_props1)
    P1, P2 = np.sort(np.random.default_rng().integers(0, S-1, size=2))

    child1_props = np.concatenate((color_props1[:P1], color_props2[P1:P2], color_props1[P2:]), axis=0)
    child2_props = np.concatenate((color_props2[:P1], color_props1[P1:P2], color_props2[P2:]), axis=0)

    child1 = Subject(palette, generation, target_color, child1_props)
    child2 = Subject(palette, generation, target_color, child2_props)

    return child1, child2

"""
Se elige un locus al azar P y una longitud L. 
Se intercambia el segmento de longitud L a partir de P.

P=[0,S-1] L=[0, ⌈ S/2 ⌉]
"""
def cross_angular(parent1, parent2, palette, target_color):
    color_props1 = parent1.get_color_proportions()
    color_props2 = parent2.get_color_proportions()
    generation = parent1.get_generation() + 1 

    S = len(color_props1)
    L = np.random.default_rng().integers(0, math.ceil(S/2))
    P = np.random.default_rng().integers(0, S-1)
    
    end_index = (P + L) % S  # calculate end index, wrapping around to the beginning if necessary
    
    # TODO : fix 
    color_props1[P:end_index], arr2[P:end_index] = arr2[P:end_index], color_props1[P:end_index]  # exchange elements between arrays
    
    child1 = Subject(palette, generation, target_color, [color_props1[:P1], color_props2[P1:P2], color_props1[P2:]])
    child2 = Subject(palette, generation, target_color, [color_props2[:P1], color_props1[P1:P2], color_props2[P2:]])

    return child1, child2

"""
Se produce un intercambio de alelos en cada gen con probabilidad P en [0,1]. 
Por lo general P=0,5.
- >: Se mantienen los alelos
- <: Se intercambian los alelos
"""
def cross_uniform(parent1, parent2, palette, target_color):
    color_props1 = parent1.get_color_proportions()
    color_props2 = parent2.get_color_proportions()
    length = len(color_props1)
    
    generation = parent1.get_generation() + 1
    ps = np.random.default_rng().uniform(0., 1., size=length)
  
    child1_props = []
    child2_props = []
    for i in range(length):
        if(ps < 0.5):
            child1_props.append(color_props2[i])
            child2_props.append(color_props1[i])
        else:
            child1_props.append(color_props1[i])
            child2_props.append(color_props2[i])

    child1 = Subject(palette, generation, target_color, child1_props)
    child2 = Subject(palette, generation, target_color, child2_props)

    return child1, child2