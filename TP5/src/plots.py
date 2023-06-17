import numpy as np
import matplotlib.pyplot as plt
import math

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

import numpy as np
import matplotlib.pyplot as plt

def create_letter_plot(letter, ax):
    array = np.array(letter).reshape((7, 5))
    cmap = plt.cm.get_cmap('Greys')
    cmap.set_under(color='white')

    ax.imshow(array, cmap=cmap, vmin=0, vmax=1)

    # Dibujar líneas adicionales en cada celda
    for i in range(6):
        ax.plot([-0.5, 4.5], [i-0.5, i-0.5], color='black', linewidth=2)
        ax.plot([i-0.5, i-0.5], [-0.5, 4.5], color='black', linewidth=2)

    for i in range(7):
        for j in range(5):
            value = array[i, j]
            color = str(1 - value)  # Convertir el valor en escala de gris (1 - valor)
            ax.add_patch(plt.Rectangle((j-0.5, i-0.5), 1, 1, linewidth=2, edgecolor='black', facecolor=color))

    ax.axis('off')


def plot_latent_space(latent_space, symbols):
    fig, ax = plt.subplots()

    ax.set_title("Espacio latente")

    for i in range(len(latent_space[:, 0])):
        ax.annotate(symbols[i], (latent_space[i][0], latent_space[i][1]))

    ax.scatter(latent_space[:, 0], latent_space[:, 1])

    plt.show()


# https://keras.io/examples/generative/vae/

def plot_latent_space2(vae, n=30, figsize=15):
    # display an n*n 2D manifold of digits
    digit_size = 28
    scale = 1.0
    figure = np.zeros((digit_size * n, digit_size * n))
    # linearly spaced coordinates corresponding to the 2D plot
    # of digit classes in the latent space
    grid_x = np.linspace(-scale, scale, n)
    grid_y = np.linspace(-scale, scale, n)[::-1]

    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            z_sample = np.array([[xi, yi]])
            x_decoded = vae.decoder.predict(z_sample)
            digit = x_decoded[0].reshape(digit_size, digit_size)
            figure[
                i * digit_size : (i + 1) * digit_size,
                j * digit_size : (j + 1) * digit_size,
            ] = digit

    plt.figure(figsize=(figsize, figsize))
    start_range = digit_size // 2
    end_range = n * digit_size + start_range
    pixel_range = np.arange(start_range, end_range, digit_size)
    sample_range_x = np.round(grid_x, 1)
    sample_range_y = np.round(grid_y, 1)
    plt.xticks(pixel_range, sample_range_x, rotation=90)
    plt.yticks(pixel_range, sample_range_y)
    plt.xlabel("z[0]")
    plt.ylabel("z[1]")
    plt.imshow(figure, cmap="Greys_r")
    plt.show()

def plot_label_clusters(vae, data, labels):
    # display a 2D plot of the digit classes in the latent space
    z_mean, _, _ = vae.encoder.predict(data)
    print(z_mean.shape)
    print(np.array(labels).shape)
    plt.figure(figsize=(12, 10))
    plt.scatter(z_mean[:, 0], z_mean[:, 1], c=labels)
    plt.colorbar()
    plt.xlabel("z[0]")
    plt.ylabel("z[1]")
    plt.show()