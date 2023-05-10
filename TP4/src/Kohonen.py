import numpy as np

class Kohonen:

    def __init__(self, data, k, learning_rate, radius, epochs) -> None:
        self.data = data
        self.k = k
        self.learning_rate = learning_rate
        self.radius = radius
        self.epochs = epochs
        self.weights = self.__init_weights()

    def __init_weights(self):
        self.weights = np.zeros((self.k, self.k, len(self.data[0])))
        for i in range(self.k):
            for j in range(self.k):
                random_idx = np.random.default_rng().choice(np.arange(len(self.data)))
                self.weights[i, j, :] = self.data[random_idx]
        print("---------------------------------------")
        print(self.weights)

    