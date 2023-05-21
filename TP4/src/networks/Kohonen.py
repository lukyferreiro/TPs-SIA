import numpy as np
import math

class Kohonen:

    def __init__(self, data, k, learning_rate, radius, epochs, likeness) -> None:
        self.data = data
        self.k = k
        self.learning_rate = learning_rate
        self.init_learning_rate = learning_rate
        self.radius = radius
        self.init_radius = radius
        self.epochs = epochs
        self.likeness = likeness
        self.__init_weights()

    # Inicializamos los pesos con muestras aleatorias de los datos de entrada
    def __init_weights(self):
        self.weights = np.zeros((self.k, self.k, len(self.data[0])))
        for i in range(self.k):
            for j in range(self.k):
                random_idx = np.random.randint(len(self.data))
                self.weights[i, j, :] = self.data[random_idx]

    def train(self):
        current_epoch = 0
        while current_epoch < self.epochs:
            random_idx = np.random.randint(len(self.data))
            Xp = self.data[random_idx]
            i,j = self.find_winner_neuron(Xp)
            winner = np.array([i,j])
            self.__update_weights(Xp, winner)

            aux = math.exp(-current_epoch / self.epochs)
            self.learning_rate = self.init_learning_rate * aux
            self.radius = self.init_radius * aux
            if self.radius < 1:
                self.radius = 1

            current_epoch += 1

    # Encontrar la neurona ganadora que tenga el vector de pesos mas cercano a Xp
    def find_winner_neuron(self, Xp):
        if self.likeness == "EUCLIDEAN":
            norms = np.linalg.norm(Xp - self.weights, axis=2)
        elif self.likeness == "EXPONENTIAL":
            norms = np.exp(-1 * (np.linalg.norm(Xp - self.weights, axis=2)) ** 2)
        return np.unravel_index(np.argmin(norms, axis=None), norms.shape)
    
    # Actualizar los pesos de las neuronas vecinas segun la regla de Kohonen
    def __update_weights(self, Xp, winner):
        neighbours = self.get_neighbours(winner)
        for (i,j) in neighbours:
            # Actualizamos solamente si pertenecen al vecindario
             self.weights[i][j] += self.learning_rate * (Xp - self.weights[i][j])

    def get_neighbours(self, winner):
        neighbours = []
        for i in range(self.k):
            for j in range(self.k):
                if np.linalg.norm(np.array([i, j]) - winner) <= self.radius:
                    neighbours.append((i, j))
        return neighbours