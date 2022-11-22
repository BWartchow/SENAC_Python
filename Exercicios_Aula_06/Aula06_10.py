# Escreva um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lidos.

peso1 = float(input("Digite o 1° peso em kg: "))
maior = peso1
menor = peso1

for c in range (2,6):
    peso = float(input(f"Digite o {c}° peso em kg: "))
    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print("-"*35)
print(f"O maior peso lido foi {maior:.2f}kg e o menor foi {menor:.2f}kg.")
