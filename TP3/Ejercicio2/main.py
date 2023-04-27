from src.utils import destructure_data, get_data
from src.perceptron import Perceptron
import json

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    perceptron_type, learning_rate, epochs, bias, beta, min_error, training_percentage, k = destructure_data(data)
    input_data, expected_data = get_data(bias)

    perceptron = Perceptron(input_data, expected_data, perceptron_type, learning_rate, epochs, beta, min_error, training_percentage, k)
    perceptron.train_k_fold()
    print(perceptron)


if __name__ == "__main__":
    main()