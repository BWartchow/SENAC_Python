#Escreva um programa que o computador pensará em um número entre 0 e 5.
# Em seguida, o usuário deverá adivinhar esse valor. Caso o usuário acerte, retorne “VENCEU”, caso perca, retorne “PERDEU”.

import random

num = random.randint(0,5)
num_user = int(input("Tente adivinhar o número entre 0 e 5 que o computador irá escolher: "))
print("VENCEU" if num_user == num else "PERDEU")
print(f"O número sorteado pelo computador foi {num}, você escolheu {num_user}")
