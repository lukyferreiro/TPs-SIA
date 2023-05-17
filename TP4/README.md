
# TP4 SIA - Aprendizaje No Supervisado

## Introducción

El siguiente TP consta de varios ejercicios: 

1. A partir del conjunto de datos del archivo europe.csv:
    - Implementar una red de Kohonen para asociar paises que posean las mismas caracteristicas geopoliıticas,
     economicas y sociales.
    - Implementar una red neuronal utilizando la regla de Oja para calcular la primer componente principal
     de los datos.
2. Implementar el modelo de Hopfield para asociar matrices ruidosas de tamaño 5×5, que corresponden con
   patrones de letras del abecedario representadas con 1 y −1.


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

Cada red neuronal consta de su propio archivo de ejecucion: main_kohonen.py, main_hopfield.py, main_pca.py y main_oja.py

```sh
pipenv shell
python main_kohonen.py
```

## Configuración

``` json
{
    "k": 4,
    "learning_rate": 0.1,
    "radius": 1,
    "epochs": 100,
    "likeness": "EUCLIDEAN",
    "mutate_prob": 1.0,
    "likeness_options": [
        "EUCLIDEAN", "EXPONENTIAL"
    ]
}
```

| Variables         | Uso           | Descripción                                                          
|-------------------|---------------|----------------------------------------------------------------------------------------|
| k                 | Kohonen       | Numero natural que representa el tamaño de la grilla KxK para la red de Kohonen        |
| learning_rate     | Kohonen y Oja | Numero real entre [0,1] que representa la tasa de aprendizaje                          | 
| radius            | Kohonen       | Numero natural que representa el valor del radio en la red de Kohonen                  | 
| epochs            | Todos         | Numero natural que representa la cantidad de epocas                                    | 
| likeness          | Kohonen       | Numero natural que representa el metodo de similitud en la red de Kohonen.             |
| mutate_prob       | Hopfield      | Numero real entre [0,1] que representa el porcentaje de mutacion en la red de Hopfield | 
| likeness_options  | Kohonen       | Arreglo de strings con los metodos de similitud permitidos (NO MODIFICAR)              |