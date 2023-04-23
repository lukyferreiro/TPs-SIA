from src.utils import destructure_data
from src.data import operation_data
from src.perceptron import perceptron, accuracy, simple_escalon
import numpy as np
import json

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    operation, learning_rate, epochs, bias = destructure_data(data)
    input_data, expected_data = operation_data(operation)

    #Concatenarle el bias al input_data
    for data in input_data:
        data.insert(0, bias)

    # Lista de pesos
    weights = np.random.rand(len(input_data[0]))
    print("ANTES\nWeights: ", weights)
    for j in range(len(input_data)):
        print(f"Resolucion: {expected_data[j]} == {simple_escalon(np.dot(weights[1:], input_data[j][1:]) - weights[0])}")
    
    new_weights = perceptron(input_data, expected_data, learning_rate, epochs, weights)

    print("DESPUES\nWeights: ", new_weights)
    for j in range(len(input_data)):
        print(f"Resolucion: {expected_data[j]} == {simple_escalon(np.dot(new_weights[1:], input_data[j][1:]) - weights[0])}")
    """ print("Accuracy perceptron:", accuracy(expected_data, weights)) """

if __name__ == "__main__":
    main()