from src.utils import destructure_data, get_data
from src.multilayer_perceptron import MultilayerPerceptron
import json

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    input_data, expected_data, learning_rate, epochs, training_percentage, qty_hidden_layers, qty_nodes_in_hidden_layers, output_activation, hidden_activation = destructure_data(data)

    perceptron = MultilayerPerceptron(input_data, expected_data, learning_rate, epochs, training_percentage, qty_hidden_layers, qty_nodes_in_hidden_layers, output_activation, hidden_activation)
    perceptron.train()
    print(perceptron)


if __name__ == "__main__":
    main()