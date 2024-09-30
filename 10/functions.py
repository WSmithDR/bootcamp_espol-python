def menu():
    print("\n--- Gestión de Conjuntos ---")
    print("1. Mostrar conjuntos")
    print("2. Unión de conjuntos")
    print("3. Intersección de conjuntos")
    print("4. Diferencia de conjuntos")
    print("5. Agregar elemento a un conjunto")
    print("6. Eliminar elemento de un conjunto")
    print("7. Guardar y salir")
    return input("Seleccione una opción: ")

def union_conjuntos(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def interseccion_conjuntos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

def diferencia_conjuntos(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

def agregar_elemento(conjunto, elemento):
    conjunto.add(elemento)

def eliminar_elemento(conjunto, elemento):
    conjunto.discard(elemento)

def mostrar_conjunto(conjunto):
    print(conjunto)

def guardar_conjuntos(conjunto1, conjunto2, archivo):
    with open(archivo, 'w') as f:
        f.write(','.join(conjunto1) + '\n')
        f.write(','.join(conjunto2))

def cargar_conjuntos(archivo):
    conjunto1 = set()
    conjunto2 = set()
    try:
        f = open(archivo, 'r')
        lineas = f.readlines()
        if len(lineas) >= 1:
            conjunto1 = set(lineas[0].strip().split(','))
        if len(lineas) >= 2:
            conjunto2 = set(lineas[1].strip().split(','))
    except FileNotFoundError:
        print("Archivo no encontrado. Se iniciarán conjuntos vacíos.")
    return conjunto1, conjunto2