"""3. Crear una tupla de números cuadrados:
Solicita al usuario que ingrese una lista de números. Luego, genera una tupla que contenga
los cuadrados de esos números.
"""

activar = True
nums = []
while activar:
    num = float(input("Ingresa un numero: "))
    nums.append(num)
    print("Quieres ingresar otro numero? yes/no")
    res = input("yes/no: ")
    if res == "no":
        activar = False

print("Generando tupla de los cuadraros que ingresaste...")

print(f"Original: {tuple(nums)}")
print(f"Cuadrados: {tuple(num**2 for num in nums)}")