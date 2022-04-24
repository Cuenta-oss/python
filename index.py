"""
    Realizar un programa :
    Que extraiga los digitos de la siguiente cadena de texto.
    Que los ordene de menor a mayor y los devuelva en una cadena de texto.
    Que sume todos los digitos y devuelva el resultado de la suma total.
    Todos estos resultados deben ser mostrados por consola de manera simultanea.  
"""

numeros = []


def funcion(cadena):

    letras = []
    for i in cadena:
        try:
            numeros.append(int(i))
        except ValueError:
            letras.append(i)
    return numeros


def ordenar(num):
    lista = sorted(num)
    convertToString = ', '.join([str(i) for i in lista])
    return convertToString


def sumarNumerosLista(num):
    lista = num
    suma = 0
    for i in lista:
        suma += i
    return suma

if __name__ == "__main__":
    cad = "3ha4sa2df3as5f3ad5a4sdf8df6"
    print("Digitos extraidos de la cadena: \n", funcion(cad))
    print("=================================================")
    print("Digitos convertidos a String: \n", ordenar(numeros))
    print("=================================================")
    print("La suma de los digitos es: \n", sumarNumerosLista(numeros))
