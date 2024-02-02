lista = [20, 10, 5, 15, 8, 11, 60, 80, 90, 31]
cubos = []
cuadrados = []

for factor in lista:
    cubos.append(factor**3)

for elemento in lista:
    cuadrados.append(elemento**2)

print(cubos)
print(cuadrados)

suma = cubos + cuadrados
suma.reverse()
print("La suma de ambas listas en su forma inversa es: {}".format(suma))

