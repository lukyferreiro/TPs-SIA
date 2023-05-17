import json
from src.utils import DataConfig, standarize_data
from src.parser_files import get_csv_data
from src.Kohonen import Kohonen
from src.plots import *

def main(): 
    with open('./config.json', 'r') as f:
        data_config = json.load(f)

    config = DataConfig(data_config)
    data, countries, labels = get_csv_data("europe.csv")
    data_standarized = standarize_data(data)

    print(data)
    print("---------------ACA--------------------")
    print(data_standarized)
    print("---------------------------------------")
    print(countries)
    print("---------------------------------------")
    print(labels)

    kohonen = Kohonen(data_standarized, config.k, config.learning_rate,
                      config.radius, config.epochs, config.likeness)
    kohonen.train()

    #plot_boxplot(data, "Boxplot con datos no estandarizados", labels)
    #plot_boxplot(data_standarized, "Boxplot con datos estandarizados", labels)
    #plot_heatmap(data_standarized, countries, kohonen, config.k, config.learning_rate, config.radius)

    for i, label in enumerate(labels): 
       plot_heatmap_single_variable(i, config.k, data_standarized, countries, kohonen, f"{label} values for each group")

if __name__ == "__main__":
    main()