from src.utils import destructure_data
from src.data import operation_data
from src.perceptron import Perceptron
import numpy as np
import json

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    operation, learning_rate, epochs, bias = destructure_data(data)
    input_data, expected_data = operation_data(operation, bias)

    perceptron= Perceptron(len(input_data[0]), learning_rate, epochs)
    perceptron.train(input_data, expected_data)

    print(f'{operation}')
    for i in range(len(input_data)):
        print(f"Predicted: {input_data[i][1]} {operation} {input_data[i][2]} = {perceptron.predict(input_data[i])}. Expected: {expected_data[i]}")


if __name__ == "__main__":
    main()