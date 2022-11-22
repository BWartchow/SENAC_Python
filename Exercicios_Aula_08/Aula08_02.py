# Escreva um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for zero.

while True:
    N = int(input("\nVocê quer a tabuada de qual número? (Digite 0 para sair) "))
    if N == 0:
        print("\nEncerrando...")
        print("Fim")
        break
    msg = f"TABUADA DO {N}"
    print("="*40)
    print(f"{msg:^40}")
    print("="*40)
    i = 1
    while i <= 10:
        print(f"{i} x {N} = {i*N}")
        i += 1
