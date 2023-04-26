import numpy as np

class Perceptron:
    def __init__(self, num_inputs, lr, epochs):
        self.weights = np.random.rand(num_inputs)
        self.num_inputs = num_inputs
        self.lr = lr
        self.epochs = epochs
    
    def activation(self, x):
        return 1 if x>=0 else -1
        
    def train(self, inputs, targets):
        target_epoch = 0
        finished = False
        errors = np.empty(self.num_inputs)
        correct = np.empty(self.num_inputs)

        while target_epoch < self.epochs and not finished:
            for j in range(self.num_inputs):
                x = np.array(inputs[j])
                O = self.activation(np.dot(self.weights, x))
                errors[j] = targets[j] - O
                correct[j] = 1 if errors[j] == 0 else 0

                self.weights += self.lr * errors[j] * x.astype(float)

            # Si la suma absoluta de los errores en cada paso es 0, se finaliza
            # O si la cantidad de respuestas correctas es igual a la longitud del input
            if (np.sum(np.abs(errors)) == 0 or self.accuracy(correct) == 1):
                finished = True

            target_epoch += 1

    def accuracy(self, correct):
        return np.sum(correct)/self.num_inputs

    # En la posición x0 está el bias para tener longitudes iguales y poder utilizar np.dot
    def predict(self, x):
        return self.activation(np.dot(self.weights, x))
    
    def get_weights(self):
        return self.weights