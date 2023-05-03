from src.utils import DataConfig
from src.perceptron import MultilayerPerceptron
import json

def main(): 
    with open('./config_2.json', 'r') as f:
        data = json.load(f)
        f.close()

    config = DataConfig(data, 2)
    
    # Combine the layers to create a neural network
    neural_network = MultilayerPerceptron(config.input_data, config.expected_data, config.learning_rate, config.bias,
                                            config.epochs, config.training_type, config.training_percentage, config.k_fold, config.min_error,
                                            config.qty_hidden_layers, config.qty_nodes_in_hidden_layers, 
                                            config.output_activation, config.hidden_activation, config.beta,
                                            config.optimizer_method, config.alpha, config.beta1, config.beta2,
                                            config.epsilon, [-1, 1])
    neural_network.train()

    # print("Achieved accuracy in parity: ", neural_network.accuracy(XTestSet[i], YTestSet[i], [-1, 1]))

if __name__ == "__main__":
    main()
