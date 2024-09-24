"""9. Contar las veces que un elemento aparece en una tupla:
Solicita al usuario que ingrese una lista de números y conviértela en una tupla. Luego, pide
un número y cuenta cuántas veces aparece en la tupla.
"""
jugar = True
nums = []    
while jugar:
    if len(nums) == 0:
        print("Empecemos creando una tupla****")
        nums = input("Numeros: ").split()
        nums = tuple(int(num) for num in nums)
        print("Escribe un numero para ver cuantas veces esta en la tupla")
        num = int(input("Numero: "))
        print(f"{num} aparece {nums.count(num)} vez/veces") 
    else:
        ops = ["1. Crear tupla numerica","2. Explorar tupla existente", "3. Salir"]
        for op in ops:
            print(op)
        print("*********")
        res = input("Respuesta (1, 2 o 3): ")
        if res == "1":
            nums = []
        if res == "3":
            print("Saliendo...")
            jugar = False    
        if res == "2":
            print("Escribe un numero para ver cuantas veces esta en la tupla")
            num = int(input("Numero: "))
            print(f"{num} aparece {nums.count(num)} vez/veces") 