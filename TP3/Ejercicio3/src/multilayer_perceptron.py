import numpy as np
class MultilayerPerceptron:

    def __init__(self, input_data, expected_data, learning_rate, epochs, training_percentage, qty_hidden_layers,
                 qty_nodes_in_hidden_layers, output_activation, hidden_activation,optimization_method):
        self.training_percentage = training_percentage

        self.input_data = input_data
        self.expected_data = expected_data
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.output_activation = output_activation
        self.hidden_activation = hidden_activation
        self.optimization_method = optimization_method
        self.qty_hidden_layers = qty_hidden_layers
        self.qty_nodes_in_hidden_layer = qty_nodes_in_hidden_layers

        self.weights = self.__init_weights()

        self.min, self.max = self.__calculate_min_and_max(expected_data)

    def __init_weights(self):
        parameters = {}
        num_layers = self.qty_hidden_layers + 1
        for l in range(num_layers):
            parameters['W' + str(l)] = 2 * np.random.rand(self.qty_nodes_in_hidden_layer[l],
                                                          self.qty_nodes_in_hidden_layer[l - 1]) - 1

        print(parameters)
        return parameters

    def __calculate_min_and_max(self, expected_data):
        return np.min(expected_data), np.max(expected_data)


    def train(self):
        # Inicializar parámetros de la red neuronal
        parameters = self.__init_weights()

        # Inicializar velocidad o momentos de primer y segundo orden según el algoritmo de optimización seleccionado
        if input_handler.optimizer == 'MOMENTUM':
            vel = __init_velocity(self)
        elif input_handler.optimizer == 'ADAM':
            M, V = __init_adam(self)

        # Iniciar bucle de entrenamiento por épocas
        errors = []
        for epoch in range(1, self.epochs + 1):
            if epoch % 1000 == 0:
                print(f"Epoch #{epoch}")

            total_error = []

            # Propagación hacia adelante
            O, caches = model_forward(self.input_data, parameters,
                                      self.hidden_activation, self.output_activation)

            # Cálculo del error y almacenamiento
            total_error.append(compute_error(O, self.expected_data, self.output_activation))

            # Retropropagación del error y cálculo de gradientes
            gradients = model_backward(O, self.expected_data, caches, self.hidden_activation,
                                       self.output_activation)

            # Actualización de parámetros según el algoritmo de optimización seleccionado
            if input_handler.optimizer == 'MOMENTUM':
                parameters, vel = __update_params_momentum(self, gradients,vel,input_handler.momentum_alpha)
            elif input_handler.optimizer == 'ADAM':
                t += 1
                parameters, M, V = __update_params_adam(self, gradients, M, V, t, input_handler.beta1, input_handler.beta2, input_handler.epsilon)
            else:
                parameters = __update_params_gd(self, gradients)

        # Cálculo del error medio y almacenamiento
        errors.append(np.mean(total_error))

        return parameters, errors

    def optimization_selector(self):
        switcher = {
            "MOMENTUM": self.__init_velocity(),
            "ADAM": self.__init_adam(),
            "GRADIENT": self.__update_params_gd()
        }
        return switcher.get(self.optimization_method,"Metodo de optimizacion invalido")

    def __init_adam(self):
        M = {}  # first moment
        V = {}  # second moment
        for l in range(1, self.qty_hidden_layers):
            M['dW' + str(l)] = np.zeros(self.weights['W' + str(l)].shape)
            V['dW' + str(l)] = np.zeros(self.weights['W' + str(l)].shape)
            M['db' + str(l)] = np.zeros(self.weights['b' + str(l)].shape)
            V['db' + str(l)] = np.zeros(self.weights['b' + str(l)].shape)
        return M, V

    def __update_params_adam(self, gradients, M, V, t, beta1, beta2, epsilon):
        parameters = self.weights.copy()
        M_hat = {}
        V_hat = {}
        for l in range(1, self.qty_hidden_layers):
            M['dW' + str(l)] = beta1 * M['dW' + str(l)] + (1 - beta1) * gradients['dW' + str(l)]  # 1st moment estimate
            V['dW' + str(l)] = beta2 * V['dW' + str(l)] + (1 - beta2) * np.power(gradients['dW' + str(l)],
                                                                                 2)  # 2nd moment estimate
            M_hat['dW' + str(l)] = M['dW' + str(l)] / (1 - np.power(beta1, t))  # bias-corrected 1st moment estimate
            V_hat['dW' + str(l)] = V['dW' + str(l)] / (1 - np.power(beta2, t))  # bias-corrected 2nd moment estimate
            parameters['W' + str(l)] = parameters['W' + str(l)] - self.learning_rate * M_hat['dW' + str(l)] / (
            np.sqrt(V_hat['dW' + str(l)]) + epsilon)  # update parameters
            M['db' + str(l)] = beta1 * M['db' + str(l)] + (1 - beta1) * gradients[
            'db' + str(l)]  # 1st moment estimate
            V['db' + str(l)] = beta2 * V['db' + str(l)] + (1 - beta2) * np.power(gradients['db' + str(l)],
                                                                                     2)  # 2nd moment estimate
            M_hat['db' + str(l)] = M['db' + str(l)] / (1 - np.power(beta1, t))  # bias-corrected 1st moment estimate
            V_hat['db' + str(l)] = V['db' + str(l)] / (1 - np.power(beta2, t))  # bias-corrected 2nd moment estimate
            parameters['b' + str(l)] = parameters['b' + str(l)] - self.learning_rate * M_hat['db' + str(l)] / (
                            np.sqrt(V_hat['db' + str(l)]) + epsilon)  # update parameters
        return parameters, M, V

    def __update_params_gd(self, gradients):
        parameters = self.weights.copy()
        for l in range(1, self.qty_hidden_layers):
            parameters['W' + str(l)] = parameters['W' + str(l)] - self.learning_rate * gradients['dW' + str(l)]
            parameters['b' + str(l)] = parameters['b' + str(l)] - self.learning_rate * gradients['db' + str(l)]
        return parameters

    def __init_velocity(self):
        vel = {}
        for l in range(1, self.qty_hidden_layers):
            vel['dW' + str(l)] = np.zeros(self.weights['W' + str(l)].shape)
            vel['db' + str(l)] = np.zeros(self.weights['b' + str(l)].shape)
        return vel

# Use gradient descent with momentum to update the parameters
    def __update_params_momentum(self, gradients,vel, alpha):
        parameters = self.weights.copy()
        for l in range(1, self.qty_hidden_layers):
            vel['dW' + str(l)] = alpha * vel['dW' + str(l)] + (1-alpha) * gradients['dW' + str(l)]
            parameters['W' + str(l)] = parameters['W' + str(l)] - self.learning_rate * vel['dW' + str(l)]
            vel['db' + str(l)] = alpha * vel['db' + str(l)] + (1-alpha) * gradients['db' + str(l)]
            parameters['b' + str(l)] = parameters['b' + str(l)] - self.learning_rate * vel['db' + str(l)]
        return parameters, vel
