"""7. Filtrar palabras largas de una lista:
Solicita al usuario que ingrese una lista de palabras y un número límite. Filtra y muestra
solo las palabras que tengan más caracteres que el límite."""

print("Este juego filtra las palabras que contengan mas caracteres del que vas a indicar a continuacion******")
n = int(input("Cnatidad limite de caracteres: "))
print("Ahora ingreza una frase o una lista de palabras...")
palabras = input("Aquí: ").split()

print("Pillando las palabras filtradas....")
for palabra in palabras:
    if len(palabra) > n:
        print(palabra)

if all(len(palabra)<= n for palabra in palabras):
    print("Ninguna palabra paso la prueba...")