## Ejercicio 5: Cálculo de mediana
"""Escribe un programa que calcule la mediana de una lista de números proporcionada por el usuario."""

import math
import numpy as np
def crear_lista_numerica():
    print("Escribe la cantidad de numeros con la que quieres tratar")

    n = int(input("Cantidad: "))
    m = range(n)

    nums = []
    for i in m:
        print(f"Faltan {len(m)-i} numeros")
        num = float(input("Ingresa un numero: "))
        nums.append(num)
    return nums

def pillar_mediana(nums):
    nums.sort()
    half_index = len(nums)//2
    print(half_index)
    if(len(nums)%2==0):
        next_half_index = half_index+1
        values = [nums[half_index],nums[next_half_index]]
        return sum(values)/2
    else:
        return nums[half_index]
    

nums = crear_lista_numerica()

med = pillar_mediana(nums)

print(f"La mediana es: {med}")