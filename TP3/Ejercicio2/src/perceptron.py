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
                expected = self.train_expected_data[j]
                self.weights += self.calculate_delta_w(x, expected, Os[j])

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
        return 1 / (1 + math.pow(math.e, -2 * self.beta * h))
    
    # Funcion de Δw 
    def calculate_delta_w(self, x, expected, O):
        error = self.__normalize_image(expected) - O
        theta_diff = self.__calculate_theta_diff(O)
        return self.learning_rate * error * theta_diff * x

    # Funcion que calcula θ' segun el tipo de perceptron
    def __calculate_theta_diff(self, O):
        switcher = {
            "LINEAR": self.__calculate_theta_diff_linear(),
            "NON_LINEAR_TANH": self.__calculate_theta_diff_non_linear_tanh(O),
            "NON_LINEAR_LOG": self.__calculate_theta_diff_non_linear_log(O),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")

    def __calculate_theta_diff_linear(self):
        return 1
    def __calculate_theta_diff_non_linear_tanh(self, O):
        return self.beta * (1 - O**2)
    def __calculate_theta_diff_non_linear_log(self, O):
        return 2 * self.beta * O * (1 - O)

    # Funcion de prediccion
    def predict(self, x):
        return self.activation(x)

    # Función de error MSE para finalizar entrenamiento
    def __mid_square_error(self, Os, expected):
        return np.sum((expected - Os) ** 2) / len(expected)

    # Funcion que normaliza los resultados segun la imagen de la funcion de activacion
    def __normalize_image(self, values):
        switcher = {
            "LINEAR": self.__normalize_linear_image(values),
            "NON_LINEAR_TANH": self.__normalize_non_linear_tanh_image(values),
            "NON_LINEAR_LOG": self.__normalize_non_linear_log_image(values),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")

    def __normalize_linear_image(self, values):
        return values
    # Normalizacion para [a,b] es: X'=((X-Xmin)/(Xmax-Xmin))(b-a)+a
    def __normalize_non_linear_tanh_image(self, values):
        # Image = (-1,1)
        return (2 * (values - self.min) / (self.max - self.min)) - 1
    def __normalize_non_linear_log_image(self, values):
        # Image = (-1,1)
        return (values - self.min) / (self.max - self.min)
    
    # Funcion que desnormaliza los resultados segun la imagen de la funcion de activacion
    def __denormalize_image(self, values):
        switcher = {
            "LINEAR": self.__denormalize_linear_image(values),
            "NON_LINEAR_TANH": self.__denormalize_non_linear_tanh_image(values),
            "NON_LINEAR_LOG": self.__denormalize_non_linear_log_image(values),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")

    def __denormalize_linear_image(self, values):
        return values
    def __denormalize_non_linear_tanh_image(self, values):
        return ((values + 1) * (self.max - self.min) * 0.5) + self.min
    def __denormalize_non_linear_log_image(self, values):
        return values * (self.max - self.min) + self.min

    def __str__(self) -> str:
        return f"Perceptron {self.perceptron_type}: {self.weights}" 
    
    def __repr__(self) -> str:
        return self.__str__()