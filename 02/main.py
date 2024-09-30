"""
2. Gestión de inventario de productos
Crea un sistema modular donde se gestionen productos de un inventario. Debes crear
funciones para:
1. **Agregar productos** al inventario, donde cada producto tiene un nombre, precio y
cantidad.
2. **Realizar una venta**, que reduce la cantidad en el inventario si hay suficiente stock.
3. **Mostrar el inventario** actualizado después de cada operación.
"""

import functions as fn

inventario = {}
inv_file = "02/inventario"
inventario = fn.leer_inventario(inv_file, inventario)

while True:
    opcion = fn.menu()
        
    if opcion == "1":
        fn.mostrar_inventario(inventario)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        fn.agregar_producto(nombre, precio, cantidad, inventario)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))
        fn.realizar_venta(nombre, cantidad, inventario)
    elif opcion == "4":
        fn.actualizar_inventario(inventario, inv_file)
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
