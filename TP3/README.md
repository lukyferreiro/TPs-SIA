
# TP3 SIA - Redes neuronales: Perceptrón Simple y Multicapa

## Introducción

El siguiente TP consta de varios ejercicios: 

1. Implementa un algoritmo de perceptron simple escalon para intentar aprender los problemas logicos AND y XOR.
2. Implementa un algoritmo de perceptrón simple lineal y no lineal para intentar aprender a clasificar los datos del archivo “Ej2-conjunto.csv”
3. Implementa un algoritmo de perceptrón multicapa para intentar aprender los siguientes problemas:
    - XOR (analogo al 1.).
    - Discriminar si un número es “par”, con entradas dadas por el conjunto de "imagenes" de números decimales del 0 al 9 del archivo “Ej3B-digitos.txt”.
    - Determinar qué dígito se corresponde con la entrada a la red. Una vez que la red haya aprendido, utilizar patrones correspondientes a los dígitos del conjunto de datos, con sus píxeles afectados por ruido.


### Requisitos

- Python 3.10.
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

Posicionado en la carpeta del TP3 ejecutar:

```sh
pipenv install
```

para instalar las dependencias necesarias en el ambiente virtual.

## Ejecución

Cada ejercicio consta de una carpeta correspondiente a su resolucion con su propio main.py.
Entonces, posicionado en la carpeta del ejercicio a correr, ejecutar:

```sh
pipenv shell
python main.py
```

Nota: el ejercicio 3 cuenta con tres main.py distintos correspondientes a cada inciso.

## Configuración

Cada ejercicio consta de su propia carpeta con su propio archivo de configuración.

### Ejercicio 1

``` json
{
    "operation": "AND",
    "learning_rate": 0.1,
    "epochs": 100,
    "bias": 1,
    "operation_options": [
        "AND", "XOR"
    ]
}
```

| Variables         | Descripción                                                          
|-------------------|------------------------------------------------------------------------------------------|
| operation         | String con la operacion a realizar. Debe ser alguno de los valores de operation_options  |
| learning_rate     | Numero real entre [0,1] que representa la tasa de aprendizaje                            | 
| epochs            | Numero natural que representa la cantidad de epocas                                      | 
| bias              | Numero natural que representa el umbral/bias.                                            | 
| operation_options | Arreglo de strings con los operaciones permitidas (NO MODIFICAR)                         |


### Ejercicio 2

``` json
{
    "perceptron_type": "LINEAR",
    "learning_rate": 0.001,
    "epochs": 50000,
    "bias": 1,
    "beta": 1.0,
    "min_error": 0.1,
    "training_type": "PERCENTAGE",
    "training_percentage": 0.8, 
    "k_fold": 4,
    "perceptron_options": [
        "LINEAR", "NON_LINEAR_TANH", "NON_LINEAR_LOG"
    ],
    "training_options": [
        "PERCENTAGE", "K-FOLD"
    ]
}
```

| Variables           | Descripción                                                          
|---------------------|------------------------------------------------------------------------------------------|
| perceptron_type     | String con el tipo de perceptron. Debe ser alguno de los valores de perceptron_options   |
| learning_rate       | Numero real entre [0,1] que representa la tasa de aprendizaje                            | 
| epochs              | Numero natural que representa la cantidad de epocas                                      | 
| bias                | Numero natural que representa el umbral/bias.                                            | 
| beta                | Numero flotante que representa el valor de beta para el perceptron no lineal             |   
| min_error           | Numero real entre [0,1] que representa la candicion de corte de error minimo             | 
| training_type       | String con el tipo de entrenamiento. Debe ser alguno de los valores de training_options  |
| training_percentage | Numero real entre [0,1] que representa el porcentaje de los datos tomandos para entrenar | 
| k_fold              | Numero natural para entrenar al perceptron con validacion k-cruzada                      | 
| perceptron_options  | Arreglo de strings con los tipos de perceptrones validos (NO MODIFICAR)                  |
| training_options    | Arreglo de strings con los tipos de entrenamiento validos (NO MODIFICAR)                 |

### Ejercicio 3

Este ejercicio cuenta con un archivo config.json correspondiente a cada inciso.
De todas formas, el formato general del archivo es el siguiente:

``` json
{
    "input_file": "./data/Ej3B-digitos.txt",
    "learning_rate": 0.01,
    "epochs": 20000,
    "bias": 1,
    "training_percentage": 0.9,
    "training_type": "PERCENTAGE",
    "k_fold": 4,
    "min_error": 0.001,

    "output_activation": "TANH",
    "hidden_activation": "TANH",
    "beta": 1.0,
    "qty_hidden_layers": 2,
    "qty_nodes_in_hidden_layers": [25, 15],

    "optimizer_method": "MOMENTUM",
    "alpha": 0.8,
    "beta1": 0.9,
    "beta2": 0.999,
    "epsilon": 1e-8,

    "activation_options": [
        "TANH", "LOG"
    ],
    "optimizer_options": [
        "ADAM", "MOMENTUM", "NONE"
    ],
    "training_options": [
        "PERCENTAGE", "K-FOLD"
    ]
}
```

| Variables           | Descripción                                                          
|---------------------|------------------------------------------------------------------------------------------|
| input_file          | String con el path al archivo donde se encuentran los datos                              |
| learning_rate       | Numero real entre [0,1] que representa la tasa de aprendizaje                            | 
| epochs              | Numero natural que representa la cantidad de epocas                                      | 
| bias                | Numero natural que representa el umbral/bias.                                            | 
| training_percentage | Numero real entre [0,1] que representa el porcentaje de los datos tomandos para entrenar | 
| training_type       | String con el tipo de entrenamiento. Debe ser alguno de los valores de training_options  | 
| k_fold              | Numero natural para entrenar al perceptron con validacion k-cruzada                      | 
| min_error           | Numero real entre [0,1] que representa la candicion de corte de error minimo             | 
| output_activation   | String con el tipo de activaccion de la capa de salida. Debe ser alguno de los valores de activation_options         | 
| hidden_activation   | String con el tipo de activacion de la capa oculta. Debe ser alguno de los valores de activation_options             | 
| beta                | Numero flotante que representa el valor de beta usado en los metodos de activacion       |   
| qty_hidden_layers   | Numero natural que representa la cantidad de capas ocultas del perceptron multicapa      | 
| qty_nodes_in_hidden_layers   | Arreglo de numeros naturales con la cantidad de nodos de cada capa oculta       | 
| optimizer_method    | String con el tipo de optimizacion. Debe ser alguno de los valores de optimizer_options  | 
| alpha               | Numero real entre [0,1] usado en el metodo de optimizacion MOMENTUM                      | 
| beta1               | Numero real entre [0,1] usado en el metodo de optimizacion ADAM                          | 
| beta2               | Numero real entre [0,1] usado en el metodo de optimizacion ADAM                          | 
| epsilon             | Numero real entre [0,1] usado en el metodo de optimizacion ADAM                          | 
| activation_options  | Arreglo de strings con los tipos de activacion validos (NO MODIFICAR)                    |
| optimizer_options   | Arreglo de strings con los tipos de optimizacion validos (NO MODIFICAR)                  |
| training_options    | Arreglo de strings con los tipos de entrenamiento validos (NO MODIFICAR)                 |
 
