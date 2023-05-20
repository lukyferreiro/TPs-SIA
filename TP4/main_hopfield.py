import json
from src.utils import DataConfig, mutate
from src.parser_files import get_letters
from src.networks.Hopfield import Hopfield
import numpy as np
from src.plots import *

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)

    config = DataConfig(data)
    letters = get_letters("data/letters.txt")

    plot_letters(letters)

    COUNT_LETTERS = 4
    letters_to_train = []
    for _ in range(COUNT_LETTERS):
        random_idx = np.random.randint(len(letters))
        letters_to_train.append(letters[random_idx])
    letters_to_train = np.array(list(letters_to_train))

    plot_letters(letters_to_train)

    hopfield = Hopfield(letters_to_train, config.epochs)

    random_letter_to_mutate = np.random.randint(len(letters_to_train))
    letter_mutated = mutate(letters_to_train[random_letter_to_mutate], config.mutate_prob)
    
    #letter_mutated_reshaped = letter_mutated.reshape((1, len(letter_mutated)))
    #print(letter_mutated_reshaped)
    #plot_letters(letter_mutated_reshaped)

    arr_patterns, arr_energy = hopfield.train(letter_mutated)

    print("-------------------------")
    print(arr_patterns)
    print(arr_energy)
    plot_letters(arr_patterns)

if __name__ == "__main__":
    main()