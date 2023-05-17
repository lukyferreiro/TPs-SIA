import numpy as np
from statistics import mean

class Oja:

    def __init__(self, data_standarized, learning_rate, epochs) -> None:
        self.__valid_mean_of_data(data_standarized)
        self.data_standarized = data_standarized
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = 2 * np.random.default_rng().random(len(data_standarized[0])) - 1

    def __valid_mean_of_data(self, data):
        mean_aux = 0
        for i in range(len(data[0])):
            aux = data[:, i]
            mean_aux += mean(aux)
        return np.abs(mean_aux) < 0.000001

    def train(self):
        current_epoch = 0
        while current_epoch < self.epochs:
            for x in self.data_standarized:
                O = np.dot(self.weights, x)
                self.weights += self.learning_rate * O * (x - O * self.weights)
            current_epoch += 1
        return self.weights