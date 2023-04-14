from src.utils import currentMilliTime
from src.genetic.subject import Subject
from src.genetic.selection import selector
from src.genetic.mutation import mutator
from src.genetic.crossover import crossover
from src.genetic.finish_conditions import check_finished

def genetic_algorithm(palette, N, target_color, selection_type,
                      crossing_type, mutation_type, mutation_pm,
                      K, max_generations, d_error, time):
    
    end = False
    generation = 0 

    population = [] 
    for _ in range(N):
        population.append(Subject(palette, generation, target_color, None))

    for i in range(N):
        print(population[i].get_color_proportions())

    initial_time = currentMilliTime()
    current_time = currentMilliTime()

    while(not end):
        print("Generacion numero: " + str(generation))

        # Check si es necesario terminar o no
        end = check_finished(population, max_generations, d_error, time, current_time)
        
        parents = selector(population, N, K, selection_type)

        # Cruza 
        children = crossover(parents, crossing_type, palette, target_color)

        # Mutar
        # Recombinar

        # TODO: Tal vez mutar después de recombinación, chequeando generación para no mutar dos veces a parents
        mutated_children = mutator(children, mutation_type, mutation_pm)

        # Reasignar la population 
        #TODO
        
        generation += 1
        current_time = currentMilliTime() - initial_time