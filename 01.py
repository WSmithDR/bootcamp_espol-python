"""1. Análisis de una frase
Crea una función llamada `analizar_frase` que reciba una cadena y realice las siguientes
operaciones:
1. Convierte la frase a mayúsculas.
2. Cuenta cuántas veces aparece la letra 'a' y devuelve el resultado.
3. Reemplaza todas las vocales por el símbolo `*` y devuelve la nueva cadena.
4. Verifica si la frase es un palíndromo."""

def analizar_frase(frase):
    vocales = ["a","e","i","o","u"]
    aMayuscula = frase.upper()
    aS = frase.count("a")
    for i in frase:
        if i in vocales:
            vocales.replace(i,"*")