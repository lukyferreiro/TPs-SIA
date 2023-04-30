from src.utils import DataConfig
from src.multilayer_perceptron import MultilayerPerceptron
import json

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
    perceptron.train()
    print(perceptron)


if __name__ == "__main__":
    main()