# Escreva um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
soma = vitorias = 0

while True:
    msg = "PAR OU ÍMPAR"
    print("=" * 40)
    print(f"{msg:^40}")
    print("=" * 40)
    print("[1] - PAR\n[2] - ÍMPAR")
    escolha = str(input("\nQual a sua escolha? ")).strip()[0]
    while escolha not in '12':
        escolha = str(input("\nResposta inválida. Digite novamente: ")).strip()[0]

   #PAR
    if escolha == '1':
        user = int(input("Você escolheu PAR. Digite seu valor: "))
        maquina = random.randint(0,10)
        soma = user+maquina
        if soma % 2 != 0:
            print(f"Número do computador = {maquina}\nNúmero do usuário = {user}")
            print(f"Soma = {soma} -> ÍMPAR")
            print("\nVocê perdeu...")
            print(f"Número de vitórias consecutivas = {vitorias}")
            print("Fim")
            break
        else:
            print(f"Número do computador = {maquina}\nNúmero do usuário = {user}")
            print(f"Soma = {soma} -> PAR")
            print("\nVocê GANHOU...")
            vitorias += 1

    #ÍMPAR
    if escolha == '2':
        user = int(input("Você escolheu ÍMPAR. Digite seu valor: "))
        maquina = random.randint(0, 10)
        soma = maquina + user
        if soma % 2 == 0:
            print(f"Número do computador = {maquina}\nNúmero do usuário = {user}")
            print(f"Soma = {soma} -> PAR")
            print("\nVocê perdeu...")
            print(f"Número de vitórias consecutivas = {vitorias}")
            print("Fim")
            break
        else:
            print(f"Número do computador = {maquina}.\nNúmero do usuário = {user}.")
            print(f"Soma = {soma} -> ÍMPAR")
            print("\nVocê GANHOU...")
            vitorias += 1
