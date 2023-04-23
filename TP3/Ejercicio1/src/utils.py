def check_positivity(num, str):
   if not type(num) == int or num <= 0:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return num

def check_prob(num, str):
   if not type(num) == float or num < 0 or num > 1:
      raise ValueError(f"Valor de '{str}' invalido")
   
   return num

def check_type(type, array, str):
   if type not in array:
      raise ValueError(f"Valor de {str} invalido")
   
   return type

def destructure_data(data):
    operation = check_type(data['operation'], data['operation_options'], "operación")
    learning_rate = check_prob(data['learning_rate'], "tasa de aprendizaje")
    epochs = check_positivity(data['epochs'], "epocas")
    bias = check_positivity(data['bias'], "bias")
    return operation, learning_rate, epochs, bias