import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

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

    plt.title(f"Heatmap with η={str(learn_rate)} and radius={str(radius)}")
    sn.heatmap(matrix, cmap='Reds', annot=countries_matrix, fmt="")
    plt.show()

def plot_single_variable(var, k, data_standarized, countries, solver, descr):
    matrix = np.zeros((k, k))
    countries_matrix_aux = [["" for _ in range(k)] for _ in range(k)]
    for k in range(len(data_standarized)):
        i,j = solver.find_winner_neuron(data_standarized[k])
        matrix[i][j] += data_standarized[k][var]
        countries_matrix_aux[i][j] += f"{countries[i]}\n"   #TODO check esto

    countries_matrix = np.array(countries_matrix_aux)
    plt.suptitle(descr)
    sn.heatmap(matrix, cmap='Blues', annot=countries_matrix)
    plt.show()

def plot_biplot(data, data_standarized, countries, labels):
    # 3. Calcular la matriz de correlaciones Sx
    Sx = np.corrcoef(data_standarized, rowvar=False)

    # 4. Calcular autovalores y autovectores de la matriz de covarianzas
    eigenvalues, eigenvectors = np.linalg.eig(Sx)

    print(eigenvalues)
    print(eigenvectors)

    # 5. Ordenar los autovalores de mayor a menor
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues_sorted = eigenvalues[idx]
    eigenvectors_sorted = eigenvectors[:, idx]

    # 6. Construir la matriz R tomando los autovectores correspondientes a los mayores autovalores
    k = 2  # Número de componentes principales deseados
    R = eigenvectors_sorted[:, :k]

    # 7. Calcular las nuevas variables Y como combinación lineal de las originales
    Y = np.dot(data_standarized, R)

    fig, ax = plt.subplots()
    ax.scatter(Y[:, 0], Y[:, 1])

    for i in range(len(data[0])):
        ax.arrow(0, 0, R[i, 0], R[i, 1], head_width=0.05, head_length=0.05, fc='red', ec='red')
        ax.text(R[i, 0]*1.2, R[i, 1]*1.2, f'{labels[i]}', color='red')

    for i in range(len(Y)):
        ax.text(Y[i, 0]*1, Y[i, 1]*1, f'{countries[i]}', color='blue')

    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(0, color='black', linestyle='--')
    ax.set_xlabel('Componente Principal 1')
    ax.set_ylabel('Componente Principal 2')
    ax.set_title('Biplot')

    '''
    zoom_factor = 0.34
    x_center = Y[:, 0].mean() 
    y_center = Y[:, 1].mean() 
    x_range = Y[:, 0].max() - Y[:, 0].min()  
    y_range = Y[:, 1].max() - Y[:, 1].min()  

    ax.set_xlim(x_center - zoom_factor * x_range, x_center + zoom_factor * x_range)
    ax.set_ylim(y_center - zoom_factor * y_range, y_center + zoom_factor * y_range)
    '''
    
    print("Autovalores:", eigenvalues_sorted)
    print("Autovectores:\n", eigenvectors_sorted)
    print("Matriz R:\n", R)
    print("Nuevas variables Y:\n", Y)

    plt.show()