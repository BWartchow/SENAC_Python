# Escreva um programa que leia vários números inteiros e só pare quando o usuário digitar o valor 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# USE WHILE TRUE

quantidade = soma = 0

while True:
    n = int(input("Digite um número inteiro ou 999 para sair: "))
    if n == 999:
        break
    quantidade += 1
    soma += n

print(f"\nVocê digitou {quantidade} números.\nA soma entre eles deu {soma}.")
