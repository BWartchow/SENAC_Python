# Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros números da Sequência de Fibonacci da seguinte forma mostrada a seguir.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
txt = "Bem vindo à SEQUÊNCIA DE FIBONACCI!"
print(f"{txt:^45}")
termo = int(input("Digite quantos termos você quer exibir: "))
c = t = f = 0
i = 1
print(f"{t} \033[031m->\033[m {i} \033[031m->\033[m ", end='')
while c < termo-2:
    f = i + t
    t = i
    i = f
    if c == termo-3:
        print(f"{f}", end='')
    else:
        print(f"{f} \033[031m->\033[m ", end='')
    c += 1
