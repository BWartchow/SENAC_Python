# Escreva um programa que leia vários números inteiros e só pare quando o usuário digitar o valor 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.

quant = soma = n = 0

while n != 999:
    n = int(input("Digite um número [ou 999 para sair]: "))
    quant += 1
    soma += n

print(f"\nVocê digitou {quant-1} números. \nA soma entre eles é {soma-999}.")
