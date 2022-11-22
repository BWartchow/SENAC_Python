# Escreva um programa que leia um número inteiro qualquer e peça ao usuário qual será a base de conversão:
# 1) [1] – Binário
# 2) [2] – Octal
# 3) [3] – Hexadecimal

n = int(input("Digite um número inteiro: "))
print("="*38)
print("Escolha uma das bases para conversão:\n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal")
print("="*38)
opcao = int(input("Sua opção: "))
if opcao == 1:
    print(f"{n} em BINÁRIO = {bin(n)[2:]}")
elif opcao == 2:
    print(f"{n} em OCTAL = {oct(n)[2:]}")
elif opcao == 3:
    print(f"{n} em HEXADECIMAL = {hex(n)[2:]}")
else:
    print("Opção inválida")

