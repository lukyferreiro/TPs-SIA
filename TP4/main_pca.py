from src.parser_files import get_csv_data
from src.utils import standarize_data
from src.plots import *

def main(): 
    # 1. Tomar un conjunto de datos X y poner las variables en columnas.
    data, countries, labels = get_csv_data("europe.csv")
    # 2. Estandarizar las variables X
    data_standarized = standarize_data(data)

    plot_biplot(data, data_standarized, countries, labels)

    #plot_boxplot(data, "Box plot not standarized", labels)
    plot_boxplot(data_standarized, "Box plot standarized", labels)

if __name__ == "__main__":
    main()