
import numpy as np

def perceptron(input_data, expected_data, learning_rate, epochs):
    
    # Lista de pesos
    #weights = np.random.default_rng().uniform(0, 1, size=(len(input_data[0])))
    weights = np.random.rand(len(input_data[0]))

    for _ in range(epochs):
        for i in range(0, len(input_data)):
            x = input_data[i]

            # Funcion de activacion
            y = simple_escalon(np.dot(weights, x))

            """
            error = expected_data[i] - y
            weights += learning_rate * error * x
            """ 
            
            for j in range(0, len(weights)):
                weights[j] += learning_rate * (expected_data[i] - y) * x[j]
            
                 
        print("w: ", weights)
     
    return weights


def simple_escalon(value):
    return 1 if value >= 0 else 0
    
def accuracy(out_true, out_pred):
    return np.sum(out_true == out_pred) / len(out_true)