import numpy as np
import copy

from activations import Identity
from loss import MSE
from optimizers import Adam
from stochastic_layer import Dense

class Sampler():
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

        # KL divergence gradients
        gradLogVar["KL"] = (np.exp(self.latentLogVar) - 1) / (2 * tmp)
        gradMean["KL"] = self.latentMean / tmp

        # MSE gradients
        gradLogVar["MSE"] = 0.5 * lastGradient * self.epsilon * np.exp(self.latentLogVar / 2.)
        gradMean["MSE"] = lastGradient

        # backpropagate gradients thorugh self.mean and self.logVar
        return self.mean.backward(gradMean["KL"] + gradMean["MSE"]) + self.logVar.backward(
            gradLogVar["KL"] + gradLogVar["MSE"])

    def getKLDivergence(self, output):
        # output.shape[1] == batchSize
        return - np.sum(1 + self.latentLogVar - np.square(self.latentMean) - np.exp(self.latentLogVar)) / (
                    2 * self.outputDim * output.shape[1])

class MLP():
    def __init__(self):
        self.layers = []
        self.loss = None

    def addLayer(self, layer):
        self.layers.append(layer)

    def feedforward(self, input_data, output_history=None):
        for layer in self.layers:
            input_data = layer.feedforward(input_data)
            if output_history is not None:
                output_history.append(input_data)

        return input_data

    def predict(self, input_data):
        input_data = input_data.reshape((input_data.shape[0], 1))
        return self.feedforward(input_data)

    def backpropagate(self, output, useLoss=True, updateParameters=True):
        if useLoss:
            # step 1:
            lastGradient = self.loss.derivative(output, self.layers[-1].a) * self.layers[-1].activation.derivative(
                self.layers[-1].z)
            # step 2:
            isOutputLayer = True
            for layer in self.layers[::-1]:
                lastGradient = layer.backward(lastGradient, outputLayer=isOutputLayer)
                isOutputLayer = False

        else:
            isOutputLayer = False
            lastGradient = output
            for layer in self.layers[::-1]:
                lastGradient = layer.backward(lastGradient, outputLayer=isOutputLayer)

    def train(self, dataset_input, dataset_output, epochs=1, batchSize=1):
        # set batch size before training
        for layer in self.layers:
            layer.setBatchSize(batchSize)

        for i in range(epochs):
            for j in range(len(dataset_input)):
                input_reshaped = np.reshape(dataset_input[j], (len(dataset_input[j]), batchSize))
                output_reshaped = np.reshape(dataset_output[j], (len(dataset_output[j]), batchSize))

                self.feedforward(input_reshaped)
                self.backpropagate(output_reshaped)

    def __str__(self):
        out = "-" * 20 + " MULTI LAYER PERCEPTRON (MLP) " + "-" * 20 + "\n\n"
        out += f"HIDDEN LAYERS = {len(self.layers) - 2} \n"
        out += f"TOTAL PARAMETERS = {sum(l.numParameters() for l in self.layers)} \n\n"
        for i, layer in enumerate(self.layers):
            out += f" *** {i + 1}. Layer: *** \n"
            out += str(layer) + "\n"
        out += "-" * 70 + "\n"
        return out
    
    def __repr__(self) -> str:
        return self.__str__()

class VAE():
    def __init__(self, encoder=None, sampler=None, decoder=None):
        self.layers = []
        self.loss = None

        if encoder != None and sampler != None and decoder != None:
            self.layers = encoder.layers + [sampler.mean, sampler.logVar] + decoder.layers
            self.encoder = encoder
            self.sampler = sampler
            self.decoder = decoder
            self.decoder.loss = MSE()

    def feedforward(self, input, output_history=None):
        encoderOutput = self.encoder.feedforward(input, output_history)
        sample = self.sampler.feedforward(encoderOutput)
        if output_history is not None:
            output_history.append(sample)
        decoderOutput = self.decoder.feedforward(sample, output_history)

        return decoderOutput

    def backpropagate(self, output):
        self.decoder.backpropagate(output)
        decoderGradient = self.decoder.layers[0].gradient
        samplerGradient = self.sampler.backpropagate(decoderGradient)
        self.encoder.backpropagate(samplerGradient, useLoss=False)

    def train(self, dataset_input, epochs=1, batchSize=1):
        for layer in self.layers:
            layer.setBatchSize(batchSize)

        for i in range(epochs):
            print(i)
            for j in range(15):
                input_reshaped = np.reshape(dataset_input[j], (len(dataset_input[j]), batchSize))
                output_reshaped = np.reshape(dataset_input[j], (len(dataset_input[j]), batchSize))

                self.feedforward(input_reshaped)
                self.backpropagate(output_reshaped)

    def getLoss(self, output):
        return self.decoder.getLoss(output) + self.sampler.getKLDivergence(output)

    def __str__(self):
        out = "-" * 20 + " VARIATIONAL AUTOENCODER (VAE) " + "-" * 20 + "\n\n"
        out += f"TOTAL PARAMETERS = {sum(l.numParameters() for l in self.layers)} \n\n"

        out += "#" * 15 + "\n"
        out += "#   ENCODER   #\n"
        out += "#" * 15 + "\n\n"
        for i, layer in enumerate(self.encoder.layers):
            out += f" *** {i + 1}. Layer: *** \n"
            out += str(layer) + "\n"

        out += "#" * 15 + "\n"
        out += "#   SAMPLER   #\n"
        out += "#" * 15 + "\n\n"
        out += f" *** MEAN Layer: *** \n"
        out += str(self.sampler.mean) + "\n"
        out += f" *** LOG_VAR Layer: *** \n"
        out += str(self.sampler.logVar) + "\n"

        out += "#" * 15 + "\n"
        out += "#   DECODER   #\n"
        out += "#" * 15 + "\n\n"
        for i, layer in enumerate(self.decoder.layers):
            out += f" *** {i + 1}. Layer: *** \n"
            out += str(layer) + "\n"

        out += "-" * 70 + "\n"
        return out
    
    def __repr__(self) -> str:
        return self.__str__()
    