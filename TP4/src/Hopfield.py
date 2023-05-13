import numpy as np

class Hopfield:

    def __init__(self, saved_patterns, epochs) -> None:
        self.saved_patterns = saved_patterns
        self.epochs = epochs
        self.__init_weights()

    def __init_weights(self):
        self.weights = (1 / len(self.saved_patterns)) * np.matmul(self.saved_patterns.T, self.saved_patterns)
        np.fill_diagonal(self.weights, 0)


    def train(self, pattern):
        pass