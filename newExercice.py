"""
    Dado un número variable de argumentos enteros, devuelve 
    los digitos que no están presentes en niguno de ellos
"""


def separateDigits(lista):
    var = lista
    convertTo = ''.join([str(i) for i in var])
    return convertTo


def convertToList(cadena):
    cad = []
    for i in cadena:
        cad.append(i)
    return cad


def convertDateint(lista):
    valInt = [int(i) for i in lista]
    return valInt


def verificar(vector):
    datos = []
    for i in range(0, 10):
        if i not in vector:
            datos.append(i)
    return datos


if __name__ == "__main__":

    lista = [12, 34, 56, 78]
    dates = separateDigits(lista)
    print("=======================")
    print(dates)
    d = convertToList(dates)
    datosEnteros = convertDateint(d)
    print("=======================")
    print(d)
    print("=======================")
    print(datosEnteros)
    print("=======================")
    print(convertToList(dates))
    print("=======================")
    print(verificar(datosEnteros))
