from src.utils import DataConfig, k_splitting
from src.perceptron import MultilayerPerceptron
import json
import numpy as np

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)
        f.close()

    config = DataConfig(data, 2)
    
    XTrainSet, YTrainSet, XTestSet, YTestSet = k_splitting(config.input_data, config.expected_data, 5)

    for i in range(len(XTrainSet)):
        print("\n <--------------------------------------------------------------->")
        print("Testing partition set-" + str(i))
        print("\nTrain set: " + str(XTrainSet[i]) + "\n")
        print("Test set: " + str(XTestSet[i]) + "\n")

        # Combine the layers to create a neural network
        neural_network = MultilayerPerceptron(XTrainSet[i], YTrainSet[i], config.learning_rate, config.bias,
                                              config.epochs, config.training_percentage, config.min_error,
                                              config.qty_hidden_layers, config.qty_nodes_in_hidden_layers, 
                                              config.output_activation, config.hidden_activation, config.beta,
                                              config.optimizer_method, config.alpha, config.beta1, config.beta2,
                                              config.epsilon)
        neural_network.train()

        print(XTestSet[i])

        print("Achieved error in parity: ", neural_network.eval_error(XTestSet[i], YTestSet[i]))
        print("Achieved accuracy in parity: ", neural_network.accuracy(XTestSet[i], YTestSet[i], [-1, 1]))

if __name__ == "__main__":
    main()
