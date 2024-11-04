## Ejercicio 3: Simulación de lanzamiento de moneda
"""Escribe un programa que simule el lanzamiento de una moneda 100 veces y cuente cuántas veces salió cara y cuántas cruz."""
import random as rd

def lanzar_moneda(veces):
    if not isinstance(veces,(int)):
        return "Veces debe ser un numero entero válido"
    else:
        lados = ["Cara","Cruz"]
        caras = 0
        cruces = 0
        for vez in range(veces):
            eleccion = rd.choice(lados)
            if eleccion == lados[0]:
                caras+=1
            if eleccion == lados[1]:
                cruces+=1
        return caras,cruces            
num_veces = int(input("Cantidad de veces a lanzar la moneda: "))

caras, cruces = lanzar_moneda(num_veces)

print(f"En {num_veces} intentos. {caras} fueron Caras y {cruces} fueron Cruces.")

