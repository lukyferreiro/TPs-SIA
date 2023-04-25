from src.utils import destructure_data, get_data
from src.perceptron import Perceptron
import json

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    perceptron_type, learning_rate, epochs, bias, beta, min_error, training_percentage = destructure_data(data)
    input_data, expected_data = get_data(bias)

    perceptron = Perceptron(len(input_data[0]), perceptron_type, learning_rate, epochs, beta, min_error, training_percentage)
    perceptron.train(input_data, expected_data)


if __name__ == "__main__":
    main()