import numpy as np
import pandas as pd

def check_positivity(num, str):
   if not type(num) == int or num < 0:
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

    def __init__(self, data, ej):

      self.bias = check_positivity(data['bias'], "bias")

      # Data 
      if(ej == 1):
         self.input_data, self.expected_data = read_data(data['input_file'])
      elif(ej == 2 or ej == 3):
         self.input_data, self.expected_data = parse_nums(data['input_file'], 7, ej)

      print(self.expected_data)

      # Training params
      self.learning_rate = check_prob(data['learning_rate'], "tasa de aprendizaje")
      self.epochs = check_positivity(data['epochs'], "epocas")
      self.training_percentage = check_prob(data['training_percentage'], "porcentaje de entrenamiento")
      self.training_type = check_type(data['training_type'], data['training_options'], "tipo de entrenamiento")
      self.k_fold = check_positivity(data['k_fold'], "k fold")
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
   
def parse_nums(file_name, height, ej):
   df = pd.read_csv(file_name, sep=' +', engine='python', header=None)
   arrayed = df.to_numpy()
   chunked = []
   base = 0
   while base < len(arrayed) - height + 1:
      grouped = np.array([], dtype=int)
      for i in range(height):
         grouped = np.append(grouped, arrayed[base + i])
      chunked.append(np.copy(grouped))
      base += height

   if(ej == 2):
      y = np.array([-1,1,-1,1,-1,1,-1,1,-1,1])
   else:
      y = [[1,0,0,0,0,0,0,0,0,0], #0
           [0,1,0,0,0,0,0,0,0,0], #1
           [0,0,1,0,0,0,0,0,0,0], #2
           [0,0,0,1,0,0,0,0,0,0], #3
           [0,0,0,0,1,0,0,0,0,0], #4
           [0,0,0,0,0,1,0,0,0,0], #5
           [0,0,0,0,0,0,1,0,0,0], #6
           [0,0,0,0,0,0,0,1,0,0], #7
           [0,0,0,0,0,0,0,0,1,0], #8
           [0,0,0,0,0,0,0,0,0,1]] #9

   return np.array(chunked), y


def k_splitting(raw_in, raw_out, k):
   if k > raw_in.shape[0]:
      raise Exception
   split_size = raw_in.shape[0] // k
   indexes = np.arange(0, raw_in.shape[0], dtype=int)
   np.random.shuffle(indexes)
   train_sets_idx = []
   test_sets_idx = []
   for i in range(k):
      test = indexes[i * split_size:(i + 1) * split_size]
      before = indexes[0:i * split_size]
      after = indexes[(i + 1) * split_size :]
      train = np.concatenate((before,after))
      train_sets_idx.append(train)
      test_sets_idx.append(test)
   # Train sets X,Y  then test sets, X and Y
   return np.take(raw_in,train_sets_idx, axis=0),np.take(raw_out,train_sets_idx, axis=0), \
         np.take(raw_in,test_sets_idx, axis=0),np.take(raw_out,test_sets_idx, axis=0)