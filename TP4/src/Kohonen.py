import numpy as np
import copy

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
        #Iinicializamos los pesos con muestras aleatorias de los datos de entrada
        for i in range(self.k):
            for j in range(self.k):
                random_idx = np.random.default_rng().choice(np.arange(len(self.data)))
                self.weights[i, j, :] = self.data[random_idx]
        print("---------------------------------------")
        print(self.weights)

    def train(self):
        current_epoch = 0
        converged = False
        while current_epoch < self.epochs and not converged:
            # Seleccionar un registro de entrada Xp
            random_idx = np.random.default_rng().choice(np.arange(len(self.data)))
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
        pass
    
    def __update_weights(self, Xp, winner):
        pass
        

    