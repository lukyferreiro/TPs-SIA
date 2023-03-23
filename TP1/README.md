
# TP1 SIA - Métodos de Búsqueda para Fill-Zone

## Introducción
El siguiente TP se encarga de implementar las soluciones para distintos metodos
de busqueda del juego Fill-Zone (http://www.mygamesworld.com/game/7682/Fill_Zone.html)
y obtener conclusiones de que metodos son mas eficientes.

### Requisitos

- Python 3.10.
- pip3
- [pipenv](https://pypi.org/project/pipenv/)

### Instalación

Posicionado en la carpeta del TP1 ejecutar:

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

Al ejecutar el comando python main.py, se le solicitara al usuario que ingrese por 
terminal el tamaño del tablero (mayor o igual a 4) y la cantidad de colores (entre 2 
y 9). 

Se recomienda no superar el tamaño 20x20 y no usar los algoritmos BFS y A* con Dijkstra Distance
(ha no ser que te encuentra muy paciente).

Tras ingresar esos dos valores, se desplegara una pantalla acorde al tamaño elegido,
con instrucciones para poder elegir el método de búsqueda a usar y la heurística a aplicar
(si es que corresponde).

Tras seleccionar toda la configuración se deberá aguardar a que el algoritmo correspondiente
calcule la solución, y tras esto se mostrará el juego FillZone, donde se podrá avanzar
y retroceder por medio de las flechas RIGHT y LEFT del teclado.

Por último, al completar el tablero, se podran visualizar los datos obtenidos por el algoritmo.