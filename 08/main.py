"""8. Cálculo de áreas y perímetros
Crea un módulo llamado `geometria.py` que contenga funciones para calcular el área y el
perímetro de figuras geométricas. Las figuras a incluir son:
1. Rectángulo (área y perímetro).
2. Círculo (área y circunferencia).
Luego, importa estas funciones en otro archivo y permite que el usuario elija qué cálculo
realizar."""

import geometria as gm


while True:
    opcion = gm.menu()
        
    if opcion == "1":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = gm.area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area}")
        
    elif opcion == "2":
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        perimetro = gm.perimetro_rectangulo(base, altura)
        print(f"El perímetro del rectángulo es: {perimetro}")
        
    elif opcion == "3":
        radio = float(input("Ingrese el radio del círculo: "))
        area = gm.area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
        
    elif opcion == "4":
        radio = float(input("Ingrese el radio del círculo: "))
        circunferencia = gm.circunferencia_circulo(radio)
        print(f"La circunferencia del círculo es: {circunferencia:.2f}")
        
    elif opcion == "5":
        print("¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, intente de nuevo.")