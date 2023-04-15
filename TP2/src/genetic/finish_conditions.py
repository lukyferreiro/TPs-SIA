

def check_finished(population, current_generation, max_generations, d_error, max_time, time_passed):

  sorted_pop = sorted(population, key=lambda x: x.fitness, reverse=True)
  best_subject = sorted_pop[0]

  """ print("---------Mejor sujeto---------")
  print(best_subject) """

  if ( current_generation >= max_generations
       or 1 - best_subject.fitness < d_error 
       or (max_time != -1 and time_passed > max_time)):
    
    if(current_generation >= max_generations):
      finish_condition = "Corto por superar maxima generacion"
    elif(1 - best_subject.fitness < d_error ):
      finish_condition = "Corto por encontrar solucion con delta de error minimo"
    else:
      finish_condition = "Corto por superar tiempo maximo"
    return True, best_subject, finish_condition

  return False, None, None
