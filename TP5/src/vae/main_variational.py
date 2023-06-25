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
LATENT_SIZE = 2
HIDDEN_SIZE = 100
HIDDEN_SIZE2 = 200
HIDDEN_SIZE3 = 300

def plot_latent_space_vae(vae, n=10, figsize=15, digit_size=28):
    scale = 1.0
    figure = np.zeros((digit_size * n, digit_size * n))
    grid_x = np.linspace(-scale, scale, n)
    grid_y = np.linspace(-scale, scale, n)[::-1]

    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            z_sample = np.array([[xi],[yi]])
            x_decoded = vae.decoder.predict(z_sample)
            digit = x_decoded.reshape(digit_size, digit_size)
            figure[
                i * digit_size : (i + 1) * digit_size,
                j * digit_size : (j + 1) * digit_size,
            ] = digit

    plt.figure(figsize=(figsize, figsize))
    start_range = digit_size // 2
    end_range = n * digit_size + start_range
    pixel_range = np.arange(start_range, end_range, digit_size)
    sample_range_x = np.round(grid_x, 1)
    sample_range_y = np.round(grid_y, 1)
    plt.xticks(pixel_range, sample_range_x, rotation=90)
    plt.yticks(pixel_range, sample_range_y)
    plt.xlabel("z[0]")
    plt.ylabel("z[1]")
    plt.imshow(figure, cmap="Greys_r")
    plt.show()

if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()

    x_train_reshaped = np.reshape(x_train, (60000, 28, 28))
    x_train_flattened = np.reshape(x_train_reshaped, (60000, 784))

    dataset_input_list = x_train_flattened
    dataset_input_list = np.expand_dims(dataset_input_list, -1).astype("float32") / 255

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

    vae.train(dataset_input=dataset_input_list, epochs=20)

    plot_latent_space_vae(vae)