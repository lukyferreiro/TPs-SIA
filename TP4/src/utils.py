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