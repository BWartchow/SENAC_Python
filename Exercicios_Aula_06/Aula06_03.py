# Escreva um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
for contador in range (1,501):
    if contador%2==1 and contador%3==0:
        soma += contador
        #print(contador)
print("Processei todos os números entre 1 e 500...")
print(f"A soma dos ímpares e múltiplos de 3 deu {soma}!")
