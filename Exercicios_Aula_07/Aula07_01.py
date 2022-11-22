# Escreva um programa que leia o sexo de uma pessoa, mas só aceite ‘M’ ou ‘F’.
# Caso esteja errado, peça digitar novamente até ter um valor correto.

resposta = str(input("Sexo [M/F]: ")).upper().strip()[0]
while resposta not in 'MF':
    resposta = str(input("Resposta inválida, digite uma das opções [M/F]: ")).upper().strip()[0]
print("Fim")
