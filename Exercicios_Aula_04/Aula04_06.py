#Escreva um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

N = int(input("Digite um número inteiro: "))
print(f"Você escolheu {N}:")
print("Este número é PAR" if N%2==0 else "Este número é ÍMPAR")
