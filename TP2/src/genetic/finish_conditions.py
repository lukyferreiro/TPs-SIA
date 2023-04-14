

def check_finished(population, max_generations, d_error, time, current_time):

  sorted_pop = sorted(population, key=lambda x: x.fitness, reverse=True)
  best_subject = sorted_pop[0]

  print(best_subject)

  if ( best_subject.generation >= max_generations
       or 1 - best_subject.fitness < d_error 
       or time >= current_time ):
    return True

  return False
