import numpy as np

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

class DataConfig:

    def __init__(self, data):

      self.bias = check_positivity(data['bias'], "bias")

      # Data 
      self.input_data, self.expected_data = read_data(data['input_file'])

      # Training params
      self.learning_rate = check_prob(data['learning_rate'], "tasa de aprendizaje")
      self.epochs = check_positivity(data['epochs'], "epocas")
      self.training_percentage = check_prob(data['training_percentage'], "porcentaje de entrenamiento")
      self.min_error = check_prob(data['min_error'], "cota de error")

      # Layer params
      self.output_activation = check_type(data['output_activation'], data['activation_options'], "funcion de activacion de capa de salida")
      self.hidden_activation = check_type(data['hidden_activation'], data['activation_options'], "funcion de activacion de capas ocultas")
      self.beta = check_num(data['beta'], "beta")

      self.qty_hidden_layers = check_positivity(data['qty_hidden_layers'], "cantidad de capas ocultas")
      self.qty_nodes_in_hidden_layers = check_arr(data['qty_nodes_in_hidden_layers'], "cantidad de nodos en capas ocultas")

      if(self.qty_hidden_layers != len(self.qty_nodes_in_hidden_layers)):
         raise ValueError("qty_hidden_layers y qty_nodes_in_hidden_layers no se corresponden entre si")
      
      # Optimizer values
      self.optimizer_method = check_type(data['optimizer_method'], data['optimizer_options'], "metodo de optimizacion")
      self.alpha = check_prob(data['alpha'], "alpha")
      self.beta1 = check_prob(data['beta1'], "beta 1")
      self.beta2 = check_prob(data['beta2'], "beta 2")
      self.epsilon = check_prob(data['epsilon'], "epsilon")


def read_data(path):

   with open(path, 'r') as f:
      first_line = f.readline().strip() 

   x = 0
   y = 0

   for val in first_line.split(','):
      if(val.startswith('x')):
         x += 1
      else:
         y += 1

   data = np.loadtxt(path, delimiter=',', skiprows=1)
   input_data = data[:, :-y]  
   expected_data = data[:, -y]

   return input_data, expected_data
   