from src.utils import DataConfig
from src.perceptron import MultilayerPerceptron
import json

def main(): 
    with open('./config_1.json', 'r') as f:
        data = json.load(f)
        f.close()

    config = DataConfig(data, 1)

    perceptron = MultilayerPerceptron(config.input_data, config.expected_data, config.learning_rate, config.bias,
                                    config.epochs, config.training_type, config.training_percentage, config.k_fold, config.min_error,
                                    config.qty_hidden_layers, config.qty_nodes_in_hidden_layers, 
                                    config.output_activation, config.hidden_activation, config.beta,
                                    config.optimizer_method, config.alpha, config.beta1, config.beta2,
                                      config.epsilon, [-1,1])
    
    mse_errors, current_epoch, acurracy, test_mse = perceptron.train()
    print(perceptron)

    print("Achieved accuracy in XOR: ", perceptron.accuracy(config.input_data, config.expected_data, [-1,1]))

    perceptron.plot(mse_errors, current_epoch)

    #for i in range(len(config.input_data)):
     #   print(f"Predicted: {config.input_data[i][0]} XOR {config.input_data[i][1]} = {perceptron.predict(config.input_data[i])}. Expected: {config.exp[i]}")

if __name__ == "__main__":
    main()