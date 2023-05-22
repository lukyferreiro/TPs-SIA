import json
from src.utils import DataConfig, standarize_data
from src.parser_files import get_csv_data
from src.networks.Kohonen import Kohonen
from src.plots import *

def main(): 
    with open('./config.json', 'r') as f:
        data_config = json.load(f)

    config = DataConfig(data_config)
    data, countries, labels = get_csv_data("data/europe.csv")
    data_standarized = standarize_data(data)

    kohonen = Kohonen(data_standarized, config.k, config.learning_rate,
                      config.radius, config.epochs, config.likeness)
    kohonen.train()

    plot_heatmap(data_standarized, countries, kohonen, config.k, config.learning_rate, config.radius)
    plot_matrix_u(kohonen, config.k)
    for i, label in enumerate(labels): 
       plot_heatmap_single_variable(i, config.k, data_standarized, kohonen, f"Valores de {label} para cada neurona")

if __name__ == "__main__":
    main()