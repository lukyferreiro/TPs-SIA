from src.utils import currentMilliTime
from src.genetic.subject import Subject
from src.genetic.selection import selector
from src.genetic.mutation import mutator
from src.genetic.crossover import crossover
from src.genetic.finish_conditions import check_finished
from src.genetic.select_new_generation import select_new_generation

def genetic_algorithm(palette, N, target_color, selection_type,
                      crossing_type, mutation_type, mutation_pm,
                      select_new_generation_type, K, max_generations, d_error, time):
    
    end = False
    generation = 0 

    population = [] 
    for _ in range(N):
        population.append(Subject(palette, generation, target_color, None))

    for i in range(N):
        print(population[i].get_color_proportions())

    initial_time = currentMilliTime()
    current_time = currentMilliTime()

    best_subject = None
    finish_condition = None

    while(not end):
        print("Generacion numero: " + str(generation))

        # Check si es necesario terminar o no
        end, best_subject, finish_condition = check_finished(population, max_generations, d_error, time, current_time)
        
        # Metodo de seleccion
        parents = selector(population, N, K, selection_type)

        # Cruza 
        children = crossover(parents, crossing_type, palette, target_color)

        # Mutacion 
        mutated_children = mutator(children, mutation_type, mutation_pm)

        # Nueva poblacion
        population = select_new_generation(mutated_children, parents, N, K, select_new_generation_type)
        
        generation += 1
        current_time = currentMilliTime() - initial_time

    print("------------GANADOR------------")
    print(f"{finish_condition}")
    print(best_subject)