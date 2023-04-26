from src.utils import destructure_data, get_data
from src.perceptron import Perceptron
import json
import numpy as np

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    perceptron_type, learning_rate, epochs, bias, beta, min_error, training_percentage = destructure_data(data)
    input_data, expected_data = get_data(bias)

    perceptron = Perceptron(input_data, expected_data, perceptron_type, learning_rate, epochs, beta, min_error, training_percentage)
    perceptron.train()

    for i in range(len(input_data)):
        print(f"Predicted:{perceptron.predict(input_data[i])}. Expected: {expected_data[i]}")

    print(perceptron)


if __name__ == "__main__":
    main()