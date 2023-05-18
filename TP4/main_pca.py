from src.parser_files import get_csv_data
from src.utils import standarize_data
from src.plots import *

def main(): 
    data, countries, labels = get_csv_data("data/europe.csv")
    data_standarized = standarize_data(data)

    #plot_boxplot(data, "Boxplot con datos no estandarizados", labels)
    #plot_boxplot(data_standarized, "Boxplot con datos estandarizados", labels)
    #plot_biplot(data, data_standarized, countries, labels)

    pca = PCA()
    principal_components = pca.fit_transform(data_standarized)
    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

    plot_biplot2(pca, principal_components, loadings, countries, labels)
    #plot_biplot3(pca, principal_components, loadings, countries, labels)

    print("Eigenvector - First Component")
    print(pca.components_.T[:, 0])
    print("PCA 1")
    print(principal_components[:, 0])

    plot_pca(pca.components_[0], labels, "1ra componente con libreria sklearn")

if __name__ == "__main__":
    main()