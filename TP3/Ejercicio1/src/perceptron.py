
import numpy as np

def perceptron(input_data, expected_data, learning_rate, epochs, weights):
    
    print(f"Weights: {weights}")
    n = 0
    not_finished = True
    while n < epochs and not_finished:

        #TODO add condicion de corte

        for i in range(len(input_data)):
            x = input_data[i]

            # Funcion de activacion
            y = simple_escalon(np.dot(weights[1:], x[1:]) - weights[0])
            
            if(expected_data[i] != y):
                for j in range(len(weights)):
                    weights[j] = weights[j] + (2 * learning_rate * x[j] * expected_data[i])

        n += 1
        print(f"Weights: {weights}")

    return weights


def simple_escalon(value):
    return 1 if value >= 0 else -1
    
def accuracy(out_true, out_pred):
    return np.sum(out_true == out_pred) / len(out_true)