from stochastic_layer import Dense, StochasticLayer
from loss import MSE    
from optimizers import Adam
from activations import ReLU, Sigmoid
from variational_autoencoder import MLP, VAE
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras

INPUT_ROWS = 28
INPUT_COLS = 28
INPUT_SIZE = INPUT_COLS * INPUT_ROWS
LATENT_SIZE = 20
HIDDEN_SIZE = 100
HIDDEN_SIZE2 = 200
HIDDEN_SIZE3 = 300

if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

    x_train_reshaped = np.reshape(x_train, (60000, 28, 28))
    x_train_flattened = np.reshape(x_train_reshaped, (60000, 784))

    dataset_input_list = x_train_flattened
    dataset_input_list = np.expand_dims(dataset_input_list, -1).astype("float32") / 255

    print(dataset_input_list[0])

    # Set the learning rate and optimizer for training
    optimizer = Adam(0.0001)

    encoder = MLP()
    encoder.addLayer(Dense(inputDim=INPUT_SIZE, outputDim=HIDDEN_SIZE3, activation=ReLU(), optimizer=optimizer))
    encoder.addLayer(Dense(inputDim=HIDDEN_SIZE3, outputDim=HIDDEN_SIZE2, activation=ReLU(), optimizer=optimizer))
    encoder.addLayer(Dense(inputDim=HIDDEN_SIZE2, outputDim=HIDDEN_SIZE, activation=ReLU(), optimizer=optimizer))
    sampler = StochasticLayer(HIDDEN_SIZE, LATENT_SIZE, optimizer=optimizer)

    decoder = MLP()
    decoder.addLayer(Dense(inputDim=LATENT_SIZE, outputDim=HIDDEN_SIZE, activation=ReLU(), optimizer=optimizer))
    decoder.addLayer(Dense(inputDim=HIDDEN_SIZE, outputDim=HIDDEN_SIZE2, activation=ReLU(), optimizer=optimizer))
    decoder.addLayer(Dense(inputDim=HIDDEN_SIZE2, outputDim=HIDDEN_SIZE3, activation=ReLU(), optimizer=optimizer))
    decoder.addLayer(Dense(inputDim=HIDDEN_SIZE3, outputDim=INPUT_SIZE, activation=Sigmoid(), optimizer=optimizer))

    vae = VAE(encoder, sampler, decoder)

    vae.train(dataset_input=dataset_input_list, epochs=1000)
