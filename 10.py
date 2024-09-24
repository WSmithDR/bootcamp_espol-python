import subprocess

def ejecutar_archivo(nombre):
    try:
        subprocess.run(["python", nombre], check=True)
    except subprocess.CalledProcessError:
        print(f"Error al ejecutar {nombre}")

while True:
    print("\nMenú de opciones:")
    print("1. Ejecutar 01.py")
    print("2. Ejecutar 02.py")
    print("3. Ejecutar 03.py")
    print("4. Ejecutar 04.py")
    print("5. Ejecutar 05.py")
    print("6. Ejecutar 06.py")
    print("7. Ejecutar 07.py")
    print("8. Ejecutar 08.py")
    print("9. Ejecutar 09.py")
    print("10. Ejecutar 10.py")
    print("11. Salir")

    opcion = input("Elige una opción (1-11): ")

    if opcion == "11":
        print("Saliendo...")
        break
    elif opcion in [str(i) for i in range(1, 11)]:
        archivo = f"{int(opcion):02d}.py"
        ejecutar_archivo(archivo)
    else:
        print("Opción no válida. Por favor, elige un número entre 1 y 11.")