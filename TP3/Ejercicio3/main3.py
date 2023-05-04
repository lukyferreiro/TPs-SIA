from src.utils import DataConfig
from src.perceptron import MultilayerPerceptron
import json
import numpy as np
import copy

def alter_data(set, mutation_p):
    for elem in set:
        for i in range(len(elem)):
            if np.random.default_rng().random() < mutation_p:
                elem[i] = (elem[i] + 1) % 2

def main(): 
    with open('./config_3.json', 'r') as f:
        data = json.load(f)
        f.close()

    config = DataConfig(data, 3)

    perceptron = MultilayerPerceptron(config.input_data, config.expected_data, config.learning_rate, config.bias,
                                            config.epochs, config.training_type, config.training_percentage, config.k_fold, config.min_error,
                                            config.qty_hidden_layers, config.qty_nodes_in_hidden_layers, 
                                            config.output_activation, config.hidden_activation, config.beta,
                                            config.optimizer_method, config.alpha, config.beta1, config.beta2,
                                            config.epsilon, config.expected_data)
    
    mse_errors, current_epoch, acurracy, test_mse = perceptron.train()

    for i in [round(0.1*i,2) for i in range(1,6)]:
        print(f"----------------Mutacion={i}----------------")
        original_input = copy.deepcopy(config.input_data)
        alter_data(original_input, i)
        expected = perceptron.normalize_image(config.expected_data, config.output_activation)
        accuracy = perceptron.accuracy_multiple(original_input, expected)
        print(f"Accuracy = {accuracy}")

if __name__ == "__main__":
    main()
