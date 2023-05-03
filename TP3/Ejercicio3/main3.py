from src.utils import DataConfig, k_splitting
from src.perceptron import MultilayerPerceptron
import json


def main(): 
    with open('./config_3.json', 'r') as f:
        data = json.load(f)
        f.close()

    config = DataConfig(data, 3)

    neural_network = MultilayerPerceptron(config.input_data, config.expected_data, config.learning_rate, config.bias,
                                            config.epochs, config.training_type, config.training_percentage, config.k_fold, config.min_error,
                                            config.qty_hidden_layers, config.qty_nodes_in_hidden_layers, 
                                            config.output_activation, config.hidden_activation, config.beta,
                                            config.optimizer_method, config.alpha, config.beta1, config.beta2,
                                            config.epsilon, config.expected_data)
    
    mse_errors, current_epoch, acurracy, test_mse = neural_network.train()

if __name__ == "__main__":
    main()
