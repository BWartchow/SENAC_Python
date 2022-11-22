# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
# 1) “O primeiro valor é maior”
# 2) “O segundo valor é maior”
# 3) “Não existe valor maior, ambos são iguais”

N1 = int(input("Digite o primeiro valor (número inteiro): "))
N2 = int(input("Digite o segundo valor (número inteiro): "))

if N1 > N2:
    print(f"O primeiro valor, {N1}, é maior que o segundo, {N2}.")
elif N2 > N1:
    print(f"O segundo valor, {N2}, é maior que o primeiro, {N1}.")
elif N2 == N1:
    print(f"Não existe valor maior, {N1} e {N2} são iguais.")
