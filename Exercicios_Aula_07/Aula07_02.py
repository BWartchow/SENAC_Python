# Escreva um programa que o computador vai “pensar” em um número inteiro entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar o número,
# mostrando no final quantos palpites foram necessários para vencer.

import random

maquina = random.randint(0,10)
# print(maquina)
tentativa = 0
user = int(input('Tente adivinhar o valor sorteado entre 0 e 10: '))
while user > 10 or user < 0:
    user = int(input('Preste atenção no intervalo, faça um palpite entre 0 e 10: '))
    tentativa += 1
    while maquina != user:
        user = int(input('Errou :( Faça outro palpite entre 0 e 10: '))
        tentativa += 1
        while user > 10 or user < 0:
            user = int(input('Preste atenção no intervalo, faça um palpite entre 0 e 10: '))
            tentativa += 1
    if user == maquina:
        print("-"*35)
        print(f"Você escolheu {user}!\nParabéns, você acertou! O número sorteado era {maquina}.")
        tentativa += 1
        print(f"Acertou com {tentativa} palpite(s)!")
