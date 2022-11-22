#Escreva um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas delas ainda não atingiram a maioridade e quantas já são maiores
import datetime
anoAtual = datetime.date.today().year
menor = 0
maior = 0
for c in range (1,8):
    nome = str(input(f"Digite o {c}° nome: "))
    ano = int(input(f"Em que ano {nome} nasceu? "))
    if (anoAtual - ano) >= 18:
        maior += 1
    else:
        menor += 1
print("")
print(f"Considerando o ano atual ({anoAtual}), há {maior} pessoas maiores de idade e {menor} menores de idade nesta lista.")

