from math import pi


def circle():
    """
    Ejercicio 6 - Geometría de Círculo

    Dado el radio de un círculo, calcular e imprimir:
    1. El área (π × radio²)
    2. La circunferencia (2 × π × radio)
    """
    radio = 5
    area_circulo = (pi * 5 ** 2)
    circunferencia_circulo = (2*pi*5)

    print(area_circulo)
    print(circunferencia_circulo)

circle()