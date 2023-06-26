import numpy as np
from loss import MSE

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
            lastGradient = self.loss.derivative(output, self.layers[-1].a) * self.layers[-1].activation.derivative(self.layers[-1].z)
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
        for layer in self.layers:
            layer.setBatchSize(batchSize)

        for _ in range(epochs):
            for j in range(len(dataset_input)):
                input_reshaped = np.reshape(dataset_input[j], (len(dataset_input[j]), batchSize))
                output_reshaped = np.reshape(dataset_output[j], (len(dataset_output[j]), batchSize))

                self.feedforward(input_reshaped)
                self.backpropagate(output_reshaped)

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
            for j in range(10000):
                input_reshaped = np.reshape(dataset_input[j], (len(dataset_input[j]), batchSize))
                output_reshaped = np.reshape(dataset_input[j], (len(dataset_input[j]), batchSize))
                self.feedforward(input_reshaped)
                self.backpropagate(output_reshaped)

    def getLoss(self, output):
        return self.decoder.getLoss(output) + self.sampler.getKLDivergence(output)
    