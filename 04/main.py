"""4. Operaciones con listas y tuplas
Escribe una función llamada `procesar_lista` que reciba una lista de números enteros. La
función debe devolver:
1. La lista ordenada.
2. La tupla de números únicos (usando un conjunto).
3. La suma de todos los números pares de la lista."""

def procesar_lista(nums):
    sortedNums = nums.sort()
    uniqueNums = tuple(set(nums))
    parNums = [num for num in nums if num%2==0]
    sumParNums = sum(parNums)
    return {
        "Sorted list":sortedNums,
        "Unique Nums":uniqueNums,
        "Sum pair nums": sumParNums
        }
numeros = [12, 45, 67, 23, 89, 34, 56, 78, 90, 15]

lista_procesada = procesar_lista(numeros)

print(lista_procesada)