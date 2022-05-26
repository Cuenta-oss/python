def sumarYGanar(lista):
    myVar = 0
    contador = 0
    print("SUMAR Y GANAR")
    print("Vaya sumando todos los números que le iré diciendo. Empezamos por 0.")
    for i in range(len(lista)):
        myVar += lista[i]
        varUser = int(input("Mas " + str(lista[i]) + ": "))
        contador += 1
        if varUser != myVar:
            print("Ha fallado, pero ha acertado " + str(i) + " veces.")
            break
    if varUser == myVar:
        print("Enhorabuena, GANASTE")

if __name__ == '__main__':
    myList = [50, 4, 28, 33, 12]
    sumarYGanar(myList)
