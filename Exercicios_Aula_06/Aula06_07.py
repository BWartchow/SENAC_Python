# Escreva um programa que leia um número inteiro e diga se ele é primo ou não.

n = int(input("Digite um número inteiro: "))
p = 0
for contador in range (1,n+1):
    if n % contador == 0:
        p += 1
        print(f"\033[33m{contador}\033[33m",end="  ")
    else:
        print(f"\033[30m{contador}\033[30m",end="  ")
print("")
print("\033[031mÉ PRIMO\033[031m" if p == 2 else "\033[031mNÃO\033[031m \033[mÉ\033[m \033[034mPRIMO\033[034m")

