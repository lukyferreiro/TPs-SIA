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
    training_type = check_type(data['training_type'], data['training_options'], "tipo de entrenamiento")
    training_percentage = check_prob(data['training_percentage'], "porcentaje de entrenamiento")
    k = check_positivity(data['k_fold'], "k fold")
    return perceptron_type, learning_rate, epochs, bias, beta, min_error, training_type, training_percentage, k

def get_data(bias):
    data = pd.read_csv('Ej2-conjunto.csv')

    input = np.array(data[['x1', 'x2', 'x3']])
    input_bias = np.insert(input, 0, bias, axis=1)

    expected_data = np.array(data['y'])

    return input_bias, expected_data

def perceptron_type_str(str, beta):
   switcher = {
      "LINEAR": "Lineal",
      "NON_LINEAR_TANH": f"No Lineal (tanh) con β={beta}",
      "NON_LINEAR_LOG": f"No Lineal (log) con β={beta}",
   }

   return switcher.get(str, "Tipo de perceptron invalido")

def get_train_type(training_type, percentage, K):

   switcher = {
      "PERCENTAGE":f"{round(percentage*100)}% de entrenamiento y {round((1-percentage)*100)}% de testeo",
      "K-FOLD": f"validacion cruzada (k={K})",
   }

   return switcher.get(training_type, "Tipo de perceptron invalido")