import numpy as np

class Hopfield:

    def __init__(self, saved_patterns, epochs) -> None:
        self.saved_patterns = saved_patterns
        self.epochs = epochs
        self.__init_weights()

    # Matriz de pesos simetrica con la diagonal 0's
    def __init_weights(self):
        _, N = self.saved_patterns.shape
        self.weights = (1 / N) * np.matmul(np.transpose(self.saved_patterns), self.saved_patterns)
        np.fill_diagonal(self.weights, 0)

    def predict(self, pattern):
        s1 = pattern
        s2 = None

        arr_patterns = []
        arr_energy = []
        arr_patterns.append(s1)
        arr_energy.append(self.__calculate_energy(s1))

        iteration = 0
        stable = False
        while not stable and iteration < self.epochs:
            s2 = np.sign(np.matmul(self.weights, s1))
            self.__replace_zeros(s1, s2)
            
            arr_patterns.append(s2)
            arr_energy.append(self.__calculate_energy(s2))

            if np.array_equal(s1, s2):
                stable = True

            s1 = s2
            iteration += 1

        return np.array(list(arr_patterns)), arr_energy
    
    def __calculate_energy(self, s1):
        return -np.dot(s1.T, np.dot(np.triu(self.weights), s1))

    def __replace_zeros(self, s1, s2):
        for indexes in np.argwhere(s2 == 0):
            s2[indexes[0]][indexes[1]] = s1[indexes[0]][indexes[1]]