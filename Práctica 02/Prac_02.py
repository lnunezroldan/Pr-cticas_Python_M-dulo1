from datetime import datetime, date

class Persona:
     def __init__(self, nombre, edad, nacionalidad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.saldo = saldo

class Persona2 (Persona):
    def __init__(self, nombre, edad, nacionalidad, saldo, monto):
        Persona().__init__(self, nombre, edad, nacionalidad, saldo)
        self.monto = monto
    def transferencia(self, monto):
        self.saldo = self.saldo - self.monto
    def mostrar_saldo(self):
        if self.saldo > 0:
            print(f"El saldo actual es {self.saldo}")
        else:
            print("Saldo Insuficiente")


person1 = Persona("Luis", 33, "peruano", 5500)
person2 = Persona2("Javier", 29, "peruano", 8000, 3500)

transfer = Persona2.transferencia(3500)
person2.mostrar_saldo()

