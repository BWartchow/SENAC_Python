# Escreva um programa que melhore o exercício 5, perguntando se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

txt = "PROGRESSÃO ARITMÉTICA:"
print("-"*40)
print(f"{txt:^40}")
print("-"*40)

razao = int(input("Qual será a razão da progressão? "))
termo = int(input("Digite o primeiro termo da progressão: "))

c = soma = 0
print(f"\nPA = {termo} ", end='')
soma = termo+razao
while c <9:
    print(f"{soma} ", end='')
    soma += razao
    c += 1
print("...")

total = 10
extra = 1
while extra != 0:
    extra = int(input("Quantos termos mais quer exibir? Se for nenhum, digite 0, senão digite o número de termos: "))
    print("... ", end="")
    total += extra
    c = 0
    while c < extra:
        print(f"{soma} ", end='')
        soma += razao
        c += 1
    print("...")

if extra ==0:
    print("\n--Fim--")
    print(f"Progressão encerrada com {total} termos exibidos")
    print("-" * 40)
