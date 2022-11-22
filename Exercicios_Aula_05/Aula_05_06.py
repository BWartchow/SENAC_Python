# Escreva um programa que leia duas notas do aluno, calcule a sua média e diga:
# 1) Média abaixo de 5: REPROVADO
# 2) Entre 5 e 6.9: RECUPERAÇÃO
# 3) Acima de 7: APROVADO

nota1 = float(input("Nota 01: "))
nota2 = float(input("Nota 02: "))
media = (nota1+nota2)/2
print(f"Média = {media}.")
if media < 5:
    print("REPROVADO")
elif media < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO!")
