nombre1 = input("Ingrese su nombre: ")
edad1 = int(input("Ingrese su edad: "))

print("El tipo de dato de 'nombre1' es: {}".format(type(nombre1)))
print("El tipo de dato de 'edad1' es: {}".format(type(edad1)))

trabajadores = []
name1 = input("Usted es el 'Trabajador 1', por favor ingrese su nombre: ")
age1 = int(input("Usted es el 'Trabajador 1', por favor ingrese su edad: "))
name2 = input("Usted es el 'Trabajador 2', por favor ingrese su nombre: ")
age2 = int(input("Usted es el 'Trabajador 2', por favor ingrese su edad: "))

trabajadores.extend((name1, age1, name2, age2))
print(trabajadores)
suma = trabajadores[1] + trabajadores[3]
print("La suma de las edades de los trabajadores 1 y 2 es: {}".format(suma))



