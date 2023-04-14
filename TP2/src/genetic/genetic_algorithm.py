from src.genetic.subject import Subject
from src.genetic.selection import selector
from src.genetic.mutation import mutator
from src.genetic.crossover import crossover
from src.genetic.finish_conditions import check_finished
from src.genetic.select_new_generation import select_new_generation
import time

def genetic_algorithm(palette, N, target_color, selection_type,
                      crossing_type, mutation_type, mutation_pm,
                      select_new_generation_type, K, max_generations, d_error, max_time):
    
    end = False
    generation = 0 

    population = [] 
    for _ in range(N):
        population.append(Subject(palette, target_color, []))

    #for i in range(N):
    #   print(population[i].get_color_proportions())

    initial_time = time.time()

    best_subject = None
    finish_condition = None

    while(not end):
        print("Generacion numero: " + str(generation))

        time_passed = time.time() - initial_time

        # Check si es necesario terminar o no
        end, best_subject, finish_condition = check_finished(population, generation, max_generations, d_error, max_time, time_passed)
        
        if(not end):
            # Metodo de seleccion
            parents = selector(population, N, K, selection_type)

            # Cruza 
            children = crossover(parents, crossing_type, palette, target_color)

            # Mutacion 
            mutated_children = mutator(children, mutation_type, mutation_pm)

            # Nueva poblacion
            population = select_new_generation(mutated_children, parents, N, K, select_new_generation_type)
            
            generation += 1

    print("------------GANADOR------------")
    print(f"{finish_condition}")
    print(best_subject)