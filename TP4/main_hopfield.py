import json
from src.utils import DataConfig, mutate, calculate_ortogonality
from src.parser_files import get_letters
from src.networks.Hopfield import Hopfield
import numpy as np
from src.plots import *

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)

    config = DataConfig(data)
    letters = get_letters("data/letters.txt")

    plot_letters(letters, "Patrones")

    COUNT_LETTERS = 4
    letters_to_train = []
    idxs = np.random.choice(len(letters), size=COUNT_LETTERS, replace=False)
    for idx in idxs:
        letters_to_train.append(letters[idx])
    letters_to_train = np.array(letters_to_train)
    orto_value = calculate_ortogonality(letters_to_train)
    plot_letters(letters_to_train, f"Patrones almacenados con ortogonalidad {orto_value}")

    hopfield = Hopfield(letters_to_train, config.epochs)

    random_idx = np.random.randint(len(letters_to_train))
    letter_to_mutate = letters_to_train[random_idx]
    plot_letters(letter_to_mutate.reshape((1, len(letter_to_mutate))), "Patron a mutar")

    letter_mutated = mutate(letter_to_mutate, config.mutate_prob)
    arr_patterns, arr_energy = hopfield.predict(letter_mutated)

    print("-------------------------")
    print(arr_patterns)
    print(arr_energy)
    plot_letters(arr_patterns, "Prediccion de Hopfield")
    plot_energy(arr_energy)

if __name__ == "__main__":
    main()