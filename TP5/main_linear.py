import json
from src.utils import DataConfig, extract_patterns
from src.autoencoder import Autoencoder
from src.plots import *
from data.font import _font_3, symbols3, _font_num, symbols_num

def main(): 
    with open('./config_linear.json', 'r') as f:
        data_config = json.load(f)

    c = DataConfig(data_config, _font_3)

    print(c.input_data)

    plot_letters(c.input_data, "Conjunto de entrenamiento")

    autoencoder = Autoencoder(c.input_data, c.input_data, c.latent_space_size,
                              c.learning_rate, c.bias, c.epochs, c.training_percentage,
                              c.min_error, c.qty_hidden_layers, c.qty_nodes_in_hidden_layers, 
                              c.output_activation, c.hidden_activation, c.beta,
                              c.optimizer_method, c.alpha, c.beta1, c.beta2,
                              c.epsilon)
    autoencoder.train()

    predicted = []
    for x in c.input_data:
        p = autoencoder.predict(x)
        predicted.append(p)
    plot_letters(predicted, "Predicted")
    
    list = []
    for i in range(len(c.input_data)):
        value = autoencoder.latent_space(c.input_data[i])
        list.append(value)
        print("Latent space value: ", value, " for letter in index ", i)
    plot_latent_space(np.array(list), symbols3)

    predicted_num = []
    numbers = extract_patterns(_font_num)
    for x in numbers:
        p = autoencoder.predict(x)
        predicted_num.append(p)
    plot_letters(predicted_num, "Predicted")
    
    list = []
    for i in range(len(numbers)):
        value = autoencoder.latent_space(numbers[i])
        list.append(value)
        print("Latent space value: ", value, " for letter in index ", i)
    plot_latent_space(np.array(list), symbols_num)

    
if __name__ == "__main__":
    main()