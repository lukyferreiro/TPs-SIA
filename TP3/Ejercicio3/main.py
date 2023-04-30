from src.utils import DataConfig
from src.multilayer_perceptron import MultilayerPerceptron
import json

import matplotlib.pyplot as plt

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    config = DataConfig(data)

    perceptron = MultilayerPerceptron(config.input_data, config.expected_data, config.learning_rate, config.bias,
                                      config.epochs, config.training_percentage, config.min_error,
                                      config.qty_hidden_layers, config.qty_nodes_in_hidden_layers, config.layer_dims, 
                                      config.output_activation, config.hidden_activation, config.beta,
                                      config.optimizer_method, config.alpha, config.beta1, config.beta2,
                                      config.epsilon)
    
    weights, errors = perceptron.train()
    print(perceptron)

    for i in range(len(config.input_data)):
        print(f"Predicted: {config.input_data[i][0]} XOR {config.input_data[i][1]} = {perceptron.predict(config.input_data[i])}. Expected: {config.exp[i]}")

if __name__ == "__main__":
    main()