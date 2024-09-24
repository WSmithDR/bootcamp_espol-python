"""6. Encontrar el número más grande en una lista:
Escribe un programa que pida al usuario que ingrese una lista de números y luego
determine cuál es el número más grande usando un bucle.
"""

print("******Ingresa varios numeros, procura seprarlos por espacio******")
nums = input("Numeros: ").split()
nums = [float(num) for num in nums]
print("Localizando al numero mas grande....")

largest_num = nums[0]
for i in range(1,len(nums)):
    if nums[i]>largest_num:
        largest_num = nums[i]

print(f"{largest_num} fue el numero mas grande que ingresaste...")