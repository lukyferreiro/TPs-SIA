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

def check_arr(arr, str):
   for i in range(len(arr)):
      check_positivity(arr[i], str)
   
   return arr

def destructure_data(data):

   input_data, expected_data = read_data(data['input_file'])
   #TODO concatenar el bias 

   learning_rate = check_prob(data['learning_rate'], "tasa de aprendizaje")
   epochs = check_positivity(data['epochs'], "epocas")
   bias = check_positivity(data['bias'], "bias")
   training_percentage = check_prob(data['training_percentage'], "porcentaje de entrenamiento")

   qty_hidden_layers = check_positivity(data['qty_hidden_layers'], "cantidad de capas ocultas")
   qty_nodes_in_hidden_layers = check_arr(data['qty_nodes_in_hidden_layers'], "cantidad de nodos en capas ocultas")

   if(qty_hidden_layers != len(qty_nodes_in_hidden_layers)):
      raise ValueError("qty_hidden_layers y qty_nodes_in_hidden_layers deben tener la misma dimension")
   
   output_activation = check_type(data['output_activation'], data['activation_options'], "funcion de activacion de capa de salida")
   hidden_activation = check_type(data['hidden_activation'], data['activation_options'], "funcion de activacion de capas ocultas")

   return input_data, expected_data, learning_rate, epochs, training_percentage, qty_hidden_layers, qty_nodes_in_hidden_layers, output_activation, hidden_activation

# TODO: modificar para generalizar la función para cuando tengamos más inputs 
def read_data(path):
   data = np.loadtxt(path, delimiter=',', skiprows=1)
   input_data = data[:, :-1]  # todas las columnas excepto la última
   expected_data = data[:, -1]  # última columna solamente

   print(input_data)
   print(expected_data)

   return input_data, expected_data
   