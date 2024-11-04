## Ejercicio 2: Palabras más largas
"""Escribe un programa que tome una oración del usuario y muestre la palabra más larga que contiene.
"""
def get_longest_word(txt):
    if(any(char.isdigit() for char in txt)): return "No se permiten numeros en este ejercicio, mi rey"
    else: 
        words = txt.split()
        words_length = list(map(lambda word:len(word),words))
        index = words_length.index(max(words_length))
        return words[index]

print("Escribe una oracion a continaucion para pillar la palabra mas larga")
input_txt = input("...: ")

longest_word = get_longest_word(input_txt)

print(f"La palabra mas large es: {longest_word}")