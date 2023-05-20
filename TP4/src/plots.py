import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import math

def plot_boxplot(data, box_plot_title, labels):
    data_arr = np.array(data)
    fig, ax = plt.subplots(figsize=(10, 7))
    x = np.array(labels)
    ax.set_xticklabels(x)
    plt.title(box_plot_title)
    ax.boxplot([data_arr[:, 0], data_arr[:, 1], data_arr[:, 2], data_arr[:, 3], data_arr[:, 4], data_arr[:, 5], data_arr[:, 6]], 
               widths=0.5, 
               boxprops=dict(color='black'),
               whiskerprops=dict(color='black'),
               medianprops=dict(color='red', linewidth=2))
    plt.show()
    
def plot_heatmap(inputs, countries, solver, k, learn_rate, radius):
    results = [solver.find_winner_neuron(i) for i in inputs]
    matrix = np.zeros((k, k))
    countries_matrix_aux = [["" for _ in range(k)] for _ in range(k)]

    for i in range(len(results)):
        matrix[results[i]] += 1
        countries_matrix_aux[results[i][0]][results[i][1]] += f"{countries[i]}\n"

    countries_matrix = np.array(countries_matrix_aux)

    plt.title(f"Heatmap {k}x{k} con η={str(learn_rate)} y radio={str(radius)}")
    sn.heatmap(matrix, cmap='Reds', annot=countries_matrix, fmt="")
    plt.show()

def plot_heatmap_single_variable(var, k, data_standarized, countries, solver, descr):
    matrix = np.zeros((k, k))
    countries_matrix_aux = [["" for _ in range(k)] for _ in range(k)]

    for k in range(len(data_standarized)):
        i,j = solver.find_winner_neuron(data_standarized[k])
        matrix[i][j] += data_standarized[k][var]
        countries_matrix_aux[i][j] += f"{countries[k]}\n" 

    countries_matrix = np.array(countries_matrix_aux)

    plt.suptitle(descr)
    sn.heatmap(matrix, cmap='Blues', annot=countries_matrix, fmt="")
    plt.show()

#TODO hacer la matriz U
def plot_matrix_u():
    pass


def plot_biplot(pca, principal_components, loadings, countries, labels):
    fig, ax = plt.subplots()
    ax.scatter(principal_components[:, 0], principal_components[:, 1])
    
    for i in range(len(principal_components[0])):
        ax.arrow(0, 0, loadings[i, 0], loadings[i, 1], head_width=0.05, head_length=0.05, fc='red', ec='red')
        ax.text(loadings[i, 0]*1.2, loadings[i, 1]*1.2, f'{labels[i]}', color='red')

    for i in range(len(principal_components)):
        ax.text(principal_components[i, 0], principal_components[i, 1], f'{countries[i]}', color='blue')
    

    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    ax.set_xlabel(f'PCA 1 ({pca.explained_variance_ratio_[0] * 100:.2f}% varianza)')
    ax.set_ylabel(f'PCA 2 ({pca.explained_variance_ratio_[1] * 100:.2f}% varianza)')
    ax.set_title('Biplot con valores de componentes principales 1 y 2')

    '''
    zoom_factor = 0.34
    x_center = principal_components[:, 0].mean() 
    y_center = principal_components[:, 1].mean() 
    x_range = principal_components[:, 0].max() - principal_components[:, 0].min()  
    y_range = principal_components[:, 1].max() - principal_components[:, 1].min()  

    ax.set_xlim(x_center - zoom_factor * x_range, x_center + zoom_factor * x_range)
    ax.set_ylim(y_center - zoom_factor * y_range, y_center + zoom_factor * y_range)
    '''
    plt.show()

def plot_pca(vec, labels, descr):
    x = list(labels)
    y = list(vec)
    plt.rc('font', size=10)

    fig, ax = plt.subplots(figsize=(10, 8))
    width = 0.5
    ind = np.arange(len(y))  

    cc = ['colors'] * len(y)
    for n, val in enumerate(y):
        if val < 0:
            cc[n] = 'red'
        elif val >= 0:
            cc[n] = 'blue'

    ax.bar(ind, y, width, color=cc)
    ax.set_xticks(ind + width / 100)
    ax.set_xticklabels(x, minor=False)
    plt.xticks(rotation=90)
    ax.set_ylabel('PCA1')
    ax.set_xlabel('Paises')
    plt.title(descr)
    plt.show()

def plot_variance(pca):
    variance_ratio = pca.explained_variance_ratio_
    variance_cumulative = np.cumsum(variance_ratio)
    print("Varianza de cada componente principal")
    print(variance_ratio)
    print("Varianza acumulada")
    print(variance_cumulative)

    pca_labels = [f'PCA{i+1}' for i in range(len(variance_ratio))]
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # Gráfico de barras para la varianza
    ax1.bar(pca_labels, variance_ratio, color='blue', alpha=0.5)
    ax1.set_ylabel('Varianza')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Gráfico de línea para la varianza acumulada
    ax2.plot(pca_labels, variance_cumulative, color='red')
    ax2.set_ylabel('Varianza Acumulada')
    ax2.tick_params(axis='y', labelcolor='red')

    plt.title('Varianza y Varianza Acumulada para Componentes PCA')
    plt.xticks(rotation=45)
    plt.subplots_adjust(right=0.8)
    plt.show()


def plot_letters(letters):
    num_letters = len(letters)
    num_rows = math.ceil(math.sqrt(num_letters))
    num_cols = math.ceil(num_letters / num_rows)
    
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 10))
    fig.subplots_adjust(hspace=0.3)

    # Envolver en una matriz adicional para mantener la consistencia si solo es una letra
    if num_letters == 1:
        axs = np.array([[axs]])  
    elif num_letters == 2:
        axs = axs[np.newaxis, :] if num_rows == 1 else axs[:, np.newaxis]
    
    for i, letter in enumerate(letters):
        row = i // num_cols
        col = i % num_cols
        ax = axs[row, col]
        create_letter_plot(letter, ax)
    
    # Eliminar ejes innecesarios
    for ax in axs.flat[num_letters:]:
        ax.remove()

    plt.show()

def create_letter_plot(letter, ax):
    array = np.array(letter).reshape((5, 5))
    cmap = plt.cm.get_cmap('Blues')
    cmap.set_under(color='white')

    ax.imshow(array, cmap=cmap, vmin=-1, vmax=1)

    # Dibujar líneas adicionales en cada celda
    for i in range(6):
        ax.plot([-0.5, 4.5], [i-0.5, i-0.5], color='black', linewidth=2)
        ax.plot([i-0.5, i-0.5], [-0.5, 4.5], color='black', linewidth=2)

    for i in range(5):
        for j in range(5):
            if array[i, j] == 1:
                ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, linewidth=2, edgecolor='black', facecolor='none'))

    ax.axis('off')