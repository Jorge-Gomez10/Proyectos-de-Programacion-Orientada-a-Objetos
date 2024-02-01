class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        raise NotImplementedError("Subclases deben implementar este método")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def mostrar_informacion(self):
        return f"Coche: {self.marca} {self.modelo}, Color: {self.color}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def mostrar_informacion(self):
        return f"Motocicleta: {self.marca} {self.modelo}, Tipo: {self.tipo}"

# Uso de abstracción
coche = Coche("Toyota", "Corolla", "Rojo")
motocicleta = Motocicleta("Honda", "CBR500R", "Deportiva")

print(coche.mostrar_informacion())         # Salida: Coche: Toyota Corolla, Color: Rojo
print(motocicleta.mostrar_informacion())   # Salida: Motocicleta: Honda CBR500R, Tipo: Deportiva
