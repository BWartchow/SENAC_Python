#Escreva um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome separadamente.

nome = input("Digite seu nome completo: ")
print("Nome: {}".format(nome))
print("Primeiro nome: {}".format(nome.split()[0]))
print("Último nome: {}".format(nome.split()[-1]))
