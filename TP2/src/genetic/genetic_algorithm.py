import numpy as np
from src.genetic.subject import Subject
from src.genetic.selection import selector
from src.genetic.crossover import crossover

def genetic_algorithm(palette, N, max_generations, target_color, selection_method, crossing_type, mutation_type, K, d_error):
    end = False
    generation = 0 

    population = [] 

    for _ in range(N):
        population.append(Subject(palette, generation, target_color, None))

    for i in range(N):
        print(population[i].get_color_proportions())

    while(not end):
        print("Generacion numero: " + str(generation))

        # Check si es necesario terminar o no
        
        parents = selector(population, N, K, selection_method)
        # Print fitness of selected individuals

        # Cruza 
        children = crossover(parents, crossing_type, palette, target_color)

        for i in range(N):
            print(children[i].get_color_proportions())

        # Mutar

        # Reasignar la population 
        
        generation += 1
        end = True