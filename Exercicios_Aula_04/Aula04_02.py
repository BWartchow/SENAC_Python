# Escreva um programa que leia uma string e retorne um “bom dia” ao user, dizendo que o nome dele é bonito caso o nome começar com a letra B.
nome = str(input("Qual o seu nome? "))
if nome.upper()[0] == "B":
    print("Nomes iniciados com 'B' são muito bonitos")


print(f"\033[1;34mBom dia, {nome}\033[30m")


print('\033[7;30mBom dia {}\033[m'.format(nome))


cores = {'limpa':'\033[m', 'azul':'\033[34m'}
print('Muito prazer {}{}{}!' .format(cores['azul'], nome, cores['limpa']))
