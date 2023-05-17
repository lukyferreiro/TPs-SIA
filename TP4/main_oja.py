import json
from src.utils import DataConfig, standarize_data
from src.parser_files import get_csv_data
from src.networks.Oja import Oja
from src.plots import *
from sklearn.decomposition import PCA

def main(): 
    with open('./config.json', 'r') as f:
        data_config = json.load(f)

    config = DataConfig(data_config)
    data, countries, labels = get_csv_data("data/europe.csv")
    data_standarized = standarize_data(data)

    oja = Oja(data_standarized, config.learning_rate, config.epochs)
    weights = oja.train()

    print("Approximated Eigenvector - First Component")
    print(weights)
    print("Approximated PCA 1")
    pca = np.matmul(data_standarized, weights)
    print(pca)
    print(countries)

    plot_pca(weights, labels, "1ra componente con Oja")

    pca = PCA()
    principal_components = pca.fit_transform(data_standarized)

    print("Eigenvector - First Component")
    print(pca.components_.T[:, 0])
    print("PCA 1")
    print(principal_components[:, 0])

    plot_pca(pca.components_[0], labels, "1ra componente con libreria sklearn")

    error = 0
    for i in range(len(weights)):
        error = np.abs(weights[i] - principal_components[0][i])
    print(error)


if __name__ == "__main__":
    main()