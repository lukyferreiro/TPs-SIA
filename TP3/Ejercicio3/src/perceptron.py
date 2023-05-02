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

        # Arquitectura de la red neuronal
        self.qty_hidden_layers = qty_hidden_layers
        self.qty_nodes_in_hidden_layer = qty_nodes_in_hidden_layers
        self.layers = self.__init_layers()  # Inicialización de las capas

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

    
    def __init_layers(self):
        layers = []
        current_layer = 0

        # Numero de neuronas definido en config.json, numero de entradas dependiente de input_data
        layer_0 = Layer(self.qty_nodes_in_hidden_layer[current_layer], len(self.input_data[0]))
        layers.append(layer_0)

        current_layer += 1

        # Inicializamos capas intermedia (si solo tenemos una nunca entramos acá)
        # Cantidad de neuronas definido en config.json, numero de entradas dependiente de capa anterior
        while current_layer < self.qty_hidden_layers:
            layer = Layer(self.qty_nodes_in_hidden_layer[current_layer], self.qty_nodes_in_hidden_layer[current_layer-1].neuron_count)
            layers.append(layer)
            current_layer += 1  

        # Inicializamos capa de salida, cantidad de neuronas dependiente de expected_data
        final_layer = Layer(len(self.expected_data[0]), layers[current_layer - 1].neuron_count)
        layers.append(final_layer)
            
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

                # Calculate error
                self.layers[-1].calc_error_d(self.expected_data[i] - activations[-1], self.output_activation, activations[-1])
                
                # Backward propagation
                for i in range(len(self.layers) - 2, -1, -1):
                    inherit_layer = self.layers[i + 1]
                    self.layers[i].calc_error_d(inherit_layer.weights.dot(inherit_layer.error_d), self.output_activation, activations[i + 1])

                for i in range(len(self.layers)):
                    self.layers[i].apply_delta(activations[i], self.learn_rate)

            current_epoch += 1

    def activate(self, init_input):
        activations = [init_input]
        for i in range(len(self.layers)):
            activations.append(self.layers[i].activate(activations[-1], self.output_activation))
        return activations

     


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