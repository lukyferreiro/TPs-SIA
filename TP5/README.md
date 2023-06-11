
# TP5 SIA - Deep Learning: Autoencoders

## Introducción

El siguiente TP consta de varios ejercicios: 
1. Implementar un:
    - Autoencoder básico para las imágenes binarias de la lista de caracteres del archivo "font.h".
     Ademas se testean diferentes arquitecturas, tecnicas de optimización y como la red puede generar un nueva letra
     que no pertenece al conjunto de entrenamiento.
    - Denoising Autoencoder para estudiar su capacidad de eliminar ruido sobre el mismo dataset.
2. Construir un conjunto de datos nuevos y utilizar el Autoencoder anterior para generar una nueva muestra
para juzgar que pertenece al conjunto de datos presentado al autoencoder.


### Requisitos

- Python 3.10.
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

Posicionado en la carpeta del TP5 ejecutar:

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual.

## Ejecución

```sh
pipenv shell
python main.py
```

## Configuración

``` json
{
}
```