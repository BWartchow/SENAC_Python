# Escreva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# # 1) A média de idade do grupo;
# # 2) Qual é o nome do homem mais velho;
# # 3) Quantas mulheres têm menos de 20 anos.

soma = 0
maior = 0
homem_velho = str("")
under_20 = 0
for c in range (1,5):
    nome = str(input(f"Qual o {c}° nome? ").upper())
    idade = int(input(f"Quantos anos de idade {nome} tem? "))
    soma += idade
    sexo = str(input(f"Sexo de {nome} [M/F]: ").upper())
    if sexo == "M":
        if idade >= maior:
            maior = idade
            homem_velho = nome
    if sexo == "F":
        if idade < 20:
            under_20 += 1
    #print(f"{c}) Nome: {nome}; Idade: {idade}; Sexo: {sexo};")
    print("-"*35)
print("Fim das leituras\n")
media = soma/4
print("-"*35)
print(f"Média de idade do grupo: {media:.2f}")
print(f"Nome do homem mais velho: {homem_velho}")
print(f"Número de mulheres com menos de 20 anos: {under_20}")
