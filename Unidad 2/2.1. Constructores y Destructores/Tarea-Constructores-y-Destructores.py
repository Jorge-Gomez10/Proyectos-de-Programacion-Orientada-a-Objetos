class Archivo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__estado = "Cerrado"
        print(f"Se ha creado el archivo: {self.__nombre}")

    def abrir(self):
        if self.__estado == "Cerrado":
            self.__estado = "Abierto"
            print(f"Se ha abierto el archivo: {self.__nombre}")
        else:
            print(f"Error: El archivo {self.__nombre} ya está abierto.")

    def cerrar(self):
        if self.__estado == "Abierto":
            self.__estado = "Cerrado"
            print(f"Se ha cerrado el archivo: {self.__nombre}")
        else:
            print(f"Error: El archivo {self.__nombre} ya está cerrado.")

    def __del__(self):
        # Destructor: Se ejecuta cuando el objeto se elimina
        if self.__estado == "Abierto":
            self.cerrar()
        print(f"Se ha eliminado el archivo: {self.__nombre}")


# Crear instancias de la clase Archivo
archivo1 = Archivo("documento.txt")
archivo2 = Archivo("imagen.png")

# Abrir y cerrar archivos
archivo1.abrir()
archivo2.abrir()
archivo1.cerrar()

# Eliminar archivos
del archivo1
del archivo2
