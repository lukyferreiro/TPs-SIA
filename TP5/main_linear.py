import json
from src.utils import DataConfig
from src.perceptron import MultilayerPerceptron

#TODO: valores de input_data_len, tamaño espacio latente, pasados por parámetro para hacer encoder y decoder. Cambiar a recibir por json
# Ver si puede generarse una estructura autoencoder así se entrena todo junto
# Modificar método de entrenamiento para que no haga de a epochs ciclos sino 1 solo
# De esta forma se podrá actualizar el autoencoder completo

def main(): 
    with open('./config.json', 'r') as f:
        data_config = json.load(f)

    config = DataConfig(data_config)

    encoder = MultilayerPerceptron(config.input_data, 35, 2, config.learning_rate, config.bias,
                                            config.epochs, config.training_percentage, config.min_error,
                                            config.qty_hidden_layers, config.qty_nodes_in_hidden_layers, 
                                            config.output_activation, config.hidden_activation, config.beta,
                                            config.optimizer_method, config.alpha, config.beta1, config.beta2,
                                            config.epsilon)
    
    decoder = MultilayerPerceptron(config.input_data, 2, 35, config.learning_rate, config.bias,
                                            config.epochs, config.training_percentage, config.min_error,
                                            config.qty_hidden_layers, config.qty_nodes_in_hidden_layers[::-1], 
                                            config.output_activation, config.hidden_activation, config.beta,
                                            config.optimizer_method, config.alpha, config.beta1, config.beta2,
                                            config.epsilon)

    print(encoder)
    print(decoder)


if __name__ == "__main__":
    main()