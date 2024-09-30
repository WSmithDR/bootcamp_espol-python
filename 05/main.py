"""5. Sistema de reserva de vuelos
Crea un sistema modularizado para la reserva de vuelos. Cada vuelo tiene un código, una
cantidad de asientos disponibles y un precio. Las funciones deben:
1. **Agregar vuelos** al sistema.
2. **Reservar asientos**, que actualiza la cantidad disponible.
3. **Mostrar información de un vuelo** en cualquier momento.
"""

import functions as fn

archivo_vuelos = "05/vuelos.txt"
vuelos = fn.cargar_vuelos(archivo_vuelos)

while True:
    opcion = fn.menu()
        
    if opcion == "1":
        codigo = input("Ingrese el código del vuelo: ")
        asientos = int(input("Ingrese la cantidad de asientos disponibles: "))
        precio = float(input("Ingrese el precio del vuelo: "))
        fn.agregar_vuelo(vuelos, codigo, asientos, precio)
        
    if opcion == "2":
        codigo = input("Ingrese el código del vuelo: ")
        cantidad = int(input("Ingrese la cantidad de asientos a reservar: "))
        fn.reservar_asientos(vuelos, codigo, cantidad)
        
    if opcion == "3":
        codigo = input("Ingrese el código del vuelo: ")
        fn.mostrar_info_vuelo(vuelos, codigo)
        
    if opcion == "4":
        fn.guardar_vuelos(vuelos, archivo_vuelos)
        print("Vuelos guardados. ¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, intente de nuevo.")