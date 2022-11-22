# Escreva um programa que retorne um número aleatório inteiro entre dois extremos escolhidos pelo usuário.

import random
N1 = int(input("Número de início: "))
N2 = int(input("Número de fim: "))
print("Número gerado entre estes: {}".format(random.randint(N1,N2)))
