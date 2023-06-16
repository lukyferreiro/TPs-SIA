import json
from src.utils import DataConfig
from src.autoencoder import Autoencoder

def main(): 
    with open('./config.json', 'r') as f:
        data_config = json.load(f)

    c = DataConfig(data_config)

    autoencoder = Autoencoder(c.input_data, len(c.input_data[0]), c.latent_space_size,
                            c.learning_rate, c.bias, c.epochs, c.training_percentage,
                            c.min_error, c.qty_hidden_layers, c.qty_nodes_in_hidden_layers, 
                            c.output_activation, c.hidden_activation, c.beta,
                            c.optimizer_method, c.alpha, c.beta1, c.beta2,
                            c.epsilon)
  
    autoencoder.train()


if __name__ == "__main__":
    main()