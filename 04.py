## Ejercicio 4: Ordenar lista de números
"""Crea un programa que pida al usuario 5 números y los imprima en orden ascendente."""

def ordenar_cinco_numeros():
    nums = []
    n = range(5)
    for i in n:
        print(f"Faltan {len(n)-i}")
        num = float(input("Ingresa un numero: "))
        nums.append(num)

    nums.sort()
    return nums

sorted_nums = ordenar_cinco_numeros()
print(f"Numeros ordenados: {sorted_nums}")    
