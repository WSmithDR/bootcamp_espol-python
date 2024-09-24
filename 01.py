"""1. Comprobar si una palabra es un palíndromo:
Escribe un programa que solicite una palabra al usuario y verifique si es un palíndromo
(una palabra que se lee igual de adelante hacia atrás).
"""
def is_palindrome(word):
  word = word.lower()
  return word==word[::-1]

word = input("Try a word: ")

print(is_palindrome(word))