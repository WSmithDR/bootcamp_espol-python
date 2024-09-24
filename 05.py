"""5. Contar vocales en una frase:
Escribe un programa que solicite una frase al usuario y cuente cuántas vocales hay en la
frase. Usa un conjunto para almacenar las vocales."""

def contar_vocales(frase):
    vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}
    for i in frase:
        if i in vocales.keys():
            vocales[i]+=1
    return vocales 

frase = input("Ingresa alguna frase: ")

print(contar_vocales(frase))
