from src.parser_files import get_csv_data
from src.utils import standarize_data
from src.plots import *

def main(): 
    data, countries, labels = get_csv_data("data/europe.csv")
    data_standarized = standarize_data(data)

    #plot_boxplot(data, "Boxplot con datos no estandarizados", labels)
    #plot_boxplot(data_standarized, "Boxplot con datos estandarizados", labels)
    plot_biplot(data, data_standarized, countries, labels)
    plot_biplot2(data, data_standarized, countries, labels)
    #plot_biplot3(data_standarized, countries, labels)

if __name__ == "__main__":
    main()