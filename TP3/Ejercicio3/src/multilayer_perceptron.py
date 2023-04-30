import numpy as np


class MultilayerPerceptron:

    def __init__(self, input_data, expected_data, learning_rate, epochs, training_percentage, qty_hidden_layers,
                 qty_nodes_in_hidden_layers, output_activation, hidden_activation, optimization_method,gradients):
        self.training_percentage = training_percentage

        self.input_data = input_data
        self.expected_data = expected_data
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.gradients = gradients
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
            vel = self.__init_velocity()
        elif input_handler.optimizer == 'ADAM':
            M, V = self.__init_adam()

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
                parameters, vel = __update_params_momentum(self, gradients, vel, input_handler.momentum_alpha)
            elif input_handler.optimizer == 'ADAM':
                t += 1
                parameters, M, V = __update_params_adam(self, gradients, M, V, t, input_handler.beta1,
                                                        input_handler.beta2, input_handler.epsilon)
            else:
                parameters = __update_params_gd(self, gradients)

        # Cálculo del error medio y almacenamiento
        errors.append(np.mean(total_error))

        return parameters, errors

    def __excitation_backward(self):
        pass #TODO

    def __excitation_forward(self):
        pass  # TODO
    def __excitation_activation_forward(self):
        pass #TODO

    def __excitation_activation_backward(self):
        pass #TODO

    def __model_forward(self):
        V = self.input_data
        caches = []
        L = len(self.weights) // 2  # includes weights and biases
        # activate hidden layers
        for l in range(1, L):  # l=0 is the input
            V_prev = V
            b = self.weights['b' + str(l)]
            V, cache = excitation_activation_forward(self.weights['W' + str(l)], b, self.hidden_activation)
            caches.append(cache)
            # activate output layer
            O, cache = excitation_activation_forward(self.weights['W' + str(L)], self.weights['b' + str(L)],
                                                     self.output_activation)
        caches.append(cache)
        return O, caches

    def __model_backward(self,O, Y, caches):
        gradients = {}
        L = len(caches)  # number of layers
        Y = Y.reshape(O.shape)
        dO = O - Y
        current_cache = caches[L - 1]
        gradients['dV' + str(L - 1)], gradients['dW' + str(L)], gradients[
                'db' + str(L)] = excitation_activation_backward()
        for l in reversed(range(L - 1)):
            current_cache = caches[l]
                gradients['dV' + str(l)], gradients['dW' + str(l + 1)], gradients[
                    'db' + str(l + 1)] = excitation_activation_backward(self.gradients['dV' + str(l + 1)], current_cache,
                                                                        self.hidden_activation)
        return

    def optimization_selector(self):
        switcher = {
            "MOMENTUM": self.__init_velocity(),
            "ADAM": self.__init_adam(),
            "GRADIENT": self.__update_params_gd()
        }
        return switcher.get(self.optimization_method, "Metodo de optimizacion invalido")

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
    def __update_params_momentum(self, gradients, vel, alpha):
        parameters = self.weights.copy()
        for l in range(1, self.qty_hidden_layers):
            vel['dW' + str(l)] = alpha * vel['dW' + str(l)] + (1 - alpha) * gradients['dW' + str(l)]
            parameters['W' + str(l)] = parameters['W' + str(l)] - self.learning_rate * vel['dW' + str(l)]
            vel['db' + str(l)] = alpha * vel['db' + str(l)] + (1 - alpha) * gradients['db' + str(l)]
            parameters['b' + str(l)] = parameters['b' + str(l)] - self.learning_rate * vel['db' + str(l)]
        return parameters, vel


    def __logistic_prediction(self):
        O, _ = self.model_forward(self)
        P = 1 * (O > 0.5)
        return O, P

    def __linear_prediction(self):
        O, _ = self.model_forward(self)
        return O, _

    def __tanh_prediction(self):
        O, _ = self.__model_forward(self)
        P = 2 * (O > 0.5) - 1
        return O, P

    def __predict(self):
        if self.output_activation == SIGMOID:
            return self.__logistic_prediction(self)
        return self.__tanh_prediction(self)

    def __predict_decision_boundary(self):
        O, _ = self.__model_forward(self)
        P = (O > 0.5)
        return P

    def __predict_multiclass(self):
        O, _ = self.__model_forward(self)
        P = []
        for output in O:
            max_val = np.max(output)
            P.append(1 * (output == max_val))
        return O, P
