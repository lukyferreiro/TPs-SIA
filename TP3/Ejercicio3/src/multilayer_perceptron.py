import numpy as np
import math

class MultilayerPerceptron:
    
    def __init__(self, input_data, expected_data, learning_rate, epochs, training_percentage, qty_hidden_layers, qty_nodes_in_hidden_layers, output_activation, hidden_activation):
        self.training_percentage = training_percentage

        self.input_data = input_data
        self.expected_data = expected_data
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.output_activation = output_activation
        self.hidden_activation = hidden_activation

        self.qty_hidden_layers = qty_hidden_layers
        self.qty_nodes_in_hidden_layer = qty_nodes_in_hidden_layers

        self.weights = self.__init_weights()

        self.min, self.max = self.__calculate_min_and_max(expected_data)

    
    def __init_weights(self):
        parameters = {}
        num_layers = self.qty_hidden_layers + 1
        for l in range(num_layers):
            parameters['W'+str(l)] = 2 * np.random.rand(self.qty_nodes_in_hidden_layer[l], self.qty_nodes_in_hidden_layer[l-1]) - 1

        print(parameters)
        return parameters
    
    def __calculate_min_and_max(self, expected_data):
        return np.min(expected_data), np.max(expected_data)

        def multilayer_perceptron(X, Y, input_handler: InputHandler):
    
    errors = []
    parameters = init_parameters(input_handler.layer_dims, input_handler.apply_bias)    
    
    num_layers = len(input_handler.layer_dims)
    if (input_handler.optimizer == MOMENTUM):
        vel = init_velocity(parameters, num_layers, input_handler.apply_bias)
    elif (input_handler.optimizer == ADAM):
        M, V = init_adam(parameters, num_layers, input_handler.apply_bias)

    t = 0
    for epoch in range(1, input_handler.num_epochs+1):
        if (epoch % 1000 == 0):
            print(f"Epoch #{epoch}")
        minibatches = random_mini_batches(X, Y, input_handler.batch_size, epoch)
        total_error = []
        for minibatch in minibatches:
            (minibatch_X, minibatch_Y) = minibatch
            O, caches = model_forward(minibatch_X, parameters, input_handler.apply_bias, input_handler.hidden_activation, input_handler.output_activation)
            total_error.append(compute_error(O, minibatch_Y, input_handler.output_activation))
            gradients = model_backward(O, minibatch_Y, caches, input_handler.hidden_activation, input_handler.output_activation, input_handler.apply_bias)
            if (input_handler.optimizer == MOMENTUM):
                parameters, vel = update_params_momentum(parameters, gradients, input_handler.learning_rate, vel, input_handler.momentum_alpha, num_layers, input_handler.apply_bias)
            elif (input_handler.optimizer == ADAM):
                t = t + 1
                parameters, M, V = update_params_adam(parameters, gradients, input_handler.learning_rate, M, V, t, input_handler.beta1, input_handler.beta2, input_handler.epsilon, num_layers, input_handler.apply_bias)
            else:
                parameters = update_params_gd(parameters, gradients, input_handler.learning_rate, num_layers, input_handler.apply_bias)
        errors.append(np.mean(total_error))
        if (input_handler.use_adaptive_etha and epoch >= input_handler.adaptive_etha['after']):
            n = input_handler.adaptive_etha['after']
            delta_e = np.mean(errors[-n:])
            if (delta_e < 0):
                delta_etha = input_handler.adaptive_etha['a']
            elif (delta_e > 0):
                delta_etha = - input_handler.adaptive_etha['b'] * input_handler.learning_rate
            else:
                delta_etha = 0
            input_handler.learning_rate += delta_etha
    return parameters, errors
