# Programa para calcular el área de un triángulo

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Args:
    base (float): Longitud de la base del triángulo.
    altura (float): Altura del triángulo.

    Returns:
    float: Área del triángulo.
    """
    # Fórmula del área de un triángulo: área = (base * altura) / 2
    area = (base * altura) / 2
    return area

# Ejemplo de uso del programa
if __name__ == "__main__":
    # Datos de entrada
    base_triangulo = 5.0
    altura_triangulo = 8.0

    # Mostrar las dimensiones del triángulo
    print(f"Base del triángulo: {base_triangulo}")
    print(f"Altura del triángulo: {altura_triangulo}")

    # Calcular el área del triángulo
    area_calculada = calcular_area_triangulo(base_triangulo, altura_triangulo)

    # Mostrar el resultado
    print(f"Área del triángulo: {area_calculada}")
