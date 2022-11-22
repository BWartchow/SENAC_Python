# Escreva um programa que leia o nome completo de uma pessoa e mostre:
# 1)	O nome com todas as letras maiúsculas;
# 2)	O nome com todas as letras minúsculas;
# 3)	Quantas l
# 4)	Quantas letras tem o primeiro nome.

nome = input("Nome Completo: ")
print("1) O nome com todas as letras maiúsculas:")
print(nome.upper())
print("2) O nome com todas as letras minúsculas:")
print(nome.lower())
print("3) Quantas letras ao todo (sem considerar os espaços):")
espacos = nome.count(" ")
apenasletras = (len(nome))
print(apenasletras-espacos)
print("4) Quantas letras tem o primeiro nome:")
primeiroEspaco = nome.find(" ")
print("Primeiro nome: {}".format(nome[:primeiroEspaco]))
numLetras = (primeiroEspaco)
print("Número de letras: {}".format(numLetras))
