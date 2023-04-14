

def check_finished(population, max_generations, d_error, time, current_time):

  sorted_pop = sorted(population, key=lambda x: x.fitness, reverse=True)
  best_subject = sorted_pop[0]

  print("---------Mejor sujeto---------")
  print(best_subject)

  if ( best_subject.generation >= max_generations
       or 1 - best_subject.fitness < d_error 
       or current_time >= time ):
    if(best_subject.generation >= max_generations):
      finish_condition = "Corto por superar maxima generacion"
    elif(1 - best_subject.fitness < d_error ):
      finish_condition = "Corto por encontrar solucion con delta de error minimo"
    else:
      finish_condition = "Corto por superar tiempo maximo"
    return True, best_subject, finish_condition

  return False, None, None
