import numpy as np


def Layer(): 
    def __init__(self, neuron_count, input_size):
        self.neuron_count = neuron_count
        self.input_size = input_size
        self.weights = 2 * np.random.default_rng().random((input_size, neuron_count)) - 1
        self.bias = 2 * np.random.default_rng().random(neuron_count) - 1
        self.error_d = None

    def apply_delta(self, last_activation, learn_rate):
        act_mat = np.matrix(last_activation)
        err_mat = np.matrix(self.error_d)
        self.weights += learn_rate * act_mat.T.dot(err_mat)
        self.bias += learn_rate*self.error_d

    def calc_error_d(self, inherited_error, derivative_function_type, activation):
        switcher = {
            "TANH": self.__activation_derivate_tanh(activation),
            "LOG": self.__activation_derivate_log(activation),
        }

        d = switcher.get(derivative_function_type, "Tipo de activacion invalido")
        self.error_d = inherited_error * d

    def __activation_derivate_tanh(self, g):
        return self.beta * ((1 - g) * g)
    def __activation_derivate_log(self, g):
        return 2 * self.beta * g * (1 - g)

    def activate(self, feed, learn_function):
        h = np.dot(feed, self.weights) + self.bias
        switcher = {
            "TANH": self.__activation_tanh(h),
            "LOG": self.__activation_log(h),
        }
        return switcher.get(learn_function, "Tipo de activacion invalido")

    def __activation_tanh(self, h):
        return np.tanh(self.beta * h)
    def __activation_log(self, h):
        return 1 / (1 + np.exp(-2 * self.beta * h))

    def __str__(self) -> str:
        return str(self.weights)

    def __repr__(self) -> str:
        return self.__str__()