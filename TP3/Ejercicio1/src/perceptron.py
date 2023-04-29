import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, num_inputs, lr, epochs, operation):
        self.weights = np.random.default_rng().random(num_inputs)
        self.lr = lr
        self.epochs = epochs
        self.operation = operation
    
    def activation(self, x):
        return 1 if x>=0 else -1
        
    def train(self, inputs, targets):
        target_epoch = 0
        finished = False

        inputs_len = len(inputs)

        errors = np.empty(inputs_len)
        correct = np.empty(inputs_len)

        while target_epoch < self.epochs and not finished:
            for j in range(inputs_len):
                x = np.array(inputs[j])
                O = self.activation(np.dot(self.weights, x))
                errors[j] = targets[j] - O
                correct[j] = 1 if errors[j] == 0 else 0

                self.weights += self.lr * errors[j] * x.astype(float)

            # Si la suma absoluta de los errores en cada paso es 0, se finaliza
            # O si la cantidad de respuestas correctas es igual a la longitud del input
            if (np.sum(np.abs(errors)) == 0 or self.accuracy(correct, inputs_len) == 1):
                finished = True

            target_epoch += 1

        print(f"Finished training in {target_epoch} epochs")

    def accuracy(self, correct, inputs_len):
        return np.sum(correct)/inputs_len

    # En la posición x0 está el bias para tener longitudes iguales y poder utilizar np.dot
    def predict(self, x):
        return self.activation(np.dot(self.weights, x))
    
    def get_weights(self):
        return self.weights
    
    def __str__(self) -> str:
        return f"Perceptron: {self.weights}" 
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def plot(self, input_data, expected_data):
        color_val = ['blue', 'red']
        bool_val = ['true', 'false']

        # asigna un color a cada punto dependiendo de la salida de la función
        colors = [color_val[0] if o == 1 else color_val[1] for o in expected_data]

        # grafica los puntos
        plt.scatter([p[1] for p in input_data], [p[2] for p in input_data], c=colors)

        # grafica la recta
        x = y = range(-2, 4)
        plt.plot(x, (-self.weights[1]*x - self.weights[0])/self.weights[2], color='green')

        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=name, markerfacecolor=color, markersize=10)
                   for color, name in zip(color_val, bool_val)]
        

        plt.title(f'Función de clasificación de perceptron {self.operation}')
        plt.legend(handles=legend_elements, loc='upper right')

        # muestra el gráfico
        plt.show()