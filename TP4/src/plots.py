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

    result_to_country = {}
    for i in range(len(results)):
        if results[i] not in result_to_country.keys():
            result_to_country.update({results[i]: []})
        result_to_country[results[i]].append(countries[i])
        matrix[results[i]] += 1

    plt.title(f"Heatmap with η={str(learn_rate)} and radius={str(radius)}")
    sn.heatmap(matrix, cmap='YlGnBu', annot=True)
    print(result_to_country)
    plt.show()

def plot_single_variable(var, k, data_standarized, solver, descr):
    matrix = np.zeros((k, k))
    for k in range(len(data_standarized)):
        i,j = solver.find_winner_neuron(data_standarized[k])
        matrix[i][j] += data_standarized[k][var]
    plt.suptitle(descr)
    sn.heatmap(matrix, cmap='YlGnBu', annot=True)
    plt.show()
