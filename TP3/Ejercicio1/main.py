from src.utils import destructure_data
from src.data import operation_data
from src.perceptron import perceptron, accuracy
#import matplotlib.pyplot as plt
import numpy as np
import json

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
    operation, learning_rate, epochs = destructure_data(data)
    input_data, expected_data = operation_data(operation)

    weights = perceptron(input_data, expected_data, learning_rate, epochs)

    print("weights: ", weights)
    print("Accuracy perceptron:", accuracy(expected_data, weights))

if __name__ == "__main__":
    main()