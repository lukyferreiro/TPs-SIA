import json
import copy
from src.utils import DataConfig, alter_data
from src.autoencoder import Autoencoder
from src.plots import *
from data.font import _font_num, symbols_num    

def main(): 
    with open('./config_denoising.json', 'r') as f:
        data_config = json.load(f)

    c = DataConfig(data_config, _font_num)
    plot_letters(c.input_data, "Conjunto de entrenamiento")

    autoencoder = Autoencoder(c.input_data, len(c.input_data[0]), c.latent_space_size,
                            c.learning_rate, c.bias, c.epochs, c.training_percentage,
                            c.min_error, c.qty_hidden_layers, c.qty_nodes_in_hidden_layers, 
                            c.output_activation, c.hidden_activation, c.beta,
                            c.optimizer_method, c.alpha, c.beta1, c.beta2,
                            c.epsilon)
    autoencoder.train()

    # Análisis de dataset original
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
    plot_latent_space(np.array(list), symbols_num)


    # Análisis de dataset mutado
    for i in [round(0.1*i,2) for i in range(1,6)]:
        print(f"----------------Mutacion={i}----------------")
        original_input = copy.deepcopy(c.input_data)
        alter_data(original_input, i)
        plot_letters(original_input, "Mutated dataset")

        predicted = []
        for x in original_input:
            p = autoencoder.predict(x)
            predicted.append(p)
        plot_letters(predicted, "Predicted")
        
        list = []
        for i in range(len(original_input)):
            value = autoencoder.latent_space(original_input[i])
            list.append(value)
            print("Latent space value: ", value, " for letter in index ", i)
        plot_latent_space(np.array(list), symbols_num)
    


if __name__ == "__main__":
    main()