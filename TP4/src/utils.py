import copy
from statistics import mean, stdev
import numpy as np

def check_positivity(num, str):
   if not type(num) == int or num <= 0:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return num

def check_prob(num, str):
   if not type(num) == float or num < 0.0 or num > 1.0:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return num

def check_type(type, array, str):
   if type not in array:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return type

class DataConfig:

    def __init__(self, data) -> None:
        self.k = check_positivity(data['k'], "K")
        self.learning_rate = check_prob(data['learning_rate'], "tasa de aprendizaje")
        self.radius = check_positivity(data['radius'], "radio")
        self.epochs = check_positivity(data['epochs'], "epocas")
        self.likeness = check_type(data['likeness'], data['likeness_options'], "metodo de likeness")
        self.mutate_prob = check_prob(data['mutate_prob'], "probabilidad de mutacion")

# Estandarizamos los datos usando la media y el desvio estandar
def standarize_data(data):
   data_standarized = copy.deepcopy(data)
   for i in range(len(data[0])):
      aux = data_standarized[:, i]
      mean_aux = mean(aux)
      stdev_aux = stdev(aux)
      data_standarized[:, i] = (data_standarized[:, i] - mean_aux) / stdev_aux
   return data_standarized

def mutate(letter, prob):
   mutated_letter = np.copy(letter)
   for i in range(len(letter)):
        if np.random.default_rng().random() < prob:
            mutated_letter[i] *= -1
   return mutated_letter