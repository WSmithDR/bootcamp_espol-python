"""4. Verificar elementos únicos en una lista usando conjuntos:
Escribe un programa que verifique si todos los elementos en una lista ingresada por el
usuario son únicos, utilizando un conjunto.
"""

text = input("Escribe cualquier cosa: ")

elements = text.split()

print("Verificando unicidad de los elementos ingresados")

if elements == list(set(elements)):
    print("Existe unicidad de elementos")
else:
    print("Hay elementos repetidos")