from src.parser_files import get_csv_data
from src.utils import standarize_data
from src.plots import *
from sklearn.decomposition import PCA
import pandas as pd

def main(): 
    data, countries, labels = get_csv_data("data/europe.csv")
    data_standarized = standarize_data(data)

    plot_boxplot(data, "Boxplot con datos no estandarizados", labels)
    plot_boxplot(data_standarized, "Boxplot con datos estandarizados", labels)

    pca = PCA()
    principal_components = pca.fit_transform(data_standarized)
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

    plot_variance(pca)
    plot_biplot(pca, principal_components, loadings, countries, labels)

    print("Eigenvector - First Component")
    print(pca.components_.T[:, 0])
    print("PCA 1")
    print(principal_components[:, 0])

    plot_pca(principal_components[:, 0], countries, "PCA1 por pais")

if __name__ == "__main__":
    main()