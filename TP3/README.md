
# TP3 SIA - Redes neuronales: Perceptrón Simple y Multicapa

## Introducción

El siguiente TP consta de varios ejercicios: 

1. Implementa un algoritmo de perceptron simple escalon para aprender los problemas logicos AND y XOR.
2. Implementa un algoritmo de perceptrón simple lineal y no lineal para aprender a clasificar los datos del archivo “Ej2-conjunto.csv”
3. Implementa un algoritmo de perceptrón multicapa para aprender los siguientes problemas:
    - XOR (analogo al 1.).
    - Discriminar si un número es “par”, con entradas dadas por el conjunto de números decimales del 0 al 9 del archivo “Ej3B-digitos.txt”.
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
    "perceptron_type": "NON_LINEAR_LOG",
    "learning_rate": 0.0001,
    "epochs": 500000,
    "bias": 1,
    "beta": 1.0,
    "min_error": 0.1,
    "training_percentage": 0.8, 
    "k_fold": 4,
    "perceptron_options": [
        "LINEAR", "NON_LINEAR_TANH", "NON_LINEAR_LOG"
    ]
```

| Variables           | Descripción                                                          
|---------------------|------------------------------------------------------------------------------------------|
| perceptron_type     | String con el tipo de perceptron. Debe ser alguno de los valores de perceptron_options   |
| learning_rate       | Numero real entre [0,1] que representa la tasa de aprendizaje                            | 
| epochs              | Numero natural que representa la cantidad de epocas                                      | 
| bias                | Numero natural que representa el umbral/bias.                                            | 
| beta                | Numero flotante que representa el valor de beta para el perceptron no lineal             |   
| min_error           | Numero real entre [0,1] que representa la candicion de corte de error minimo             | 
| training_percentage | Numero real entre [0,1] que representa el porcentaje de los datos tomandos para entrenar | 
| k_fold              | Numero natural para entrenar al perceptron con validacion k-cruzada       | 
| perceptron_options  | Arreglo de strings con los tipos de perceptrones validos (NO MODIFICAR)                  |

### Ejercicio 3

``` json
{
   
}
