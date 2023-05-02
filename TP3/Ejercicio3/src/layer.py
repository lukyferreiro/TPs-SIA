import numpy as np

class Layer(): 
    def __init__(self, neuron_count, input_size, activation_method, beta):
        self.neuron_count = neuron_count
        self.input_size = input_size
        self.weights = 2 * np.random.default_rng().random((input_size, neuron_count)) - 1
        self.bias = 2 * np.random.default_rng().random(neuron_count) - 1
        self.error_d = None
        self.activation_method = activation_method
        self.beta = beta

    def apply_delta(self, last_activation, learn_rate):
        act_mat = np.matrix(last_activation)
        err_mat = np.matrix(self.error_d)
        self.weights += learn_rate * act_mat.T.dot(err_mat)
        self.bias += learn_rate * self.error_d

    def calc_error_d(self, inherited_error, activation):
        if(self.activation_method == "TANH"):
            d = self.beta * ((1 - activation) * activation)
        else:
            d = 2 * self.beta * activation * (1 - activation)

        self.error_d = inherited_error * d

    def activate(self, feed):
        h = np.dot(feed, self.weights) + self.bias

        if(self.activation_method == "TANH"):
            return np.tanh(self.beta * h)
        else:
            return 1 / (1 + np.exp(-2 * self.beta * h))

    def __str__(self) -> str:
        return str(self.weights)

    def __repr__(self) -> str:
        return self.__str__()