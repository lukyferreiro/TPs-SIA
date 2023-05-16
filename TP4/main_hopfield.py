import json
from src.utils import DataConfig, mutate
from src.parser_files import get_letters
from src.Hopfield import Hopfield
import numpy as np

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)

    config = DataConfig(data)
    letters = get_letters("letters.txt")

    print(len(letters))
    print(letters)

    COUNT_LETTERS = 4
    letters_to_train = []
    for _ in range(COUNT_LETTERS):
        random_idx = np.random.randint(len(letters))
        letters_to_train.append(letters[random_idx])
    letters_to_train = np.array(list(letters_to_train))

    hopfield = Hopfield(letters_to_train, config.epochs)

    random_letter_to_mutate = np.random.randint(len(letters_to_train))
    letter_mutated = mutate(letters_to_train[random_letter_to_mutate], config.mutate_prob)
    
    arr_patterns, arr_energy = hopfield.train(letter_mutated)

    print(arr_energy)

if __name__ == "__main__":
    main()