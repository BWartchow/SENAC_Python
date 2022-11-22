# Escreva um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# 1)	Quantas pessoas tem mais de 18 anos;
# 2)	Quantos homens foram cadastrados;
# 3)	Quantas mulheres tem menos de 20 anos.

maior18 = homens = mulheres_under20 = 0
txt = "RESULDADOS"
while True:
    sexo = str(input("Sexo [M/F]: ")).upper().strip()[0]
    while sexo not in "MF":
        sexo = str(input("Resposta inválida, digite novamente o Sexo [M/F]: ")).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    idade = int(input("Idade: "))
    if idade >= 18:
        maior18 += 1
    if sexo == 'F' and idade < 20:
        mulheres_under20 += 1
    continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while continuar not in "SN":
        continuar = str(input("Resposta inválida, digite novamente [S/N]: ")).upper().strip()[0]
    if continuar == "N":
        break
    print("="*40)
print(f"{txt:=^40}")
print(f"Quantas pessoas tem mais de 18 anos: {maior18}\nQuantos homens foram cadastrados: {homens}\nQuantas mulheres tem menos de 20 anos: {mulheres_under20}")
