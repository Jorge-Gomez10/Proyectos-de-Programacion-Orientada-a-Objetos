class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario

    def obtener_nombre(self):
        return self.__nombre

    def obtener_salario(self):
        return self.__salario

    def calcular_bono(self):
        raise NotImplementedError("Subclases deben implementar este método")


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre, salario_mensual)
        self.__bono_anual = 0.1 * salario_mensual

    def calcular_bono(self):
        return self.__bono_anual


class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        super().__init__(nombre, salario_por_hora)
        self.__horas_trabajadas = horas_trabajadas

    def calcular_bono(self):
        return 0.05 * (self.obtener_salario() * self.__horas_trabajadas)


# Crear instancias de las clases
empleado_fulltime = EmpleadoTiempoCompleto("Juan Pérez", 5000)
empleado_parttime = EmpleadoMedioTiempo("Ana López", 20, 25)

# Demostrar encapsulación y herencia
print(f"{empleado_fulltime.obtener_nombre()} - Salario: ${empleado_fulltime.obtener_salario()}")
print(f"Bono anual: ${empleado_fulltime.calcular_bono()}")

print(f"\n{empleado_parttime.obtener_nombre()} - Salario/hora: ${empleado_parttime.obtener_salario()}")
print(f"Bono mensual: ${empleado_parttime.calcular_bono()}")

# Ejemplo de polimorfismo
empleados = [empleado_fulltime, empleado_parttime]

print("\nBono total para todos los empleados:")
for empleado in empleados:
    print(f"{empleado.obtener_nombre()}: ${empleado.calcular_bono()}")
