# Escreva um programa que leia vários números.
# No final, mostre a média entre todos os valores e qual foi o maior e o menor valores lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resposta = 'S'
total = soma = media = 0

N = int(input("Digite um número: "))
menor = maior = N
total += 1
soma += N
resposta = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
while resposta not in "SN":
    resposta = str(input("Resposta inválida. Digite novamente [S/N]: ")).upper().strip()[0]

while resposta == 'S':
    N = int(input("Digite um número: "))
    resposta = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while resposta not in "SN":
        resposta = str(input("Resposta inválida. Digite novamente [S/N]: ")).upper().strip()[0]
    total += 1
    soma += N
    if N < menor:
        menor = N
    if N > maior:
        maior = N


print("\nEncerrando...")
print(f"Você digitou {total} números.\nA soma foi {soma} e a média foi {(soma/total):.2f}.\nO maior número foi {maior} e o menor foi {menor}.")
