import numpy as np
import matplotlib.pyplot as plt
import math
from data.font import symbols3

def plot_letters(letters, desc):
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

    fig.suptitle(desc, fontsize=20, fontweight="bold")
    plt.show()

def create_letter_plot(letter, ax):
    array = np.array(letter).reshape((7, 5))
    cmap = plt.cm.get_cmap('Blues')
    cmap.set_under(color='white')

    ax.imshow(array, cmap=cmap, vmin=-1, vmax=1)

    # Dibujar líneas adicionales en cada celda
    for i in range(6):
        ax.plot([-0.5, 4.5], [i-0.5, i-0.5], color='black', linewidth=2)
        ax.plot([i-0.5, i-0.5], [-0.5, 4.5], color='black', linewidth=2)

    for i in range(7):
        for j in range(5):
            if array[i, j] > 0.5: # Si el valor es cercano a 1, colorear la celda de negro
                ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, linewidth=2, edgecolor='black', facecolor='black'))
            else:  # Si el valor es cercano a 0, dejar la celda en blanco
                ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, linewidth=2, edgecolor='black', facecolor='white'))

    ax.axis('off')

def plot_latent_space(latent_space):
    fig, ax = plt.subplots()

    ax.set_title("Espacio latente")
    ax.set_ylim((0, 1.1))
    ax.set_xlim((0, 1.1))

    for i in range(len(latent_space[:, 0])):
        ax.annotate(symbols3[i], (latent_space[i][0], latent_space[i][1]))

    ax.scatter(latent_space[:, 0], latent_space[:, 1])

    plt.show()
