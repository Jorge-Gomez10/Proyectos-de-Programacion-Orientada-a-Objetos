class Vuelo:

    def __init__(self, origen, destino, fecha, hora, precio):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.precio = precio

    def imprimir(self):
        print(f"Vuelo de {self.origen} a {self.destino} el {self.fecha} a las {self.hora}. Precio: {self.precio}")

class Reserva:

    def __init__(self, vuelo, nombre, apellidos, identificacion):
        self.vuelo = vuelo
        self.nombre = nombre
        self.apellidos = apellidos
        self.identificacion = identificacion

    def imprimir(self):
        print(f"Reserva del vuelo {self.vuelo.origen}-{self.vuelo.destino} para {self.nombre} {self.apellidos} con cedula nº {self.identificacion}")

vuelo1 = Vuelo("Quito", "Guayaquil", "2023-08-20", "12:00", 100)
vuelo2 = Vuelo("Guayaquil", "Quito", "2023-08-21", "14:00", 200)

reserva1 = Reserva(vuelo1, "Francisco", "Perez", "2100667489")
reserva2 = Reserva(vuelo2, "Magdalena", "Lopez", "1700547205")

vuelo1.imprimir()
reserva1.imprimir()

vuelo2.imprimir()
reserva2.imprimir()
