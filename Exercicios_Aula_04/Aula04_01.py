# Escreva um programa que leia a idade do user e diga se ele é maior de idade ou menor de idade.

idade = int(input("Qual a sua idade? "))
print("Você disse ter {} anos".format(idade))
#if idade >= 18:
    #print("Você é maior de idade!")
#else:
    #print("Você é menor de idade ainda...")

print("Você é maior de idade" if idade >= 18 else "Você é menor de idade ainda...")
