
import random
lista = []
def addtolist():
    index = int(input("Ingrese la cantidad de número a agregar: "))
    for count in range(index):
        number = random.randint(1, index)
        lista.append(number)

addtolist()
print(lista)

other_list = []
def not_repeated():
    for numero in lista:
        if lista.count(numero) > 1 :
            continue
        else:
            other_list.append(numero)

not_repeated()
print(other_list)

def to_order():
    other_list.sort()
    print("La lista ordenada de menor a mayor es: {}".format(other_list))
    other_list.reverse()
    print("La lista ordenada de mayor a menor es: {}".format(other_list))

to_order()

def par():
    pares = []
    for number in other_list:
        if number % 2 == 0 :
            pares.append(number)
        continue
    max_number = max(pares)
    print("El mayor par de la lista es {}".format(max_number))

par()
