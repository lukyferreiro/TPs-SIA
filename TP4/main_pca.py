from src.parser_files import get_csv_data
from src.utils import standarize_data
from src.plots import *

def main(): 
    data, countries, labels = get_csv_data("europe.csv")
    data_standarized = standarize_data(data)

    #plot_boxplot(data, "Box plot not standarized", labels)
    #plot_boxplot(data_standarized, "Box plot standarized", labels)
    #plot_biplot(data, data_standarized, countries, labels)
    plot_biplot2(data_standarized, countries, labels)

if __name__ == "__main__":
    main()