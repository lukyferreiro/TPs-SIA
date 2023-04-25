def operation_data(operation, bias):

    switcher = {
        "AND": get_and_data(),
        "XOR": get_xor_data(),
    }

    x, y = switcher.get(operation, "Operación invalida")

    # xo es el umbral/bias
    for data in x:
        data.insert(0, bias)

    return x, y

# x: entrada 
# y: salida esperada
def get_and_data():
    x = [ [-1, 1], [1, -1], [-1, -1], [1, 1] ]
    y = [-1, -1, -1, 1]

    return x, y

def get_xor_data():
    x = [ [-1, 1], [1, -1], [-1, -1], [1, 1] ]
    y = [1, 1, -1, -1]

    return x, y 
