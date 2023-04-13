import numpy as np
from src.genetic.subject import Subject
from src.genetic.selection import selector

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
        
        K = 10  #TODO agregar al config.json
        # Selector
        parents = selector(population, N, K, "ELITE")
        # Print fitness of selected individuals

        # Cruza 

        # Mutar

        # Reasignar la population 
        
        generation += 1
        end = True