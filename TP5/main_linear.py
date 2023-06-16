import json
from src.utils import DataConfig
from src.autoencoder import Autoencoder
import numpy as np
import matplotlib.pyplot as plt

#TODO: valores de input_data_len, tamaño espacio latente, pasados por parámetro para hacer encoder y decoder. Cambiar a recibir por json
# Ver si puede generarse una estructura autoencoder así se entrena todo junto
# Modificar método de entrenamiento para que no haga de a epochs ciclos sino 1 solo
# De esta forma se podrá actualizar el autoencoder completo

def main(): 
    with open('./config.json', 'r') as f:
        data_config = json.load(f)

    c = DataConfig(data_config)

    autoencoder = Autoencoder(c.input_data, len(c.input_data[0]), c.latent_space_size,
                              c.learning_rate, c.bias, c.epochs, c.training_percentage,
                              c.min_error, c.qty_hidden_layers, c.qty_nodes_in_hidden_layers, 
                              c.output_activation, c.hidden_activation, c.beta,
                              c.optimizer_method, c.alpha, c.beta1, c.beta2,
                              c.epsilon)
  
    
    autoencoder.train()

    """
    predicted = autoencoder.predict(c.input_data[10])
    print(predicted)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    create_letter_plot(predicted, ax)
    plt.show()
    """

"""
def create_letter_plot(letter, ax):
    array = np.array(letter).reshape((7, 5))  # Cambia la forma del arreglo a una matriz de 5x7
    cmap = plt.cm.get_cmap('binary')  # Utiliza la escala de colores 'binary' para blanco y negro

    ax.imshow(array, cmap=cmap, vmin=0, vmax=1)

    # Dibujar líneas adicionales en cada celda
    for i in range(8):
        ax.plot([-0.5, 4.5], [i-0.5, i-0.5], color='black', linewidth=2)
    for i in range(6):
        ax.plot([i-0.5, i-0.5], [-0.5, 6.5], color='black', linewidth=2)

    # Colorear celdas según el valor del arreglo
    for i in range(7):
        for j in range(5):
            if array[i, j] > 0.5: # Si el valor es cercano a 1, colorear la celda de negro
                ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, linewidth=2, edgecolor='black', facecolor='black'))
            else:  # Si el valor es cercano a 0, dejar la celda en blanco
                ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, linewidth=2, edgecolor='black', facecolor='white'))

    ax.axis('off')
"""

if __name__ == "__main__":
    main()