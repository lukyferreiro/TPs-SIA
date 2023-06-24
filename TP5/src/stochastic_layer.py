import numpy as np
from src.layer import Layer

class StochasticLayer():
    def __init__(self, neuron_count, input_size, activation_method, beta):
        self.input_size = input_size
        self.neuron_count = neuron_count
        self.mean = Layer(self.neuron_count, self.input_size, activation_method, beta)
        self.logVar = Layer(self.neuron_count, self.input_size, activation_method, beta)

    def activate(self, input):
        self.latentMean = self.mean.activate(input)
        self.latentLogVar = self.logVar.activate(input)
        self.epsilon = np.random.standard_normal(size=self.neuron_count)
        self.sample = self.latentMean + np.exp(self.latentLogVar / 2.) * self.epsilon
        return self.sample

    def apply_delta(self, lastGradient):
        gradLogVar = {}
        gradMean = {}
        tmp = self.neuron_count * lastGradient.shape[1]

        # KL divergence gradients
        gradLogVar["KL"] = (np.exp(self.latentLogVar) - 1) / (2 * tmp)
        gradMean["KL"] = self.latentMean / tmp

        # MSE gradients
        gradLogVar["MSE"] = 0.5 * lastGradient * self.epsilon * np.exp(self.latentLogVar / 2.)
        gradMean["MSE"] = lastGradient

        # backpropagate gradients thorugh self.mean and self.logVar
        return self.mean.apply_delta(gradMean["KL"] + gradMean["MSE"]) + self.logVar.apply_delta(
            gradLogVar["KL"] + gradLogVar["MSE"])

    def calc_error_d(self, output):
        # output.shape[1] == batchSize
        return - np.sum(1 + self.latentLogVar - np.square(self.latentMean) - np.exp(self.latentLogVar)) / (
                    2 * self.neuron_count * output.shape[1])
