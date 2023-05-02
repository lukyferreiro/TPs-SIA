import numpy as np
import math 

class Layer(): 
    def __init__(self, neuron_count, input_size, activation_method, beta):
        self.neuron_count = neuron_count
        self.input_size = input_size
        self.weights = 0.4 * np.random.default_rng().random((input_size, neuron_count)) - 0.2
        self.bias = 0.4 * np.random.default_rng().random(neuron_count) - 0.2
        self.error_d = None
        self.activation_method = activation_method
        self.beta = beta

        # MOMENTUM
        self.prev_delta = 0
        self.prev_bias = 0

        # ADAM
        self.m = 0 
        self.v = 0
        self.m_bias = np.zeros(self.bias.shape)
        self.v_bias = np.zeros(self.bias.shape)

    def apply_delta(self, last_activation, learn_rate, t, optimization_method, alpha, beta1, beta2, epsilon):
        act_mat = np.matrix(last_activation)
        err_mat = np.matrix(self.error_d)

        self.__update_weights(act_mat, err_mat, learn_rate, t, optimization_method, alpha, beta1, beta2, epsilon)

    def __update_weights(self, act_mat, err_mat, learn_rate, t, optimization_method, alpha, beta1, beta2, epsilon):
        if optimization_method == "MOMENTUM":
            self.weights += learn_rate * np.dot(act_mat.T, err_mat) + alpha * self.prev_delta
            self.prev_delta = learn_rate * np.dot(act_mat.T, err_mat) + alpha * self.prev_delta
            self.bias += learn_rate * self.error_d + alpha * self.prev_bias
            self.prev_bias = learn_rate * self.error_d + alpha * self.prev_bias
       
        elif optimization_method == "ADAM":
            t += 1
            gt = np.dot(act_mat.T, err_mat)

            # Actualización de weights
            self.m = beta1 * self.m + (1 - beta1) * gt
            self.v = beta2 * self.v + (1 - beta2) * np.power(gt, 2)

            m_mean = self.m / (1 - np.power(beta1, t)) 
            v_mean = self.v / (1 - np.power(beta2, t))

            self.weights += learn_rate * m_mean / (np.sqrt(v_mean) + epsilon)

            # Actualización de bias
            gt_bias = self.error_d

            self.m_bias = beta1 * self.m_bias + (1 - beta1) * gt_bias
            self.v_bias = beta2 * self.v_bias + (1 - beta2) * np.power(gt_bias, 2)

            m_bias_mean = self.m_bias / (1 - np.power(beta1, t))
            v_bias_mean = self.v_bias / (1 - np.power(beta2, t))

            self.bias += learn_rate * m_bias_mean / (np.sqrt(v_bias_mean) + epsilon)
       
        else:
            self.weights += learn_rate * np.dot(act_mat.T, err_mat)
            self.bias += learn_rate * self.error_d

    def calc_error_d(self, inherited_error, activation):
        if(self.activation_method == "TANH"):
            d = self.beta * (1 - activation ** 2)
        else:
            d = 2 * self.beta * activation * (1 - activation)

        self.error_d = inherited_error * d

    def activate(self, feed):
        h = np.dot(feed, self.weights) + self.bias

        if(self.activation_method == "TANH"):
            H_beta = h * self.beta
            return  (np.exp(H_beta) - np.exp(-H_beta)) / (np.exp(H_beta) + np.exp(-H_beta))
        else:
            return 1 / (1 + np.exp(-2 * self.beta * h))

    def __str__(self) -> str:
        return str(self.weights)

    def __repr__(self) -> str:
        return self.__str__()