from statistics import mean, stdev
import copy
import pandas as pd

def get_csv_data(file_path):
    data = pd.read_csv(file_path)
    countries = data.values[:, 0]
    labels = ['Area', 'GDP', 'Inflation', 'Life.expect', 'Military', 'Pop.growth', 'Unemployment']

    data.set_index('Country', drop=True, inplace=True)
    data = data.values

    # Estandarizamos los datos usando la media y el desvio estandar
    data_standarized = copy.deepcopy(data)
    for i in range(len(data[0])):
        aux = data_standarized[:, i]
        mean_aux = mean(aux)
        stdev_aux = stdev(aux)
        data_standarized[:, i] = (data_standarized[:, i] - mean_aux) / stdev_aux

    return data, data_standarized, countries, labels