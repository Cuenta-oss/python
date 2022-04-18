"""
    Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente 
    todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y 
    multip([1,2,3,4]) debería devolver 24.
"""

from lib2to3.pytree import convert


def sum(lista):
    s = 0
    for i in lista:
        s = s + i
    return s


def mult(lista):
    s = 1
    for i in lista:
        s = s * i
    return s


"""
    Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
    "estoy probando" debería devolver la cadena "odnaborp yotse"
"""


def inversa(cadena):
    cadena2 = ""
    for i in cadena:
        cadena2 = i + cadena2
    return cadena2


"""
    Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen 
    el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""


def es_Polidromo(cadena):
    convert = cadena.lower()
    print(convert)
    cadena2 = ""
    for i in convert:
        cadena2 = i + cadena2
        if cadena2 == convert:
            return True

    return False


"""
    Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro 
    en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""


def superposicion(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False


"""
    Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
    Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""


def generar_Caracteres(val1, val2):
    for i in range(val1):
        print(val2, end="")
    print("\n")


"""
    Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la 
    pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
    
    ****
    *********
    *******
"""


def procedimiento(lista):
    caracter = "*"
    for i in lista:
        print(i * caracter)


if __name__ == "__main__":
    print(sum([1, 2, -3, 4]))
    print(mult([1, 2, 3, -4]))
    print(inversa("Estoy probando"))
    print(es_Polidromo("Radar"))
    print("===================")
    print(superposicion([2, 3, 4, 5], [10, 0, 6, 7]))
    generar_Caracteres(10, "*")
    procedimiento([9, 5, 7, 2, 10])
