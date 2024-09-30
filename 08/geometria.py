import math

def menu():
    print("\n--- Cálculos Geométricos ---")
    print("1. Área de un rectángulo")
    print("2. Perímetro de un rectángulo")
    print("3. Área de un círculo")
    print("4. Circunferencia de un círculo")
    print("5. Salir")
    return input("Seleccione una opción (numero): ")

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def area_circulo(radio):
    return math.pi * radio ** 2

def circunferencia_circulo(radio):
    return 2 * math.pi * radio