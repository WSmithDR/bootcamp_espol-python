"""1. Análisis de una frase
Crea una función llamada `analizar_frase` que reciba una cadena y realice las siguientes
operaciones:
1. Convierte la frase a mayúsculas.
2. Cuenta cuántas veces aparece la letra 'a' y devuelve el resultado.
3. Reemplaza todas las vocales por el símbolo `*` y devuelve la nueva cadena.
4. Verifica si la frase es un palíndromo."""

def analizar_frase(frase):
    frase_mayusculas = frase.upper()
    conteo_a = frase_mayusculas.count('A')
    vocales = 'AEIOU'
    frase_sin_vocales = ''.join(['*' if c in vocales else c for c in frase_mayusculas])
    
    frase_sin_espacios = ''.join(c.lower() for c in frase)
    es_palindromo = frase_sin_espacios == frase_sin_espacios[::-1]
    
    return {
        'frase_mayusculas': frase_mayusculas,
        'conteo_a': conteo_a,
        'frase_sin_vocales': frase_sin_vocales,
        'es_palindromo': es_palindromo
    }


frase_ejemplo = "Anita lava la tina"
resultado = analizar_frase(frase_ejemplo)
    
print(f"Frase original: {frase_ejemplo}")
print(f"En mayúsculas: {resultado['frase_mayusculas']}")
print(f"Cantidad de 'A's: {resultado['conteo_a']}")
print(f"Sin vocales: {resultado['frase_sin_vocales']}")
print(f"Es palíndromo: {'Sí' if resultado['es_palindromo'] else 'No'}")