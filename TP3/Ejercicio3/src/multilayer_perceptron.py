import numpy as np
import math

class MultilayerPerceptron:
    
    def __init__(self, input_data, expected_data, learning_rate, epochs, training_percentage, qty_hidden_layers, qty_nodes_in_hidden_layers, output_activation, hidden_activation):
        self.training_percentage = training_percentage
        self.input_data = input_data
        self.expected_data = expected_data
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.min, self.max = self.__calculate_min_and_max(expected_data)