import numpy as np
class Kohonen:

    def __init__(self, data, k, learning_rate, radius, epochs) -> None:
        self.data = data
        self.k = k
        self.learning_rate = learning_rate
        self.radius = radius
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
        converged = False
        while current_epoch < self.epochs and not converged:
            # Seleccionar un registro de entrada Xp
            random_idx = np.random.randint(len(self.data))
            Xp = self.data[random_idx]
            # Encontrar la neurona ganadora que tenga el vector de pesos mas cercano a Xp
            winner = self.__find_winner_neuron(Xp)
            # Actualizar los pesos de las neuronas vecinas segun la regla de Kohonen
            self.__update_weights(Xp, winner)
            # Ver cuando converge
            if ...:
                converged = True
            # Actualizar learning rate y radius ??
            current_epoch += 1

    # Encontrar la neurona ganadora que tenga el vector de pesos mas cercano a Xp
    def __find_winner_neuron(self, Xp):
        # Calculo la norma euclidiana entre Xp y cada vector de pesos
        norms = np.linalg.norm(self.weights - Xp, axis=2)
        return np.array(np.unravel_index(np.argmin(norms, axis=None), norms.shape))
    
    def __update_weights(self, Xp, winner):
        pass
        

    