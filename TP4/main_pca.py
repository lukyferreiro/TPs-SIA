import json
from src.utils import DataConfig
from src.parser_files import get_csv_data
from src.Kohonen import Kohonen
from src.plots import *

def main(): 
    # 1. Tomar un conjunto de datos X y poner las variables en columnas.
    # 2. Estandarizar las variables X
    data, data_standarized, countries, labels = get_csv_data("europe.csv")

    plot_biplot(data, data_standarized, countries, labels)

    #plot_boxplot(data, "Box plot not standarized", labels)
    plot_boxplot(data_standarized, "Box plot standarized", labels)

if __name__ == "__main__":
    main()