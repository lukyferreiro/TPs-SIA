import numpy as np
import pandas as pd

def check_positivity(num, str):
   if not type(num) == int or num <= 0:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return num

def check_prob(num, str):
   if not type(num) == float or num < 0 or num > 1:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return num

def check_num(num, str):
   if not type(num) == float:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return num

def check_type(type, array, str):
   if type not in array:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return type

def destructure_data(data):
    perceptron_type = check_type(data['perceptron_type'], data['perceptron_options'], "tipo de perceptrón")
    learning_rate = check_prob(data['learning_rate'], "tasa de aprendizaje")
    epochs = check_positivity(data['epochs'], "epocas")
    bias = check_positivity(data['bias'], "bias")
    beta = check_num(data['beta'], "beta")
    min_error = check_prob(data['min_error'], "cota de error")
    training_percentage = check_prob(data['training_percentage'], "porcentaje de entrenamiento")
    k = (data['k_fold'], "k fold")
    return perceptron_type, learning_rate, epochs, bias, beta, min_error, training_percentage, k

def get_data(bias):
    data = pd.read_csv('Ej2-conjunto.csv')

    input = np.array(data[['x1', 'x2', 'x3']])
    input_bias = np.insert(input, 0, bias, axis=1)

    expected_data = np.array(data['y'])

    return input_bias, expected_data