def ingresa_temperaturas_diarias():
    temperaturas = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura para el día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedio_semanal = sum(temperaturas) / len(temperaturas)
    return promedio_semanal

def main():
    print("Ingrese las temperaturas diarias para la semana:")
    temperaturas_diarias = ingresa_temperaturas_diarias()

    promedio = calcular_promedio_semanal(temperaturas_diarias)

    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()

