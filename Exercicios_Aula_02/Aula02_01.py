# Escreva um programa que leia um número do usuário e mostre a raíz quadrada desse número e arredonde para cima esse número se for necessário.

import math

N = float(input("Digite um numero: "))
print("A raiz de {} vale {}.".format(N,math.sqrt(N)))
print("O arredondamento superior dessa raiz vale {}.".format(math.ceil(math.sqrt(N))))
print("O arredondamento inferior dessa raiz vale {}.".format(math.floor(math.sqrt(N))))

