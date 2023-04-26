import numpy as np
import math

class Perceptron:
    
    def __init__(self, input_data, expected_data, perceptron_type, learning_rate, epochs, beta, min_error, training_percentage):
        self.num_inputs = len(input_data[0])
        self.weights = np.zeros(self.num_inputs)
        self.training_percentage = training_percentage
        self.train_input, self.train_expected_data, self.test_input, self.test_expected_data = self.__divide_data_by_percentage(input_data, expected_data, self.training_percentage)
        self.perceptron_type = perceptron_type
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.beta = beta
        self.min_error = min_error
        self.min, self.max = self.__calculate_min_and_max()

    def __calculate_min_and_max(self):
        return min(self.train_input)[0], max(self.train_input)[0]

    # Inicializar conjuntos de training y testing
    def __divide_data_by_percentage(self, input, expected, p):
        num_rows = int(p * input.shape[0])

        idx = np.random.permutation(input.shape[0])

        t1 = input[idx[:num_rows], :]
        e1 = expected[idx[:num_rows]]

        t2 = input[idx[num_rows:], :]
        e2 = expected[idx[num_rows:]]

        return t1, e1, t2, e2

    # Función de entrenamiento
    def train(self):
        target_epoch = 0
        finished = False

        train_len = len(self.train_input)
        Os = np.empty(train_len)

        while target_epoch < self.epochs and not finished:
            for j in range(train_len):
                x = np.array(self.train_input[j])
                h = np.dot(self.weights, x)
                Os[j] = self.activation(h)
                self.weights += self.calculate_delta_w(x, self.train_expected_data[j] - Os[j], h)

            if (self.__mid_square_error(Os, self.train_expected_data) < self.min_error):
                finished = True

            target_epoch += 1

    # Funciónes de activación O segun el tipo de perceptron
    def activation(self, h):
        switcher = {
            "LINEAR": self.__activate_linear(h),
            "NON_LINEAR_TANH": self.__activate_non_linear_tanh(h),
            "NON_LINEAR_LOG": self.__activate_non_linear_log(h),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")
    
    def __activate_linear(self, h):
        return h
    def __activate_non_linear_tanh(self, h):
        return math.tanh(self.beta * h)
    def __activate_non_linear_log(self, h):
        return 1 / (1 + math.pow(math.e, -2*self.beta*h))
    
    # Funcion de Δw 
    def calculate_delta_w(self, x, error, h):
        theta = self.__calculate_theta_diff(h)
        return self.learning_rate * error * theta * x

    # Funcion que calcula θ' segun el tipo de perceptron
    def __calculate_theta_diff(self, h):
        switcher = {
            "LINEAR": self.__calculate_theta_diff_linear(),
            "NON_LINEAR_TANH": self.__calculate_theta_diff_non_linear_tanh(h),
            "NON_LINEAR_LOG": self.__calculate_theta_diff_non_linear_log(h),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")

    def __calculate_theta_diff_linear(self):
        return 1
    def __calculate_theta_diff_non_linear_tanh(self, h):
        theta = self.activation(h)
        return self.beta * (1 - theta**2)
    def __calculate_theta_diff_non_linear_log(self, h):
        theta = self.activation(h)
        return 2 * self.beta * theta * (1 - theta)

    # Funcion de prediccion
    def predict(self, x):
        return self.activation(x)

    # Función de error MSE para finalizar entrenamiento
    def __mid_square_error(self, Os, expected):
        return np.sum((expected - Os) ** 2) / len(expected)

    def __str__(self) -> str:
        return f"Perceptron {self.perceptron_type}: {self.weights}" 
    
    def __repr__(self) -> str:
        return self.__str__()