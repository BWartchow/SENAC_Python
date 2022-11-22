# Escreva um programa que faça a contagem regressiva de 10 até 0 com uma pausa de 1 segundo entre eles.

import time

for contador in range (10,-1,-1):
    print("Contando...")
    time.sleep(1)
    print(contador)
print("Fim!")
