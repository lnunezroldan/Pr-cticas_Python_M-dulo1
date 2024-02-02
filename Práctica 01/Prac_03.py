diccionario = {}
diccionario["nombre"] = input("Ingrese su nombre: ")
diccionario["apellidos"] = input("Ingrese sus apellidos: ")
diccionario["edad"] = input("Ingrese su edad: ")
diccionario["dni"] = input("Ingrese su DNI: ")

print("Los valores del diccionarios son: {}".format(diccionario.values()))

diccionario["profesion"] = "Ingeniero"
del diccionario["dni"]

print("El diccionario actualizado es: {}".format(diccionario))
