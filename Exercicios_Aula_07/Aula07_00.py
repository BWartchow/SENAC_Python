# Escreva um programa que o usuário escreverá quantos números ele quiser.
# No final, mostre quantos valores pares e impares foram digitados ao total.

par = impar = 0
resposta = 'S'
while resposta == 'S':
    valor = int(input("Digite um número inteiro: "))
    if valor%2 == 0:
        par += 1
    else:
        impar += 1
    resposta = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while resposta not in 'SN':
    # while resposta != 'S' and resposta != 'N':
        resposta = str(input("Resposta inválida. Digite novamente: [S/N] ")).upper().strip()[0]

print("-"*35)
print(f"Você digitou {par} números pares;\nVocê digitou {impar} números ímpares.")
