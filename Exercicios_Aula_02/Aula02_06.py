# Escreva um programa que leia  o nome de quatro alunos e sorteie aleatóriamente um deles,  mostrando o nome na tela.
# Escreva um prorgama que leia o nome de 4 alunos e coloque eles em uma ordem aleatória, monstrando essa ordem na tela.
import random

a1 = input("1o aluno: ")
a2 = input("2o aluno: ")
a3 = input("3o aluno: ")
a4 = input("4o aluno: ")

nomes = [a1,a2,a3,a4]
random.shuffle(nomes)
escolhido = random.choice([a1,a2,a3,a4])

print("Alunos: {}\nO escolhido foi: {}".format(nomes,escolhido))
