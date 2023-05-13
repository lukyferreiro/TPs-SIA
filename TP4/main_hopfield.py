import json
from src.utils import DataConfig
from src.parser_files import get_letters
from src.Hopfield import Hopfield

def main(): 
    with open('./config.json', 'r') as f:
        data = json.load(f)

    config = DataConfig(data)
    letters = get_letters("letters.txt")

    print(len(letters))
    print(letters)

    # TODO Elegir aleatoriamente 4 letras de letters_matrix y enviarlas
    # como patrones almacenados a Hopfield
    # Luego en train entrenar con solo uno de los elegidos 

    hopfield = Hopfield(letters, config.epochs)
    hopfield.train(letters[1])

if __name__ == "__main__":
    main()