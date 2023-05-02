import numpy as np
from src.layer import Layer

class MultilayerPerceptron:

    def __init__(self, input_data, expected_data, learning_rate, bias, epochs, training_percentage, min_error,
                 qty_hidden_layers, qty_nodes_in_hidden_layers, output_activation, hidden_activation, beta,
                 optimization_method, alpha, beta1, beta2, epsilon):

        # Info del set de entrenamiento 
        self.min, self.max = self.__calculate_min_and_max(expected_data)
        self.bias = bias
        self.input_data = input_data
        self.expected_data = self.__normalize_image(expected_data, output_activation)
        
        # Global para la red neuronal
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.training_percentage = training_percentage
        self.min_error = min_error

        # Metodos de activacion
        self.output_activation = output_activation
        self.hidden_activation = hidden_activation
        self.beta = beta

        # Metodos de optimización
        self.optimization_method = optimization_method
        self.alpha = alpha
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

        # Arquitectura de la red neuronal
        self.qty_hidden_layers = qty_hidden_layers
        self.qty_nodes_in_hidden_layer = qty_nodes_in_hidden_layers
        self.layers = self.__init_layers()  # Inicialización de las capas
    
    def __init_layers(self):
        layers = []
        current_layer = 0

        # Numero de neuronas definido en config.json, numero de entradas dependiente de input_data
        layer_0 = Layer(self.qty_nodes_in_hidden_layer[current_layer],
                        len(self.input_data[0]),
                        self.hidden_activation, self.beta)
        layers.append(layer_0)

        current_layer += 1

        # Inicializamos capas intermedia (si solo tenemos una nunca entramos acá)
        # Cantidad de neuronas definido en config.json, numero de entradas dependiente de capa anterior
        while current_layer < self.qty_hidden_layers:
            layer = Layer(self.qty_nodes_in_hidden_layer[current_layer],
                          self.qty_nodes_in_hidden_layer[current_layer-1],
                          self.hidden_activation, self.beta)
            layers.append(layer)
            current_layer += 1  

        # Inicializamos capa de salida, cantidad de neuronas dependiente de expected_data

        num_outputs = len(self.expected_data[0]) if isinstance(self.expected_data[0], list) else 1
        output_layer = Layer(num_outputs,
                             layers[current_layer - 1].neuron_count,
                             self.output_activation, self.beta) 
        layers.append(output_layer)
        return layers

    def __calculate_min_and_max(self, expected_data):
        return np.min(expected_data), np.max(expected_data)

    def train(self):
        current_epoch = 0
        train_len = len(self.input_data)
        while current_epoch < self.epochs:
            for i in range(train_len):
                # Forward activation
                activations = self.activate(self.input_data[i])
                O = activations[-1]

                # Calculate error
                self.layers[-1].calc_error_d(self.expected_data[i] - O, O)
                
                # Backward propagation
                for i in range(len(self.layers) - 2, -1, -1):
                    inherit_layer = self.layers[i + 1]
                    self.layers[i].calc_error_d(np.dot(inherit_layer.weights,inherit_layer.error_d), activations[i + 1])

                for i in range(len(self.layers)):
                    self.layers[i].apply_delta(activations[i], self.learning_rate, current_epoch, self.optimization_method, self.alpha, self.beta1, self.beta2, self.epsilon)

            current_epoch += 1

    def activate(self, init_input):
        activations = [init_input]
        for i in range(len(self.layers)):
            activations.append(self.layers[i].activate(activations[-1]))
        return activations

    def __str__(self) -> str:
        str = "Perceptron multicapa\n"
        for i in range(len(self.layers)):
            str += f"Capa {i}:\n. {self.layers[i]}\n"
        return str
    
    def __repr__(self) -> str:
        return self.__str__()

    def eval_error(self,test_set,expected_out):
        error = 0
        for i in range(test_set.shape[0]):
            activations = self.activate(test_set[i])
            error += (expected_out[i] - activations[-1]) ** 2
        return np.sum(error) / test_set.shape[0]

    def accuracy(self,test_set,expected_out,out_classes):
        matches = 0
        for case_idx in range(len(test_set)):
            activations = self.activate(test_set[case_idx])
            guess = self.__denormalize_image(activations[-1][0], self.output_activation)

            print(guess)

            closest_idx = (np.abs(out_classes-guess)).argmin()
            matches += 1 if out_classes[closest_idx] == expected_out[case_idx] else 0
        return matches/len(test_set)

    def accuracy_by_node(self,test_set,expected_out):
        matches = 0
        for case_idx in range(len(test_set)):
            guess = self.activate(test_set[case_idx])[-1]
            max_idx = guess.argmax()
            matches += 1 if expected_out[case_idx][max_idx] == 1 else 0
        return matches/len(test_set)

    # -----------------------NORMALIZATION-----------------------
    def __normalize_image(self, values, output_activation):
        switcher = {
            "TANH": self.__normalize_tanh_image(values),
            "LOG": self.__normalize_log_image(values),
        }

        return switcher.get(output_activation, "Tipo de activacion de salida invalido")

    # Normalizacion para [a,b] es: X'=((X-Xmin)/(Xmax-Xmin))(b-a)+a
    def __normalize_tanh_image(self, values):
        return (2 * (values - self.min) / (self.max - self.min)) - 1
    def __normalize_log_image(self, values):
        return (values - self.min) / (self.max - self.min)

    def __denormalize_image(self, values, output_activation):
        switcher = {
            "TANH": self.__denormalize_tanh_image(values),
            "LOG": self.__denormalize_log_image(values),
        }

        return switcher.get(output_activation, "Tipo de activacion de salida invalido")

    def __denormalize_tanh_image(self, values):
        return ((values + 1) * (self.max - self.min) * 0.5) + self.min
    def __denormalize_log_image(self, values):
        return values * (self.max - self.min) + self.min