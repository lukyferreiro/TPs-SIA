import tensorflow as tf
from tensorflow import keras
from keras import layers
import numpy as np
from plots import *

# https://keras.io/examples/generative/vae/

class VAE(keras.Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        latent = 2
        self.initiateEncoder(latent)
        self.initiateDecoder(latent)
        self.total_loss_tracker = keras.metrics.Mean(name="total_loss")
        self.reconstruction_loss_tracker = keras.metrics.Mean(name="reconstruction_loss")
        self.kl_loss_tracker = keras.metrics.Mean(name="kl_loss")

    def train(self, trainset):
        self.compile(optimizer=keras.optimizers.Adam())
        self.fit(trainset, epochs=50, batch_size=100)

    def initiateDecoder(self, latent):
        latInputs = keras.Input(shape=(latent,))
        x = layers.Dense(7 * 7 * 64, activation="relu")(latInputs)
        x = layers.Reshape((7, 7, 64))(x)
        x = layers.Conv2DTranspose(20, 3, activation="relu", strides=2, padding="same")(x)
        x = layers.Conv2DTranspose(10, 3, activation="relu", strides=2, padding="same")(x)
        outputs = layers.Conv2DTranspose(1, 3, activation="sigmoid", padding="same")(x)
        self.decoder = keras.Model(latInputs, outputs, name="decoder")

    def initiateEncoder(self, latent):
        encoder_inputs = keras.Input(shape=(28, 28, 1))  # Esperamos que el input sean de 28x28x1
        x = layers.Conv2D(10, 3, activation="relu", strides=2, padding="same")(encoder_inputs)
        x = layers.Conv2D(20, 3, activation="relu", strides=2, padding="same")(x)
        x = layers.Flatten()(x)
        x = layers.Dense(16, activation="relu")(x)
        z_mean = layers.Dense(latent, name="z_mean")(x)
        z_log_var = layers.Dense(latent, name="z_log_var")(x)
        z = getSample(z_mean, z_log_var)
        self.encoder = keras.Model(encoder_inputs, [z_mean, z_log_var, z], name="encoder")

    @property
    def metrics(self):
        return [
            self.total_loss_tracker,
            self.reconstruction_loss_tracker,
            self.kl_loss_tracker,
        ]

    def train_step(self, data):
        with tf.GradientTape() as tape:
            z_mean, z_log_var, z = self.encoder(data)
            reconstruction = self.decoder(z)
            reconstruction_loss = tf.reduce_mean(
                tf.reduce_sum(keras.losses.binary_crossentropy(data, reconstruction), axis=(1, 2))
            )
            kl_loss = -0.5 * (1 + z_log_var - tf.square(z_mean) - tf.exp(z_log_var))
            kl_loss = tf.reduce_mean(tf.reduce_sum(kl_loss, axis=1))
            total_loss = reconstruction_loss + kl_loss
        grads = tape.gradient(total_loss, self.trainable_weights)
        self.optimizer.apply_gradients(zip(grads, self.trainable_weights))
        self.total_loss_tracker.update_state(total_loss)
        self.reconstruction_loss_tracker.update_state(reconstruction_loss)
        self.kl_loss_tracker.update_state(kl_loss)
        return {
            "loss": self.total_loss_tracker.result(),
            "reconstruction_loss": self.reconstruction_loss_tracker.result(),
            "kl_loss": self.kl_loss_tracker.result(),
        }

def getSample(z_mean, z_log_var):
    z_mean, z_log_var = z_mean, z_log_var
    batch = tf.shape(z_mean)[0]
    dim = tf.shape(z_mean)[1]
    epsilon = tf.keras.backend.random_normal(shape=(batch, dim))
    return z_mean + tf.exp(0.5 * z_log_var) * epsilon

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
trainset = np.concatenate([x_train, x_test], axis=0)
trainset = np.expand_dims(trainset, -1).astype("float32") / 255
vae = VAE()
plot_latent_space_vae(vae)
vae.train(trainset)
plot_latent_space_vae(vae)
trainset = np.expand_dims(x_train, -1).astype("float32") / 255
trainoutputset = np.concatenate([y_train, y_test]).astype("float32") / 255
trainoutputset = np.expand_dims(trainoutputset, -1).astype("float32") / 255
plot_label_clusters(vae, trainset, y_train)