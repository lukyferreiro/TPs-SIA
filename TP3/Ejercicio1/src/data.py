def operation_data(operation):

    switcher = {
        "AND": get_and_data(),
        "XOR": get_xor_data(),
    }

    return switcher.get(operation, "Operación invalida")

# x: entrada (xo es el umbral/bias)
# y: salida esperada

def get_and_data():
    x = [ [-1, 1], [1, -1], [-1, -1], [1, 1] ]
    y = [-1, -1, -1, 1]

    return x, y

def get_xor_data():
    x = [ [-1, 1], [1, -1], [-1, -1], [1, 1] ]
    y = [1, 1, -1, -1]

    return x, y 
