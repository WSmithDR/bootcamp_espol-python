# Taller Data Science

## Ejercicio 1: Normalización de datos
"""Dada la lista de valores:
valores = [10, 20, 30, 40, 50]
Crea un programa que normalice los valores dividiendo cada elemento por el máximo valor en la lista.
"""
valores = [10, 20, 30, 40, 50]
def normalizador(_list):
    if not all(isinstance(num, (int, float)) for num in _list):
        return "Uno de los elementos no es un numero"
    else:
        _max = max(_list)
        return [num/_max for num in _list]

print(normalizador(valores))    
print(normalizador(valores+[""]))    