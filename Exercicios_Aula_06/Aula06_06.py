# Escreva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print("="*50)
print("            PROGRESSÃO ARITMÉTICA!!!\n")
razao = int(input("Digite a razão da progressão aritmética: "))
primeiro = int(input("Digite o primeiro termo para iniciar a progressão: "))
print("\n")
print(f"Razão = {razao}\nPrimeiro termo = {primeiro}")
n = 1
soma = primeiro
for contador in range (primeiro, primeiro + 10):
    print(f"{n}) {soma}")
    soma += razao
    n += 1
print("Estes são os 10 primeiros termos desta progressão aritmética!")
