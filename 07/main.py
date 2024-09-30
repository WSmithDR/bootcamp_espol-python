""""7. Validación de datos de usuarios
Escribe una función `validar_usuarios` que reciba un diccionario donde las claves sean
nombres de usuario y los valores sean contraseñas. La función debe:
1. Verificar si una contraseña es válida (mínimo 8 caracteres).
2. Devolver una lista con los nombres de usuarios que tienen contraseñas válidas."""

def validar_usuarios(usuarios):
    usuarios_validos = []
    for nombre, clave in usuarios.items():
        if len(clave) >= 8:
            usuarios_validos.append(nombre)
    return usuarios_validos


ejemplos = {
        "usuario1": "contraseña123",
        "usuario2": "clave",
        "usuario3": "segura1234",
        "usuario4": "12345678"
}


usuarios_validados = validar_usuarios(ejemplos)


print("Usuarios con contraseñas válidas:")
for usuario in usuarios_validados:
    print(usuario)