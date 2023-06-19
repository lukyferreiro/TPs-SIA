import json
import numpy as np
from src.utils import DataConfig
from src.plots import *
from src.vae2 import VAE, Sampling
from tensorflow import keras

def main(): 
    with open('./config_variational.json', 'r') as f:
        data_config = json.load(f)

    c = DataConfig(data_config)

    LATENT_DIM = c.latent_space_size

    # Encoder
    encoder_inputs = keras.Input(shape=(28, 28, 1))
    x = keras.layers.Conv2D(32, 3, activation="relu", strides=2, padding="same")(encoder_inputs)
    x = keras.layers.Conv2D(64, 3, activation="relu", strides=2, padding="same")(x)
    x = keras.layers.Flatten()(x)
    x = keras.layers.Dense(16, activation="relu")(x)
    z_mean = keras.layers.Dense(LATENT_DIM, name="z_mean")(x)
    z_log_var = keras.layers.Dense(LATENT_DIM, name="z_log_var")(x)
    z = Sampling()([z_mean, z_log_var])
    encoder = keras.Model(encoder_inputs, [z_mean, z_log_var, z], name="encoder")
    encoder.summary()

    # Decoder
    latent_inputs = keras.Input(shape=(LATENT_DIM,))
    x = keras.layers.Dense(7 * 7 * 64, activation="relu")(latent_inputs)
    x = keras.layers.Reshape((7, 7, 64))(x)
    x = keras.layers.Conv2DTranspose(64, 3, activation="relu", strides=2, padding="same")(x)
    x = keras.layers.Conv2DTranspose(32, 3, activation="relu", strides=2, padding="same")(x)
    decoder_outputs = keras.layers.Conv2DTranspose(1, 3, activation="sigmoid", padding="same")(x)
    decoder = keras.Model(latent_inputs, decoder_outputs, name="decoder")
    decoder.summary()

    # Entrenamos el VAE
    
    (x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
    mnist_digits = np.concatenate([x_train, x_test], axis=0)
    mnist_digits = np.expand_dims(mnist_digits, -1).astype("float32") / 255
    
    vae = VAE(encoder, decoder)
    vae.compile(optimizer=keras.optimizers.Adam())
    vae.fit(mnist_digits, epochs=30, batch_size=128)

    plot_latent_space2(vae)
    
    x_train = np.expand_dims(x_train, -1).astype("float32") / 255
    plot_label_clusters(vae, x_train, y_train)

if __name__ == "__main__":
    main()