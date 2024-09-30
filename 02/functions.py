def menu():
    print("\n--- Bienvenido al mercado de Don Pepito ---")
    print("\n--- Elija qué quiere hacer con el programa ---")
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Realizar venta")
    print("4. Guardar y salir")
    print("\n--- Seleccione una opción ingresando solamente el numero ---")
    return input("Opcion...: ")

def leer_inventario(inv_file, inventario):
    try:
        x =  open(f"{inv_file}.txt", "r")
        for line in x:
            nombre, precio, cantidad = line.strip().split(",")
            inventario[nombre] = {"precio": float(precio), "cantidad": int(cantidad)}
    except FileNotFoundError:
        print(f"El archivo {inv_file}.txt no existe. Se creará un nuevo inventario.")
    return inventario

def mostrar_inventario(inventario):
    print("\nInventario actual:")
    for nombre, datos in inventario.items():
        print(f"{nombre}: Precio: ${datos['precio']:.2f}, Cantidad: {datos['cantidad']}")
    print()

def actualizar_inventario(inventario, inv_file):
    with open(f"{inv_file}.txt", "w") as x:
        for nombre, datos in inventario.items():
            x.write(f"{nombre},{datos['precio']},{datos['cantidad']}\n")
    print("Inventario actualizado en el archivo.")

def agregar_producto(nombre, precio, cantidad, inventario):
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe. Se actualizará la cantidad.")
        inventario[nombre]['cantidad'] += cantidad
    else:
        inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
    print(f"Producto '{nombre}' agregado/actualizado en el inventario.")
    mostrar_inventario(inventario)

def realizar_venta(nombre, cantidad, inventario):
    if nombre not in inventario:
        print(f"El producto '{nombre}' no existe en el inventario.")
        return
    
    if inventario[nombre]['cantidad'] >= cantidad:
        inventario[nombre]['cantidad'] -= cantidad
        print(f"Venta realizada: {cantidad} unidades de '{nombre}'")
    else:
        print(f"No hay suficiente stock de '{nombre}'. Venta no realizada.")
    
    mostrar_inventario(inventario)