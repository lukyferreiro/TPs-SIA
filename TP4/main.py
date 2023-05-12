import json
from src.utils import DataConfig
from src.parser_files import get_csv_data
from src.Kohonen import Kohonen
from src.plots import *

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)

    config = DataConfig(data)
    data, data_standarized, countries, labels = get_csv_data("europe.csv")

    print(data)
    print("---------------ACA--------------------")
    print(data_standarized)
    print("---------------------------------------")
    print(countries)
    print("---------------------------------------")
    print(labels)

    k = config.k
    

    kohonen = Kohonen(data_standarized, config.k, config.learning_rate,
                      config.radius, config.epochs, config.similitud)
    kohonen.train()

    plot_boxplot(data, "Box plot not standarized", labels)
    plot_boxplot(data_standarized, "Box plot standarized", labels)
    plot_heatmap(data_standarized, countries, kohonen, config.k, config.learning_rate, config.radius)
    for i, label in enumerate(labels): 
        plot_single_variable(i, config.k, data_standarized, kohonen, f"{label} values for each group")

if __name__ == "__main__":
    main()