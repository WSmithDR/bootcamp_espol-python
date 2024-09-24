"""2. Clasificar números en una lista:
Pide al usuario que ingrese una lista de números y clasifícalos en tres listas: números pares,
números impares y múltiplos de 3."""

activate = True
nums = []
while activate:
    print("Enter a number...")
    num = input("Number: ")
    nums.append(int(num))
    print("Do you wanna enter another number? yes/no")
    res = input("Response: ")
    if res == "no":
        activate = False

print("Clasifying numbers...")

def es_par(num):
    return num%2==0

def es_impar(num):
    return num%2!=0

def es_multiplo_de_tres(num):
    return num%3==0

for num in nums:
    par = es_par(num)
    impar = es_impar(num)
    x3 = es_multiplo_de_tres(num)
    if par:
        print(f"{num} es par.")
    if impar:
        print(f"{num} es impar.")
    if x3:
        print(f"{num} es multiplo de 3.")        