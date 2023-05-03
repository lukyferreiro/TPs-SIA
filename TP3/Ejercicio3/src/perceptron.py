import numpy as np
from src.layer import Layer
import matplotlib.pyplot as plt
import copy

class MultilayerPerceptron:

    def __init__(self, input_data, expected_data, learning_rate, bias, epochs, training_type, training_percentage, k_fold, min_error,
                 qty_hidden_layers, qty_nodes_in_hidden_layers, output_activation, hidden_activation, beta,
                 optimization_method, alpha, beta1, beta2, epsilon, out_array):

        # Info del set de entrenamiento 
        self.min, self.max = self.__calculate_min_and_max(expected_data)
        self.bias = bias
        self.input_data = input_data
        self.expected_data = self.__normalize_image(expected_data, output_activation)
        self.train_MSE = -1

        # Global para la red neuronal
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.training_type = training_type
        self.training_percentage = training_percentage
        self.k_fold = k_fold

        self.train_input_data = self.train_expected_data = self.test_input_data = self.test_expected_data = None

        if training_percentage < 1:
            self.train_input_data, self.train_expected_data, self.test_input_data, self.test_expected_data = self.__divide_data_by_percentage(self.input_data, self.expected_data, self.training_percentage)

        self.min_error = min_error
        self.out_array = out_array

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
    
    # Inicializar conjuntos de training y testing
    def __divide_data_by_percentage(self, input, expected, p):
        num_rows = int(p * input.shape[0])

        idx = np.random.permutation(input.shape[0])

        t1 = input[idx[:num_rows], :]
        e1 = expected[idx[:num_rows]]

        t2 = input[idx[num_rows:], :]
        e2 = expected[idx[num_rows:]]

        return t1, e1, t2, e2

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
        num_outputs = self.__get_num_outputs()
        output_layer = Layer(num_outputs,
                             layers[current_layer - 1].neuron_count,
                             self.output_activation, self.beta) 
        layers.append(output_layer)
        return layers
    
    def __get_num_outputs(self):
        if isinstance(self.expected_data, np.ndarray) and self.expected_data.ndim == 1:
            return 1
        # Comprobar si expected es una matriz
        elif isinstance(self.expected_data, np.ndarray) and self.expected_data.ndim == 2:
            return self.expected_data.shape[1]
        else:
            raise ValueError("Expected debe ser un array o una matriz")

    def __calculate_min_and_max(self, expected_data):
        return np.min(expected_data), np.max(expected_data)

    def train(self):
        if(self.training_type == "PERCENTAGE"):
            return self.__train_percentage()
        else:
            return self.__train_k_fold()

    def __train_percentage(self):
        current_epoch = 0

        train_len = 0
        input = expected = None

        if self.training_percentage == 1:
            train_len = len(self.input_data) 
            input = self.input_data
            expected = self.expected_data
        else:
            train_len = len(self.train_input_data)
            input = self.train_input_data
            expected = self.train_expected_data

        mse_errors = []

        finished = False
        while current_epoch < self.epochs and not finished:
            Os = []
            if current_epoch%1000 == 0:
                print(current_epoch) 

            for i in range(train_len):
                # Forward activation
                activations = self.activate(input[i])
                Os.append(activations[-1])

                # Calculate error of output layer
                self.layers[-1].calc_error_d(expected[i] - Os[i], Os[i])
                
                # Backward propagation
                for i in range(len(self.layers) - 2, -1, -1):
                    inherit_layer = self.layers[i + 1]
                    self.layers[i].calc_error_d(np.dot(inherit_layer.weights,inherit_layer.error_d), activations[i + 1])

                for i in range(len(self.layers)):
                    self.layers[i].apply_delta(activations[i], self.learning_rate, current_epoch, self.optimization_method, self.alpha, self.beta1, self.beta2, self.epsilon)

            mse_errors.append(self.mid_square_error(Os, expected))

            if (mse_errors[current_epoch] < self.min_error):
                finished = True

            current_epoch += 1

        # Guardo el MSE error al finalizar el entrenamiento
        self.train_MSE = mse_errors[current_epoch - 1]

        print(f"Finished Training. \n MSE: {self.train_MSE}")

        if self.training_percentage < 1:
            test_accuracy, test_mse = self.test(self.test_input_data, self.test_expected_data)
        else:
            test_accuracy, test_mse = self.test(self.input_data, self.expected_data)

        return mse_errors, current_epoch, test_accuracy, test_mse

    def __train_k_fold(self):
        if self.k_fold > len(self.input_data) :
            raise("No puede entrenarse con validacion k-cruzada porque supera la cantidad de datos.")
        
        original_layers = copy.deepcopy(self.layers)

        idx = np.random.permutation(self.input_data.shape[0])

        input = self.input_data[idx, :]
        expected = self.expected_data[idx]

        input_data_sets = np.array_split(input, self.k_fold)
        expected_data_sets = np.array_split(expected, self.k_fold)

        MSEs_array_train = np.empty(self.k_fold)

        all_layers = []

        for k in range(self.k_fold):
            self.layers = copy.deepcopy(original_layers)

            current_train = np.concatenate([input_data_sets[i] for i in range(self.k_fold) if i != k])
            current_expected = np.concatenate([expected_data_sets[i] for i in range(self.k_fold) if i != k])

            train_len = len(current_train)

            Os = np.empty(train_len)
            mse_errors = np.empty(self.epochs)

            current_epoch = 0
            finished = False

            while current_epoch < self.epochs and not finished:
                Os = []

                for i in range(train_len):
                    # Forward activation
                    activations = self.activate(current_train[i])
                    Os.append(activations[-1])

                    # Calculate error of output layer
                    self.layers[-1].calc_error_d(current_expected[i] - Os[i], Os[i])
                    
                    # Backward propagation
                    for i in range(len(self.layers) - 2, -1, -1):
                        inherit_layer = self.layers[i + 1]
                        self.layers[i].calc_error_d(np.dot(inherit_layer.weights,inherit_layer.error_d), activations[i + 1])

                    for i in range(len(self.layers)):
                        self.layers[i].apply_delta(activations[i], self.learning_rate, current_epoch, self.optimization_method, self.alpha, self.beta1, self.beta2, self.epsilon)

                mse_errors[current_epoch] = self.mid_square_error(Os, current_expected)

                if (mse_errors[current_epoch] < self.min_error):
                    finished = True

                current_epoch += 1

            self.train_MSE = MSEs_array_train[k] = mse_errors[current_epoch - 1]
        
            print("Finished Training")

            test_accuracy, test_mse = self.test(input_data_sets[k], expected_data_sets[k])
            all_layers = np.append(all_layers, self.layers)

        all_layers = all_layers.reshape((self.k_fold, len(self.layers)))

        #idx = self.__choose_k_fold(MSEs_array_train, MSEs_array_test)

        return [], current_epoch, test_accuracy, test_mse

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

    def mid_square_error(self, Os, expected):
        error = 0
        size = len(Os)
        for i in range(size):
            error += (expected[i] - self.__denormalize_image(Os[i])) ** 2
        return np.sum(error) / size
        
    def accuracy(self,test_set,expected_out,out_classes):
        matches = 0
        for case_idx in range(len(test_set)):
            activations = self.activate(test_set[case_idx])
            guess = self.__denormalize_image(activations[-1][0])
            closest_idx = (np.abs(out_classes-guess)).argmin()

            print(guess)

            matches += 1 if out_classes[closest_idx] == expected_out[case_idx] else 0
        return matches/len(test_set)

    def accuracy_multiple(self,test_set,expected_out):
        matches = 0
        for case_idx in range(len(test_set)):
            activations = self.activate(test_set[case_idx])
            guess = self.__denormalize_image(activations[-1])
            max_idx = guess.argmax()
            matches += 1 if expected_out[case_idx][max_idx] == 1 else 0

            print(f"Expected {expected_out[case_idx].argmax()}")
            print(f"Guess {max_idx}")

        return matches/len(test_set)

    def test(self, input, expected):
        test_accuracy = -1
        if (self.__get_num_outputs() > 1):
            test_accuracy = self.accuracy_multiple(input, expected)
        else:
            test_accuracy = self.accuracy(input, expected, self.out_array)

        Os = []
        for i in range(len(input)):
            activations = self.activate(input[i])
            Os.append(activations[-1])
        test_mse = self.mid_square_error(Os, expected)

        print(f"Test Accuracy: {test_accuracy}")
        print(f"Test MSE = {test_mse}")
        return test_accuracy, test_mse

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

    def __denormalize_image(self, values):
        switcher = {
            "TANH": self.__denormalize_tanh_image(values),
            "LOG": self.__denormalize_log_image(values),
        }

        return switcher.get(self.output_activation, "Tipo de activacion de salida invalido")

    def __denormalize_tanh_image(self, values):
        return ((values + 1) * (self.max - self.min) * 0.5) + self.min
    def __denormalize_log_image(self, values):
        return values * (self.max - self.min) + self.min

    def plot(self, mse_errors, epochs):

        plt.plot(range(epochs), mse_errors)
        plt.xlabel('Generación')
        plt.ylabel('Error (MSE)')
        plt.title(f'Perceptron Multicapa \n η={self.learning_rate} \n')
        
        plt.show()