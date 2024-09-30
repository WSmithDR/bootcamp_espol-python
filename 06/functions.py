def menu():
    print("\n--- Sistema de Gestión de Ventas ---")
    print("1. Agregar venta")
    print("2. Calcular total de ventas")
    print("3. Mostrar producto con más ventas")
    print("4. Guardar y salir")
    print("\n--- Solo escribir el numero de la opcion ---")
    return input("Seleccione una opción: ")

def cargar_ventas(archivo):
    ventas = {}
    try:
        with open(archivo, 'r') as f:
            for linea in f:
                producto, cantidad, precio = linea.strip().split(',')
                if producto in ventas:
                    ventas[producto]['cantidad'] += int(cantidad)
                    ventas[producto]['total'] += int(cantidad) * float(precio)
                else:
                    ventas[producto] = {'cantidad': int(cantidad), 'total': int(cantidad) * float(precio)}
    except FileNotFoundError:
        print("Archivo de ventas no encontrado. Se iniciará con un sistema vacío.")
    return ventas

def agregar_venta(ventas, producto, cantidad, precio):
    if producto in ventas:
        ventas[producto]['cantidad'] += cantidad
        ventas[producto]['total'] += cantidad * precio
    else:
        ventas[producto] = {'cantidad': cantidad, 'total': cantidad * precio}
    print(f"Venta agregada: {cantidad} unidades de {producto} a ${precio:.2f} cada una.")

def calcular_total_ventas(ventas):
    total = sum(producto['total'] for producto in ventas.values())
    print(f"El total de ventas de todos los productos es: ${total:.2f}")

def producto_mas_vendido(ventas):
    if not ventas:
        print("No hay ventas registradas.")
        return
    producto_max = max(ventas, key=lambda x: ventas[x]['cantidad'])
    print(f"El producto con más ventas es: {producto_max}")
    print(f"Cantidad vendida: {ventas[producto_max]['cantidad']}")
    print(f"Total generado: ${ventas[producto_max]['total']:.2f}")

def guardar_ventas(ventas, archivo):
    with open(archivo, 'w') as f:
        for producto, info in ventas.items():
            f.write(f"{producto},{info['cantidad']},{info['total'] / info['cantidad']:.2f}\n")