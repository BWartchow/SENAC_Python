# Escreva um programa que leia duas notas do user e calcule a média. Se a média for maior que 7, retorne APROVADO. Caso contrário, retorne REPROVADO.

N1 = float(input("Digite a nota 01: "))
N2 = float(input("Digite a nota 02: "))
print(f"Nota 01 = {N1}")
print(f"Nota 02 = {N2}")
media = (N1+N2)/2
print(f"Média = {media}")
print("Você foi \033[34mAprovado\033[34m!!" if media >= 7.0 else "Você foi \033[31mReprovado\033[31m!!")
