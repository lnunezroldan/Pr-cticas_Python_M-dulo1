import random, math

lista = []
file = open("../Examen Final/notas.txt", "a+")
def archivos():
    index = int(input("Ingrese el tamaño de lista que desea: "))
    i = 1
    while i <= index :
        number = random.randint(1, 100)
        lista.append(number)
        i += 1
    file.writelines(str(lista))


def cuadrados():
    cuadrados = []
    for number in lista:
        a = math.sqrt(number)
        cuadrados.append(a)
    file.writelines(str(cuadrados))
    file.close()

archivos()
cuadrados()