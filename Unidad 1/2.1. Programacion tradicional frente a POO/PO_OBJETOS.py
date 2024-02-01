class ClimaDiario:
    def __init__(self):
        self.temperaturas_diarias = []

    def ingresar_temperatura_diaria(self, temperatura):
        self.temperaturas_diarias.append(temperatura)

    def ingresar_temperaturas_semanales(self):
        for dia in range(1, 8):
            temperatura = float(input(f"Ingrese la temperatura para el día {dia}: "))
            self.ingresar_temperatura_diaria(temperatura)

    def calcular_promedio_semanal(self):
        if len(self.temperaturas_diarias) == 0:
            return 0  # Evitar división por cero si no se ingresaron temperaturas

        promedio_semanal = sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)
        return promedio_semanal


def main():
    clima_semanal = ClimaDiario()

    print("Ingrese las temperaturas diarias para la semana:")
    clima_semanal.ingresar_temperaturas_semanales()

    promedio = clima_semanal.calcular_promedio_semanal()

    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()

