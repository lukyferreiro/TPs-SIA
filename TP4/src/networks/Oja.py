import numpy as np

class Oja:

    def __init__(self, data_standarized, learning_rate, epochs) -> None:
        self.data_standarized = data_standarized
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.random.default_rng().random(len(data_standarized[0]))

    def train(self):
        current_epoch = 0
        while current_epoch < self.epochs:
            for x in self.data_standarized:
                O = np.dot(self.weights, x)
                self.weights += self.learning_rate * O * (x - O * self.weights)
            current_epoch += 1
        return self.weights