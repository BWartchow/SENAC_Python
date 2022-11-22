# Escreva um programa que leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da PA.
# (USE WHILE)

txt = "PROGRESSÃO ARITMÉTICA:"
print("-"*40)
print(f"{txt:^40}")
print("-"*40)
razao = int(input("Qual será a razão da progressão? "))
termo = int(input("Digite o primeiro termo da progressão: "))
print("\nOs dez primeiros termos dessa razão: ")
c = soma = 0
print(f"\nPA = {termo} ", end='')
soma = termo+razao
while c <9:
    print(f"{soma} ", end='')
    soma += razao
    c += 1
print("\n--Fim--")
