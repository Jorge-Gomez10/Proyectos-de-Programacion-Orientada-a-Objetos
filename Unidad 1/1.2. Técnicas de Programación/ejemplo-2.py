class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        else:
            return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        else:
            return False

# Uso de encapsulación
cuenta = CuentaBancaria("Juan Perez", 1000)

print(cuenta.obtener_saldo())   # Salida: 1000
cuenta.depositar(500)
print(cuenta.obtener_saldo())   # Salida: 1500
cuenta.retirar(200)
print(cuenta.obtener_saldo())   # Salida: 1300
