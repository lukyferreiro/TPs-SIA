from src.utils import DataConfig, k_splitting
from src.perceptron import MultilayerPerceptron
import json


def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    config = DataConfig(data, 3)
    

    neural_network = MultilayerPerceptron(config.input_data, config.expected_data, config.learning_rate, config.bias,
                                         config.epochs, config.training_percentage, config.min_error,
                                         config.qty_hidden_layers, config.qty_nodes_in_hidden_layers, 
                                         config.output_activation, config.hidden_activation, config.beta,
                                         config.optimizer_method, config.alpha, config.beta1, config.beta2,
                                         config.epsilon)
    neural_network.train()


    print("Achieved error in numbers: ", neural_network.eval_error(config.input_data, config.expected_data))
    print("Achieved accuracy in numbers: ", neural_network.accuracy_by_node(config.input_data, config.expected_data))

if __name__ == "__main__":
    main()
