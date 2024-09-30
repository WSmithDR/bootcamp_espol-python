"""10. Combinación de conjuntos y funciones
Crea un programa que permita a los usuarios gestionar dos conjuntos de datos. Debe haber
funciones para:
1. Encontrar la unión, intersección y diferencia de dos conjuntos.
2. Permitir agregar y eliminar elementos de los conjuntos.
3. Mostrar el conjunto resultante después de cada operación."""

import functions as fn

ARCHIVO_DATOS = "10/conjuntos.txt"


conjunto1, conjunto2 = fn.cargar_conjuntos(ARCHIVO_DATOS)

while True:
    opcion = fn.menu()
    if opcion == "1":
        print("Conjunto 1:")
        fn.mostrar_conjunto(conjunto1)
        print("Conjunto 2:")
        fn.mostrar_conjunto(conjunto2)
        
    if opcion == "2":
        resultado = fn.union_conjuntos(conjunto1, conjunto2)
        print("Unión de conjuntos:")
        fn.mostrar_conjunto(resultado)
        
    if opcion == "3":
        resultado = fn.interseccion_conjuntos(conjunto1, conjunto2)
        print("Intersección de conjuntos:")
        fn.mostrar_conjunto(resultado)
        
    if opcion == "4":
        resultado = fn.diferencia_conjuntos(conjunto1, conjunto2)
        print("Diferencia de conjuntos (1-2):")
        fn.mostrar_conjunto(resultado)
        
    if opcion == "5":
        conjunto_num = input("¿A qué conjunto desea agregar (1 o 2)? ")
        elemento = input("Ingrese el elemento a agregar: ")
        if conjunto_num == "1":
            fn.agregar_elemento(conjunto1, elemento)
        if conjunto_num == "2":
            fn.agregar_elemento(conjunto2, elemento)
        else:
            print("Opción no válida")
        
    if opcion == "6":
        conjunto_num = input("¿De qué conjunto desea eliminar (1 o 2)? ")
        elemento = input("Ingrese el elemento a eliminar: ")
        if conjunto_num == "1":
            fn.eliminar_elemento(conjunto1, elemento)
        if conjunto_num == "2":
            fn.eliminar_elemento(conjunto2, elemento)
        else:
            print("Opción no válida")
        
    if opcion == "7":
        fn.guardar_conjuntos(conjunto1, conjunto2, ARCHIVO_DATOS)
        print("Conjuntos guardados. ¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, intente de nuevo.")