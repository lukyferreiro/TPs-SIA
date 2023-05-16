import pandas as pd
import numpy as np

def get_csv_data(file_path):
    csv = pd.read_csv(file_path)
    countries = csv.values[:, 0]
    labels = list(csv.columns)[1:]
    csv.set_index('Country', drop=True, inplace=True)
    data = csv.values
    return data, countries, labels

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