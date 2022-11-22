# Escreva um programa que leia um número do usuário e retorne a tábuada desse número.

print("="*30)
print(" GERADOR DE TABUADA!!!!!!!!!")
print("="*30)

n = int(input("Digite o número que você quer: "))
print("="*30)
print(f"TABUADA DE {n}:")
for multiplicador in range (1,11):
    print(f"{multiplicador} x {n} = {multiplicador*n}")
print("="*30)
