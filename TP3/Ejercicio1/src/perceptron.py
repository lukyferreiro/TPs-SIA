import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, num_inputs, learning_rate, epochs, operation):
        self.weights = np.random.default_rng().random(num_inputs)
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.operation = operation
        self.errors = []
        self.current_epoch = 0
    
    def activation(self, x):
        return 1 if x>=0 else -1
        
    def train(self, inputs, targets):

        inputs_len = len(inputs)
        errors = np.empty(inputs_len)
        correct = np.empty(inputs_len)

        finished = False

        while self.current_epoch < self.epochs and not finished:
            for j in range(inputs_len):
                x = np.array(inputs[j])
                O = self.activation(np.dot(self.weights, x))
                errors[j] = targets[j] - O
                correct[j] = 1 if errors[j] == 0 else 0
                self.weights += self.learning_rate * errors[j] * x.astype(float)

            self.errors.append(np.sum(np.abs(errors)))

            # Se finaliza si:
            # --la suma absoluta de los errores en cada paso es 0
            # --la cantidad de respuestas correctas es igual a la cantidad de entradas
            if (self.errors[self.current_epoch] == 0 or self.calculate_accuracy(correct, inputs_len) == 1):
                finished = True

            self.current_epoch += 1

        print(f"Finished training in {self.current_epoch} epochs")

    def calculate_accuracy(self, correct, inputs_len):
        return np.sum(correct) / inputs_len

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
        bool_val = ['1', '-1']

        # asigna un color a cada punto dependiendo de la salida de la función
        colors = [color_val[0] if o == 1 else color_val[1] for o in expected_data]


        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

        # grafica los puntos
        ax1.scatter([p[1] for p in input_data], [p[2] for p in input_data], c=colors)

        # grafica la recta
        x = range(-2, 4)
        ax1.plot(x, (-self.weights[1]*x - self.weights[0])/self.weights[2], color='green')

        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=name, markerfacecolor=color, markersize=10)
                   for color, name in zip(color_val, bool_val)]
        

        ax1.set_title(f'Clasificación lineal del problema')
        ax1.legend(handles=legend_elements, loc='upper right')

        ax2.plot(range(self.current_epoch), self.errors, color='red')
        ax2.set_title("Rendimiento a traves de las generaciones")
        ax2.set_xlabel('Generación')
        ax2.set_ylabel('Error')

        plt.suptitle(f"Perceptron simple escalon para {self.operation} con η={self.learning_rate}")
        plt.show()