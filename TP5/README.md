
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
    "learning_rate": 0.001,
    "epochs": 10000,
    "bias": 1,
    "training_percentage": 1.0,
    "min_error": 0.001,

    "output_activation": "LOG",
    "hidden_activation": "TANH",
    "beta": 1.0,

    "qty_hidden_layers": 3,
    "qty_nodes_in_hidden_layers": [25,12,5],
    "latent_space_size": 2,

    "optimizer_method": "ADAM",
    "alpha": 0.8,
    "beta1": 0.9,
    "beta2": 0.999,
    "epsilon": 1e-8,

    "activation_options": [
        "TANH", "LOG"
    ],
    "optimizer_options": [
        "ADAM", "MOMENTUM", "NONE"
    ]
}
```

| Variables           | Descripción                                                          
|---------------------|------------------------------------------------------------------------------------------|
| learning_rate       | Numero real entre [0,1] que representa la tasa de aprendizaje                            | 
| epochs              | Numero natural que representa la cantidad de epocas                                      | 
| bias                | Numero natural que representa el umbral/bias.                                            | 
| training_percentage | Numero real entre [0,1] que representa el porcentaje de los datos tomandos para entrenar | 
| min_error           | Numero real entre [0,1] que representa la candicion de corte de error minimo             | 
| output_activation   | String con el tipo de activaccion de la capa de salida. Debe ser alguno de los valores de activation_options | 
| hidden_activation   | String con el tipo de activacion de la capa oculta. Debe ser alguno de los valores de activation_options     | 
| beta                | Numero real que representa el valor de beta usado en los metodos de activacion           |   
| qty_hidden_layers   | Numero natural que representa la cantidad de capas ocultas de los perceptrones del autoencoder      | 
| qty_nodes_in_hidden_layers  | Arreglo de numeros naturales con la cantidad de nodos de cada capa oculta        | 
| latent_space_size   | Cantidad de nodos en la capa latente                                                     | 
| optimizer_method    | String con el tipo de optimizacion. Debe ser alguno de los valores de optimizer_options  | 
| alpha               | Numero real entre [0,1] usado en el metodo de optimizacion MOMENTUM                      | 
| beta1               | Numero real entre [0,1] usado en el metodo de optimizacion ADAM                          | 
| beta2               | Numero real entre [0,1] usado en el metodo de optimizacion ADAM                          | 
| epsilon             | Numero real entre [0,1] usado en el metodo de optimizacion ADAM                          | 
| activation_options  | Arreglo de strings con los tipos de activacion validos (NO MODIFICAR)                    |
| optimizer_options   | Arreglo de strings con los tipos de optimizacion validos (NO MODIFICAR)                  |
 
