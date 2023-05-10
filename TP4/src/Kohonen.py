import numpy as np
import math
class Kohonen:

    def __init__(self, data, k, learning_rate, radius, epochs) -> None:
        self.data = data
        self.k = k
        self.learning_rate = learning_rate
        self.init_learning_rate = learning_rate
        self.radius = radius
        self.init_radius = radius
        self.epochs = epochs
        self.weights = self.__init_weights()

    # Inicializamos los pesos con muestras aleatorias de los datos de entrada
    def __init_weights(self):
        self.weights = np.zeros((self.k, self.k, len(self.data[0])))
        for i in range(self.k):
            for j in range(self.k):
                random_idx = np.random.randint(len(self.data))
                self.weights[i, j, :] = self.data[random_idx]

        return self.weights

    def train(self):
        current_epoch = 0
        while current_epoch < self.epochs:
            random_idx = np.random.randint(len(self.data))
            Xp = self.data[random_idx]
            winner = self.__find_winner_neuron(Xp)
            self.__update_weights(Xp, winner)

            aux = math.exp(-current_epoch / self.epochs)
            self.learning_rate = self.init_learning_rate * aux
            self.radius = self.init_radius * aux
            if self.radius < 1:
                self.radius = 1

            current_epoch += 1

    # Encontrar la neurona ganadora que tenga el vector de pesos mas cercano a Xp
    def __find_winner_neuron(self, Xp):
        # Norma euclidiana entre Xp y cada vector de pesos
        norms = np.linalg.norm(self.weights - Xp, axis=2)
        return np.array(np.unravel_index(np.argmin(norms, axis=None), norms.shape))
    
    # Actualizar los pesos de las neuronas vecinas segun la regla de Kohonen
    def __update_weights(self, Xp, winner):
        for i in range(self.k):
            for j in range(self.k):
                # Actualizamos solamente si pertenecen al vecindario
                if np.linalg.norm(np.array([i, j]) - winner) <= self.radius:
                    self.weights[i][j] += self.learning_rate * (Xp - self.weights[i][j])