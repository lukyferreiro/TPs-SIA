import numpy as np

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