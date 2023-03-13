import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage,AnnotationBbox

# La función get_image toma como entrada el nombre de una pokeball y devuelve una imagen de la pokebola.
# La imagen se lee del archivo de imagen correspondiente.
def get_image(name):
    path = f"img/{name}.png"
    im = plt.imread(path)
    return im

# La función offset_image toma como entrada la coordenada de la barra, el nombre del pokemon y el objeto de
# ejes de la figura. Esta función crea una imagen de la pokebola utilizando la función get_image y crea un
# objeto OffsetImage que se utiliza para agregar la imagen en la posición correcta en el gráfico de barras.
# La imagen se ajusta a un tamaño determinado utilizando el parámetro zoom. La función AnnotationBbox se
# utiliza para crear un objeto de anotación que se ajusta a la barra y contiene la imagen de la pokebola.
# La ubicación de la caja de anotación se especifica mediante xybox, xycoords y boxcoords. Finalmente,
# se agrega el objeto de anotación al eje de la figura utilizando la función ax.add_artist.
def offset_image(coord, name, ax):
    img = get_image(name)
    im = OffsetImage(img, zoom=0.05)
    im.image.axes = ax

    ab = AnnotationBbox(im, (coord, 0),  xybox=(0., -16.), frameon=False,
                        xycoords='data',  boxcoords="offset points", pad=0)

    ax.add_artist(ab)