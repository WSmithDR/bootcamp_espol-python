"""6. Análisis de ventas con funciones y diccionarios
Crea un programa que gestione las ventas de una tienda. Debes tener:
1. Una función para agregar ventas al sistema, donde se registra el nombre del producto, la
cantidad vendida y el precio.
2. Una función para calcular el total de ventas de todos los productos.
3. Una función que muestre el producto con más ventas."""

import functions as fn

archivo_ventas = "06/ventas.txt"
ventas = fn.cargar_ventas(archivo_ventas)

while True:
    opcion = fn.menu()
    
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad vendida: "))
        precio = float(input("Ingrese el precio unitario: "))
        fn.agregar_venta(ventas, producto, cantidad, precio)
    
    elif opcion == "2":
        fn.calcular_total_ventas(ventas)
    
    elif opcion == "3":
        fn.producto_mas_vendido(ventas)
    
    elif opcion == "4":
        fn.guardar_ventas(ventas, archivo_ventas)
        print("Ventas guardadas. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, intente de nuevo.")