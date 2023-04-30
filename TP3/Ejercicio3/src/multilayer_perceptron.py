import numpy as np
import math


class MultilayerPerceptron:

    def __init__(self, input_data, expected_data, learning_rate, epochs, training_percentage, min_error,
                 qty_hidden_layers, qty_nodes_in_hidden_layers, output_activation, hidden_activation, beta,
                 optimization_method, alpha, beta1, beta2, epsilon):

        self.min, self.max = self.__calculate_min_and_max(expected_data)
        self.input_data = input_data
        self.expected_data = self.__normalize_image(expected_data)
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.training_percentage = training_percentage
        self.min_error = min_error

        self.qty_hidden_layers = qty_hidden_layers
        self.qty_nodes_in_hidden_layer = qty_nodes_in_hidden_layers
        self.output_activation = output_activation
        self.hidden_activation = hidden_activation
        self.beta = beta

        self.optimization_method = optimization_method
        self.alpha = alpha
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

        self.weights = self.__init_weights()

    def __init_weights(self):
        weights = {}
        num_layers = self.qty_hidden_layers
        for l in range(num_layers):
            weights['W' + str(l)] = 2 * np.random.default_rng().random(self.qty_nodes_in_hidden_layer[l],
                                                                       self.qty_nodes_in_hidden_layer[l - 1]) - 1
            weights['b' + str(l)] = np.zeros((self.qty_nodes_in_hidden_layer[l], 1))

        print(weights)
        return weights

    @staticmethod
    def __calculate_min_and_max(expected_data):
        return np.min(expected_data), np.max(expected_data)

    def __calculate_error(self, O):
        num_examples = len(self.expected_data)
        loss = - np.dot(self.expected_data, np.log(O)) - np.dot(1 - self.expected_data, np.log(1 - O))
        return np.sum(loss) / num_examples

    def train(self):
        # Inicializar velocidad o momentos de primer y segundo orden según el algoritmo de optimización seleccionado
        if self.optimization_method == 'MOMENTUM':
            vel = self.__init_momentum()
        elif self.optimization_method == 'ADAM':
            M, V = self.__init_adam()

        t = 0
        errors = []
        current_epoch = 0
        finished = False

        while current_epoch < self.epochs and not finished:
            total_error = []

            # Forward propagation
            O, caches = self.__forward_propagation()

            # Cálculo del error y almacenamiento
            total_error.append(self.__calculate_error(O))

            # Retropropagación del error y cálculo de gradientes
            gradients = self.__backward_propagation(O, caches)

            # Actualización de parámetros según el algoritmo de optimización seleccionado
            if self.optimization_method == 'MOMENTUM':
                vel = self.__update_weights_momentum(gradients, vel)
            elif self.optimization_method == 'ADAM':
                t += 1
                M, V = self.__update_weights_adam(gradients, M, V, t)
            else:
                self.__update_weights_gd(gradients)

        # Cálculo del error medio y almacenamiento
        errors.append(np.mean(total_error))

        return self.weights, errors

    def predict(self):
        O, _ = self.__forward_propagation()
        return O, _

    # -----------------------FORWARD PROPAGATION-----------------------

    def __forward_propagation(self):
        V = self.input_data
        caches = []
        L = len(self.weights) // 2  # includes weights and biases

        # Activate hidden layers
        for l in range(1, L):  # l=0 is the input
            V_prev = V
            b = self.weights['b' + str(l)]
            V, cache = self.__activation_forward(V_prev, self.weights['W' + str(l)],
                                                 b, self.hidden_activation)
            caches.append(cache)

        # Activate output layer
        O, cache = self.__activation_forward(V, self.weights['W' + str(L)],
                                             self.weights['b' + str(L)],
                                             self.output_activation)
        caches.append(cache)
        return O, caches

    def __activation_forward(self, V_prev, W, b, activation):
        H = np.dot(W, V_prev) + b  # hyperplane with bias
        excitation_cache = (V_prev, W, b)

        switcher = {
            "TANH": self.__activate_forward_tanh(H),
            "LOG": self.__activate_forward_log(H),
        }

        V, activation_cache = switcher.get(activation, "Tipo de activacion invalido")
        cache = (excitation_cache, activation_cache)
        return V, cache

    def __activate_forward_tanh(self, H):
        V = math.tanh(self.beta * H)
        cache = H
        return V, cache

    def __activate_forward_log(self, H):
        V = 1 / (1 + math.pow(math.e, -2 * self.beta * H))
        cache = H
        return V, cache

    # -----------------------BACKWARD PROPAGATION-----------------------

    def __backward_propagation(self, O, caches):
        gradients = {}
        L = len(caches)  # number of layers
        Y = self.expected_data.reshape(O.shape)
        dO = O - Y

        current_cache = caches[L - 1]
        gradients['dV' + str(L - 1)], gradients['dW' + str(L)], gradients['db' + str(L)] = self.__activation_backward(
            dO, current_cache, self.output_activation)

        for l in reversed(range(L - 1)):
            current_cache = caches[l]
            gradients['dV' + str(l)], gradients['dW' + str(l + 1)], gradients[
                'db' + str(l + 1)] = self.__activation_backward(gradients['dV' + str(l + 1)], current_cache,
                                                                self.hidden_activation)

        return gradients

    def __activation_backward(self, dV, cache, activation):
        excitation_cache, activation_cache = cache

        switcher = {
            "TANH": self.__activate_backward_tanh(dV),
            "LOG": self.__activate_backward_log(dV, activation_cache),
        }

        dH = switcher.get(activation, "Tipo de activacion invalido")
        dV_prev, dW, db = self.__excitation_backward(dH)
        return dV_prev, dW, db

    def __activate_backward_tanh(self, cache):
        H = cache
        tanh = math.tanh(self.beta * H)
        dH = self.beta * (1 - tanh ** 2)
        return dH

    def __activate_backward_log(self, dV, cache):
        H = cache
        log = 1 / (1 + math.pow(math.e, -2 * self.beta * H))
        dH = dV * 2 * self.beta * log * (1 - log)
        return dH

    def __excitation_backward(dH, cache):
        V_prev, W, _ = cache
        dV_prev = np.dot(W.T, dH)  # dV_prev = delta_H/delta_V_prev
        num_examples = V_prev.shape[1]
        dW = (1 / num_examples) * np.dot(dH, V_prev.T)  # dW = delta_H/delta_W
        db = (1 / num_examples) * np.sum(dH, axis=1, keepdims=True)  # db = delta_H/delta_b
        return dV_prev, dW, db

    # -----------------------OPTIMIZATION-----------------------

    def __init_momentum(self):
        vel = {}
        for l in range(1, self.qty_hidden_layers):
            vel['dW' + str(l)] = np.zeros(self.weights['W' + str(l)].shape)
            vel['db' + str(l)] = np.zeros(self.weights['b' + str(l)].shape)
        return vel

    # Use gradient descent with momentum to update the parameters
    def __update_weights_momentum(self, gradients, vel):
        weights = self.weights.copy()
        for l in range(1, self.qty_hidden_layers):
            vel['dW' + str(l)] = self.alpha * vel['dW' + str(l)] + (1 - self.alpha) * gradients['dW' + str(l)]
            weights['W' + str(l)] = weights['W' + str(l)] - self.learning_rate * vel['dW' + str(l)]
            vel['db' + str(l)] = self.alpha * vel['db' + str(l)] + (1 - self.alpha) * gradients['db' + str(l)]
            weights['b' + str(l)] = weights['b' + str(l)] - self.learning_rate * vel['db' + str(l)]

        self.weights = weights
        return vel

    def __init_adam(self):
        M = {}  # first moment
        V = {}  # second moment
        for l in range(1, self.qty_hidden_layers):
            M['dW' + str(l)] = np.zeros(self.weights['W' + str(l)].shape)
            V['dW' + str(l)] = np.zeros(self.weights['W' + str(l)].shape)
            M['db' + str(l)] = np.zeros(self.weights['b' + str(l)].shape)
            V['db' + str(l)] = np.zeros(self.weights['b' + str(l)].shape)
        return M, V

    def __update_weights_adam(self, gradients, M, V, t):
        weights = self.weights.copy()
        M_hat = {}
        V_hat = {}
        for l in range(1, self.qty_hidden_layers):
            M['dW' + str(l)] = self.beta1 * M['dW' + str(l)] + (1 - self.beta1) * gradients[
                'dW' + str(l)]  # 1st moment estimate
            V['dW' + str(l)] = self.beta2 * V['dW' + str(l)] + (1 - self.beta2) * np.power(gradients['dW' + str(l)],
                                                                                           2)  # 2nd moment estimate
            M_hat['dW' + str(l)] = M['dW' + str(l)] / (
                        1 - np.power(self.beta1, t))  # bias-corrected 1st moment estimate
            V_hat['dW' + str(l)] = V['dW' + str(l)] / (
                        1 - np.power(self.beta2, t))  # bias-corrected 2nd moment estimate
            weights['W' + str(l)] = weights['W' + str(l)] - self.learning_rate * M_hat['dW' + str(l)] / (
                    np.sqrt(V_hat['dW' + str(l)]) + self.epsilon)  # update parameters
            M['db' + str(l)] = self.beta1 * M['db' + str(l)] + (1 - self.beta1) * gradients[
                'db' + str(l)]  # 1st moment estimate
            V['db' + str(l)] = self.beta2 * V['db' + str(l)] + (1 - self.beta2) * np.power(gradients['db' + str(l)],
                                                                                           2)  # 2nd moment estimate
            M_hat['db' + str(l)] = M['db' + str(l)] / (
                        1 - np.power(self.beta1, t))  # bias-corrected 1st moment estimate
            V_hat['db' + str(l)] = V['db' + str(l)] / (
                        1 - np.power(self.beta2, t))  # bias-corrected 2nd moment estimate
            weights['b' + str(l)] = weights['b' + str(l)] - self.learning_rate * M_hat['db' + str(l)] / (
                    np.sqrt(V_hat['db' + str(l)]) + self.epsilon)  # update parameters

        self.weights = weights
        return M, V

    def __update_params_gd(self, gradients):
        weights = self.weights.copy()
        for l in range(1, self.qty_hidden_layers):
            weights['W' + str(l)] = weights['W' + str(l)] - self.learning_rate * gradients['dW' + str(l)]
            weights['b' + str(l)] = weights['b' + str(l)] - self.learning_rate * gradients['db' + str(l)]

        self.weights = weights

    # -----------------------NORMALIZATION-----------------------

    def __normalize_image(self, values):
        switcher = {
            "TANH": self.__normalize_tanh_image(values),
            "LOG": self.__normalize_log_image(values),
        }

        return switcher.get(self.output_activation, "Tipo de activacion de salida")

    # Normalizacion para [a,b] es: X'=((X-Xmin)/(Xmax-Xmin))(b-a)+a
    def __normalize_tanh_image(self, values):
        # Image = (-1,1)
        return (2 * (values - self.min) / (self.max - self.min)) - 1

    def __normalize_log_image(self, values):
        # Image = (0,1)
        return (values - self.min) / (self.max - self.min)

    def __denormalize_image(self, values):
        switcher = {
            "TANH": self.__denormalize_tanh_image(values),
            "LOG": self.__denormalize_log_image(values),
        }

        return switcher.get(self.output_activation, "Tipo de activacion de salida")

    def __denormalize_tanh_image(self, values):
        return ((values + 1) * (self.max - self.min) * 0.5) + self.min

    def __denormalize_log_image(self, values):
        return values * (self.max - self.min) + self.min
