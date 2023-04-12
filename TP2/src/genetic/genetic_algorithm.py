import numpy as np
from src.genetic.subject import Subject

def genetic_algorithm(palette, target_color, N):

    end = False
    generation = 0 
    prueba = Subject(palette, generation, target_color)

    population = [] 

    for _ in range(N):
      population.append(Subject(palette, generation, target_color))

    while(not end):
      print("Generacion numero: " + str(generation))

        # Check si es necesario terminar o no
        

        # Selector

        # Cruza 

        # Mutar

        # Reasignar la population 
        
     #   generation += 1