inventario = {}

def mostrar_inventario():
    print("\nInventario actual:")
    for nombre, datos in inventario.items():
        print(f"{nombre}: Precio: ${datos['precio']}, Cantidad: {datos['cantidad']}")
    print()

def agregar_producto(nombre, precio, cantidad):
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe. Se actualizará la cantidad.")
        inventario[nombre]['cantidad'] += cantidad
    else:
        inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
    print(f"Producto '{nombre}' agregado/actualizado en el inventario.")
    mostrar_inventario()

def realizar_venta(nombre, cantidad):
    if nombre not in inventario:
        print(f"El producto '{nombre}' no existe en el inventario.")
        return
    
    if inventario[nombre]['cantidad'] >= cantidad:
        inventario[nombre]['cantidad'] -= cantidad
        print(f"Venta realizada: {cantidad} unidades de '{nombre}'")
    else:
        print(f"No hay suficiente stock de '{nombre}'. Venta no realizada.")
    
    mostrar_inventario()

agregar_producto("Laptop", 1000, 5)
agregar_producto("Teléfono", 500, 10)
realizar_venta("Laptop", 2)
realizar_venta("Teléfono", 3)
agregar_producto("Laptop", 1000, 3)
realizar_venta("Tablet", 1)