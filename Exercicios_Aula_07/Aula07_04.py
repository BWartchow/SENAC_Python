# Escreva um programa que leia um número e calcule seu fatorial mostra da tela como exemplo a seguir.
# 5! = 5x4x3x2x1 = 120

import math
texto = "FATORAÇÃO"
print(f"{texto:^20}")
n = int(input("Digite um número inteiro : "))
while n <= 0:
    print("Não existe fatorial de números negativos ou de zero!")
    n = int(input("Digite outro número inteiro : "))

fatorial = math.factorial(n)
i = n
print (f"{n}! = ", end=' ')
while i > 1:
    print (f"{i} x ", end=' ')
    i -= 1
    if i == 1:
        print(f"{i} = {fatorial}")
print("fim")
