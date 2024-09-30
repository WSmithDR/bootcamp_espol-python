"""9. Procesamiento de datos en listas
Escribe una función llamada `procesar_datos` que reciba una lista de tuplas, donde cada
tupla contiene el nombre de un producto, su precio y cantidad vendida. La función debe
devolver:
1. El total de ingresos generados.
2. El producto más vendido.
3. El producto con mayor ingreso."""

def obtener_total_ingresos(lista_tuplas):
    total = 0
    for producto in lista_tuplas:
        total += producto[1] * producto[2]
    return total

def obtener_producto_mas_vendido(lista_tuplas):
    max_cantidad = 0
    producto_mas_vendido = ""
    for producto in lista_tuplas:
        nombre, _, cantidad = producto
        if cantidad > max_cantidad:
            max_cantidad = cantidad
            producto_mas_vendido = nombre
    return producto_mas_vendido

def obtener_producto_mayor_ingreso(lista_tuplas):
    max_ingreso = 0
    producto_mayor_ingreso = ""
    for producto in lista_tuplas:
        nombre, precio, cantidad = producto
        ingreso = precio * cantidad
        if ingreso > max_ingreso:
            max_ingreso = ingreso
            producto_mayor_ingreso = nombre
    return producto_mayor_ingreso

def procesar_datos(lista_tuplas):
    total_ingresos = obtener_total_ingresos(lista_tuplas)
    producto_mas_vendido = obtener_producto_mas_vendido(lista_tuplas)
    producto_mayor_ingreso = obtener_producto_mayor_ingreso(lista_tuplas)
    
    return (
        total_ingresos,
        producto_mas_vendido,
        producto_mayor_ingreso
    )

datos_ventas = [
        ("Producto A", 10.0, 50),
        ("Producto B", 15.0, 30),
        ("Producto C", 5.0, 100),
        ("Producto D", 20.0, 25)
    ]
    
total, mas_vendido, mayor_ingreso = procesar_datos(datos_ventas)
    
print(f"Total de ingresos generados: ${total:.2f}")
print(f"Producto más vendido: {mas_vendido}")
print(f"Producto con mayor ingreso: {mayor_ingreso}")