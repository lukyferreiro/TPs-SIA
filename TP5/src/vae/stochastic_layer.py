import numpy as np
import copy
from activations import Sigmoid, Identity
from optimizers import Adam

class Dense():
    def __init__(self, inputDim = 1, outputDim = 1, activation = Sigmoid(), optimizer = Adam()):
        self.inputDim = inputDim
        self.outputDim = outputDim
        self.activation = activation
        self.weightOptimizer = copy.copy(optimizer)
        self.biasOptimizer = copy.copy(optimizer)
        limit = np.sqrt(6 / (inputDim + outputDim)) 
        self.weight = np.random.uniform(-limit, limit,(outputDim, inputDim))
        self.bias = np.zeros(outputDim)

    def feedforward(self, input):
        if input.ndim == 1:
            input = np.squeeze(input).reshape((input.shape[0], self.batchSize))

        self.input = input
        self.z = np.dot(self.weight, self.input) + np.tile(self.bias, (self.input.shape[1], 1)).T
        self.a = self.activation.apply(self.z)
        return self.a

    def backward(self, lastGradient, outputLayer = False):
        oldWeight = np.copy(self.weight)
        if not outputLayer:
            lastGradient *= self.activation.derivative(self.z)

        gradWeight = np.dot(lastGradient, self.input.T)
        gradBias = np.sum(lastGradient, axis=1)
        self.weightOptimizer.optimize(self.weight, gradWeight)
        self.biasOptimizer.optimize(self.bias, gradBias)
        self.gradient = np.dot(oldWeight.T, lastGradient)
        return self.gradient

    def numParameters(self):
        weightShape = self.weight.shape
        return weightShape[0]*weightShape[1] + self.bias.shape[0]

    def setBatchSize(self, batchSize):
        self.batchSize = batchSize
        self.weightOptimizer.setLearningFactor(self.batchSize)
        self.biasOptimizer.setLearningFactor(self.batchSize)
    
class StochasticLayer():
    def __init__(self, inputDim=1, outputDim=1, optimizer=Adam()):
        self.inputDim = inputDim
        self.outputDim = outputDim
        self.mean = Dense(self.inputDim, self.outputDim, activation=Identity(), optimizer=copy.copy(optimizer))
        self.logVar = Dense(self.inputDim, self.outputDim, activation=Identity(), optimizer=copy.copy(optimizer))

    def feedforward(self, input):
        self.latentMean = self.mean.feedforward(input)
        self.latentLogVar = self.logVar.feedforward(input)
        self.epsilon = np.random.standard_normal(size=(self.outputDim, input.shape[1]))
        self.sample = self.latentMean + np.exp(self.latentLogVar / 2.) * self.epsilon
        return self.sample

    def backpropagate(self, lastGradient):
        gradLogVar = {}
        gradMean = {}
        tmp = self.outputDim * lastGradient.shape[1]
        gradLogVar["KL"] = (np.exp(self.latentLogVar) - 1) / (2 * tmp)
        gradMean["KL"] = self.latentMean / tmp
        gradLogVar["MSE"] = 0.5 * lastGradient * self.epsilon * np.exp(self.latentLogVar / 2.)
        gradMean["MSE"] = lastGradient
        return self.mean.backward(gradMean["KL"] + gradMean["MSE"]) + self.logVar.backward(gradLogVar["KL"] + gradLogVar["MSE"])

    def getKLDivergence(self, output):
        return - np.sum(1 + self.latentLogVar - np.square(self.latentMean) - np.exp(self.latentLogVar)) / (2 * self.outputDim * output.shape[1])
