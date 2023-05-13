from statistics import mean, stdev
import copy
import pandas as pd
import numpy as np

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

def get_letters(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        
    letters = []
    for i in range(26):
        letter = []
        for j in range(5):
            current_line = list(map(lambda v: int(v), lines[j + i * 5].split()))
            for n in current_line:
                letter.append(n)
        letters.append(letter)

    letters = np.array(letters)
    letters = np.where(letters == 0, -1, letters)

    return letters