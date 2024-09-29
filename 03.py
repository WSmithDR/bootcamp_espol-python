"""3. Estadísticas de calificaciones
Crea una función llamada `calcular_estadisticas` que reciba un diccionario de estudiantes y
sus calificaciones. La función debe devolver:
1. La calificación más alta.
2. La calificación más baja.
3. El promedio de las calificaciones."""

def calcular_promedio(lista_numerica):
    if len(lista_numerica) == 0:
        return 0 
    return sum(lista_numerica) / len(lista_numerica)


def calcular_estadisticas(calificaciones):
    info = {}
    for estudiante, notas in calificaciones.items():
        info[estudiante] = {}  # Crear un diccionario para cada estudiante
        info[estudiante]["Calificacion maxima"] = max(notas)
        info[estudiante]["Calificacion minima"] = min(notas)
        info[estudiante]["Calificacion promedio"] = calcular_promedio(notas)
    return info       


calificaciones_estudiantes = {
    'Ana': [85, 90, 78],
    'Luis': [88, 92, 79],
    'Maria': [95, 87, 91],
    'Carlos': [70, 85, 89],
    'Lucia': [92, 94, 88]
}

info = calcular_estadisticas(calificaciones_estudiantes)

for est, dic in info.items():
    print(f"Estudiante: {est}: Info: {dic}")