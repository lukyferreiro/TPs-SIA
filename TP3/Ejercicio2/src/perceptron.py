import numpy as np
import math

class Perceptron:
    def __init__(self, num_inputs, perceptron_type, learning_rate, epochs, beta, min_error, training_percentage):
        self.weights = np.random.rand(num_inputs)
        self.num_inputs = num_inputs
        self.perceptron_type = perceptron_type
        self.lr = learning_rate
        self.epochs = epochs
        self.beta = beta
        self.min_error = min_error
        self.training_percentage = training_percentage

    def train(self, input_data, expected_data):
        target_epoch = 0
        finished = False

        while target_epoch < self.epochs and not finished:
            for j in range(self.num_inputs):
                x = np.array(input_data[j])
                y = self.activation(x)

                self.weights += self.calculate_delta_w(x, expected_data[j] - y)

            #if ("Calcular si termino con MSE"):
            #    finished = True

            target_epoch += 1

    
    def activation(self, x):
        switcher = {
            "LINEAR": self.__activate_linear(x),
            "NON_LINEAR_TANH": self.__activate_non_linear_tanh(x),
            "NON_LINEAR_LOG": self.__activate_non_linear_log(x),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")
    
    def __activate_linear(self, x):
        return np.dot(self.weights, x)
    def __activate_non_linear_tanh(self):
        return any
    def __activate_non_linear_log(self):
        return any
    
    def calculate_delta_w(self, x, error):
        switcher = {
            "LINEAR": self.__calculate_delta_w_linear(x, error),
            "NON_LINEAR_TANH": self.__calculate_delta_w_non_linear_tanh(x, error),
            "NON_LINEAR_LOG": self.__calculate_delta_w_non_linear_log(x, error),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")

    def __calculate_delta_w_linear(self, x, error):
        return self.lr * error * x
    
    def __calculate_delta_w_non_linear_tanh(self, x, error):
        aux = []
        for i in x:
            theta = math.tanh(self.beta * i)
            aux.append(self.beta * (1 - theta**2))

        return self.lr * error * x * aux
    
    def __calculate_delta_w_non_linear_log(self, x, error):
        aux = []
        for i in x:
            theta = 1 / (1 + math.e**(-2*self.beta*i))
            aux.append(2 * self.beta * theta * (1 - theta) )

        return self.lr * error * x * aux

    def predict(self, x):
        return self.activation(x)
