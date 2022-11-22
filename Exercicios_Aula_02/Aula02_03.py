# Escreva um programa que leia um número real qualquer e mostre a sua porção inteira.

import math

N = float(input("Digite um valor do tipo real: "))
N2 = math.trunc(N)
print("A parte inteira de {} é {}.".format(N,N2))
