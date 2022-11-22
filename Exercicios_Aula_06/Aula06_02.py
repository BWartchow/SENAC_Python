# Escreva um programa que mostre todos os números pares que estão entre 1 e 50.

print("Números pares entre 1 e 50:")
for contador in range (1,51):
    if contador%2 == 0:
        print(f"- {contador}")
print("Fim!")
