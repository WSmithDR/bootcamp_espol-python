def menu():
    print("\n--- Sistema de Reserva de Vuelos ---")
    print("1. Agregar vuelo")
    print("2. Reservar asientos")
    print("3. Mostrar información de un vuelo")
    print("4. Guardar y salir")
    print("\n--- Solo escribir el numero de la opcion ---")
    return input("Seleccione una opción: ")

def cargar_vuelos(archivo):
    vuelos = {}
    try:
        f = open(archivo, 'r')
        for linea in f:
            codigo, asientos, precio = linea.strip().split(',')
            vuelos[codigo] = {"asientos_disponibles": int(asientos), "precio": float(precio)}
    except FileNotFoundError:
        print("Archivo de vuelos no encontrado. Se iniciará con un sistema vacío.")
    return vuelos

def agregar_vuelo(vuelos, codigo, asientos, precio):
    if codigo in vuelos:
        print(f"El vuelo con código {codigo} ya existe.")
        return
    vuelos[codigo] = {"asientos_disponibles": asientos, "precio": precio}
    print(f"Vuelo {codigo} agregado con éxito.")

def reservar_asientos(vuelos, codigo, cantidad):
    if codigo not in vuelos:
        print(f"El vuelo con código {codigo} no existe.")
        return
    if vuelos[codigo]["asientos_disponibles"] >= cantidad:
        vuelos[codigo]["asientos_disponibles"] -= cantidad
        print(f"Reserva exitosa. {cantidad} asiento(s) reservado(s) para el vuelo {codigo}.")
    else:
        print(f"No hay suficientes asientos disponibles en el vuelo {codigo}.")

def mostrar_info_vuelo(vuelos, codigo):
    if codigo not in vuelos:
        print(f"El vuelo con código {codigo} no existe.")
        return
    vuelo = vuelos[codigo]
    print(f"Información del vuelo {codigo}:")
    print(f"Asientos disponibles: {vuelo['asientos_disponibles']}")
    print(f"Precio: ${vuelo['precio']:.2f}")

def guardar_vuelos(vuelos, archivo):
    with open(archivo, 'w') as f:
        for codigo, info in vuelos.items():
            f.write(f"{codigo},{info['asientos_disponibles']},{info['precio']}\n")