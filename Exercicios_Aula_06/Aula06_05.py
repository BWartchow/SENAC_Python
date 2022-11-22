# Escreva um programa que leia 6 números inteiros do usuário e mostre a soma apenas daqueles que forem pares,
# Se o valor for ímpar, desconsidere-o.

soma = 0
for c in range (1,7):
    n = int(input(f"Digite o {c}° número inteiro: "))
    if n%2==0:
        soma += n
print(f"A soma dos números pares é {soma}!")
