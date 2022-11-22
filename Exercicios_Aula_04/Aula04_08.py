#Escreva um programa que leia três números e mostre qual é o maior e qual é o menor.

N1 = int(input("Digite o primeiro número (inteiro): "))
maior = N1
menor = N1
N2 = int(input("Digite o segundo número (inteiro): "))
if N2 > N1:
    maior = N2
if N2 < N1:
    menor = N2
N3 = int(input("Digite o terceiro número (inteiro): "))
if N3 > N1 and N3 > N2:
    maior = N3
if N3 < N1 and N3 < N2:
    menor = N3
print(f"Você escolheu os números {N1}, {N2} e {N3}. O maior deles é o {maior} e o menor é o {menor}")


