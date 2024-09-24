"""8. Crear una lista de números pares usando un bucle while:
Escribe un programa que genere una lista de números pares entre 1 y 100 usando un bucle
while.
"""

print("Generando pares entre 1 y 100")

pares = []

current_num = 1
while current_num < 100:
    if current_num % 2==0:
        pares.append(current_num)
    current_num+=1    
print(f"Pares entre 1 y 100: {pares}")        