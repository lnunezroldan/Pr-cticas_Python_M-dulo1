from datetime import datetime, date

class Persona:
    a = datetime.now()
    fecha = a.date()
    hora = a.hour
    minuto = a.minute
    def __init__(self, nombre, edad, nacionalidad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.saldo = saldo

    def datos(self):
        try:
            self.nombre = input("Ingrese su nombre: ")
            self.edad = input("Ingrese su edad: ")
            self.nacionalidad = input("Ingrese su nacionalidad: ")
        except (TypeError):
            print("Error de tipo de datos")

    def cumpleanos(self):
        self.edad = self.edad + 1
        print("La nueva edad sería: {}".format(self.edad))

    def registro(self):
        print(f"La persona se registró el {Persona.fecha}, a las {Persona.hora} horas y {Persona.minuto} minutos.")

person = Persona("Luis", 33, "peruano", 3500)
person.cumpleanos()
person.cumpleanos()

