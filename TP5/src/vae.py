from keras import backend as K
from keras import metrics
from keras.layers import Input, Dense, Lambda
from keras.models import Model

class VAE:
    def __init__(self, x, epochs, latent_space_size, qty_nodes_in_hidden_layers):
        self.dim = len(x[0])
        self.latent_neurons = latent_space_size
        self.intermediate_layers = qty_nodes_in_hidden_layers
        self.epochs = epochs
        self.set_vae()

    def train(self, training_set, batch_size):
        print(training_set.shape)
        self.model.fit(training_set, training_set, epochs=self.epochs,
                       batch_size=batch_size,
                       validation_data=(training_set, training_set))

    def set_vae(self):
        x = Input(shape=(self.dim,), name="input")
        self.encoder = self._set_encoder(x)
        self.encoder.summary()
        self.decoder = self._set_decoder()
        self.decoder.summary()
        output_combined = self.decoder(self.encoder(x)[2])
        self.model = Model(x, output_combined)
        self.model.summary()
        self.model.compile(loss=self._vae_loss)

    def _set_encoder(self, x):
        h = None
        if (len(self.intermediate_layers) != 0):
            aux_h = x
            for (i, neurons) in enumerate(self.intermediate_layers[:-1]):
                h = Dense(neurons, name="encoding_{0}".format(i))(aux_h)
                aux_h = h
            h = Dense(self.intermediate_layers[-1], activation="relu",
                      name="encoding_{0}".format(len(self.intermediate_layers) - 1))(aux_h)
        self.z_mean = Dense(self.latent_neurons, name="mean")(h)
        self.z_log_var = Dense(self.latent_neurons, name="log-variance")(h)
        z = Lambda(self._get_samples, output_shape=(self.latent_neurons,))([self.z_mean, self.z_log_var])
        return Model(x, [self.z_mean, self.z_log_var, z], name="encoder")

    def _set_decoder(self):
        input_decoder = Input(shape=(self.latent_neurons,), name="decoder_input")
        reversed_layers = self.intermediate_layers.copy()
        reversed_layers.reverse()
        h = None
        if (len(self.intermediate_layers) != 0):
            aux_h = input_decoder
            for (i, neurons) in enumerate(reversed_layers[:-1]):
                h = Dense(neurons, name="encoding_{0}".format(i))(aux_h)
                aux_h = h
            h = Dense(reversed_layers[-1], activation="relu",
                      name="encoding_{0}".format(len(self.intermediate_layers) - 1))(aux_h)
        x_decoded = Dense(self.dim, activation='sigmoid', name="flat_decoded")(h)
        decoder = Model(input_decoder, x_decoded, name="decoder")
        return decoder

    def _get_samples(self, args):
        z_mean, z_log_var = args
        epsilon = K.random_normal(shape=(K.shape(z_mean)[0], self.latent_neurons), mean=0., stddev=1.0)
        return z_mean + K.exp(z_log_var / 2) * epsilon 

    def _vae_loss(self, x, x_decoded_mean):
        xent_loss = self.dim * metrics.binary_crossentropy(x, x_decoded_mean) 
        kl_loss = - 0.5 * K.sum(1 + self.z_log_var - K.square(self.z_mean) - K.exp(self.z_log_var), axis=-1)
        _vae_loss = K.mean(xent_loss + kl_loss)
        return _vae_loss