
# TP2 SIA - Color Searcher

## Introducción

El siguiente TP implementa un sistema que, mediante Algoritmos Genéticos, mezcla proporciones
de los diferentes colores de una paleta con el fin de encontrar un color deseado.

### Requisitos

- Python 3.10.
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

Posicionado en la carpeta del TP2 ejecutar:

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
Todas las posibles variables a configurar se deben detallar en el archivo config.json

A continuacion se detalla en una tabla las posibles variables, su caso de uso y descripcion:


| Variables         | Casos de uso            | Descripción                                                          
|-------------------|-------------------------|---------------------------------------------------------------------------------|
| palette_csv_path  | Siempre                 | String al path del archivo csv (desde main.py) con la paleta de colores         |
| N                 | Siempre                 | Numero natural que representa la poblacion inical                               | 
| target_color      | Siempre                 | Arreglo [R,G,B], con 0 <= R,G,B <= 255 que representa el color objetivo         | 
| selection_method  | Siempre                 | Metodo de seleccion a usar. Debe ser alguno de los valores de selection_options | 
| crossing_type     | Siempre                 | Metodo de cruza a usar. Debe ser alguno de los valores de crossing_options      | 
| mutation_type     | Siempre                 | Metodo de mutacion a usar. Debe ser alguno de los valores de mutation_options   |
| mutation_pm       | Siempre                 | Numero real entre [0,1] que representa la probabilidad de mutacion              |
| select_new_generation_type | Siempre        | Metodo de seleccion de la nueva generacion. Debe ser un valor de select_new_generation_options  |
| K                 | Siempre                 | Numero natural que representa la cantidad de individuos a seleccionar           |
| max_generations   | Siempre                 | Numero natural que representa la cantidad maxima de generaciones a esperar hasta obtener la solucion   |       
| d_error           | Siempre                 | Numero real entre (0,1) que representa el error minimo entre el individuo mas apto y el color objetivo |
| time              | Opcional                | Numero entero que representa el tiempo maximo en segundos a esperar la solucion  |
| selection_options | Siempre (NO MODIFICAR)  | Arreglo de strings con los metodos de seleccion implementados                   |
| crossing_options  | Siempre (NO MODIFICAR)  | Arreglo de strings con los metodos de cruza implementados                       |
| mutation_options  | Siempre (NO MODIFICAR)  | Arreglo de strings con los metodos de mutacion implementados                    |
| select_new_generation_options  | Siempre (NO MODIFICAR)  | Arreglo de strings con los metodos de seleccion de la nueva generacion implementados     |

Nota: max_generations, d_error y time son las condiciones de corte
Time puede tener valor -1, en cuyo caso no se toma en cuenta dicha condición de corte

### Ejemplo de config.json

``` json
{
    "palette_csv_path": "./src/colores.csv",
    "N": 100, 
    "target_color": [138, 16, 0],
    "selection_type": "ELITE", 
    "crossing_type": "ONE_POINT",       
    "mutation_type": "ONE_GEN",   
    "mutation_pm": 0.5,
    "select_new_generation_type": "USE_ALL",
    "K": 100,
    "max_generations": 1000,
    "d_error": 0.01,
    "time": 60,
    "selection_options": [
        "ELITE", "ROULETTE", "UNIVERSAL", "TOURNAMENT_DETERMINISTIC", "TOURNAMENT_PROBABILISTIC"
    ],
    "crossing_options": [
        "ONE_POINT", "DOUBLE_POINT", "ANGULAR", "UNIFORM"
    ],
    "mutation_options": [
        "ONE_GEN", "MULTIGEN_LIMITED", "MULTIGEN_UNIFORM", "COMPLETE"
    ],
    "select_new_generation_options": [
        "USE_ALL", "NEW_OVER_ACTUAL"
    ]
}
```
