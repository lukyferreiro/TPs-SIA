import json
from src.utils import DataConfig
from src.utils import extract_patterns
from src.autoencoder import Autoencoder
from src.plots import *
from data.font import _font_num

def main(): 
    with open('./config.json', 'r') as f:
        data_config = json.load(f)

    c = DataConfig(data_config)

    print(c.input_data)

    plot_letters(c.input_data, "ASDASDAS")

    new_patterns = extract_patterns(_font_num)
    plot_letters(new_patterns, "Numeros")

    autoencoder = Autoencoder(c.input_data, len(c.input_data[0]), c.latent_space_size,
                              c.learning_rate, c.bias, c.epochs, c.training_percentage,
                              c.min_error, c.qty_hidden_layers, c.qty_nodes_in_hidden_layers, 
                              c.output_activation, c.hidden_activation, c.beta,
                              c.optimizer_method, c.alpha, c.beta1, c.beta2,
                              c.epsilon)
  
    autoencoder.train()

    numbers = []
    for num in new_patterns:
        predicted = autoencoder.predict(num)
        numbers.append(predicted)
    
    print(numbers)
    plot_letters(numbers, "Numeros predicted")

    predicted = autoencoder.predict(c.input_data[7])
    predicted = predicted.reshape((1, len(predicted)))
    print(predicted)
    plot_letters(predicted, "G")

    predicted = autoencoder.predict(c.input_data[8])
    predicted = predicted.reshape((1, len(predicted)))
    print(predicted)
    plot_letters(predicted, "H")

    list = []
    for i in range(len(c.input_data)):
        value = autoencoder.latent_space(c.input_data[i])
        list.append(value)
        print("Latent space value: ", value, " for letter in index ", i)

    plot_latent_space(np.array(list))

    
if __name__ == "__main__":
    main()