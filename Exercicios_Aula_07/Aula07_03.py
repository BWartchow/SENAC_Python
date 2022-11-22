# Escreva um programa que lerá dois valores do usuário e mostre um menu na tela dando as opções:
# [1] – somar, [2] – multiplicar, [3] – maior, [4] – novos números, [5] – sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.

v1 = int(input("Primeiro valor: "))
v2 = int(input("Segundo valor: "))
opcao = ""

while opcao != "5":
    texto = "OPÇÕES"
    print("-" * 35)
    print(f" {texto:^35}")
    print("-" * 35)
    print("[1] – somar \n[2] – multiplicar \n[3] – maior \n[4] – novos números \n[5] – sair do programa")
    opcao = str(input("Escolha uma das opções acima [1/2/3/4/5]: "))

    while opcao not in "12345":
        opcao = str(input("Opção inválida, digite novamente [1/2/3/4/5]: "))

    if opcao == "1":
        print("\n OPÇÃO 1 - SOMA: ")
        print(f"{v1} + {v2} = {v1 + v2}")
    elif opcao == "2":
        print("\n OPÇÃO 2 - MULTIPLICAÇÃO: ")
        print(f"{v1} x {v2} = {v1 * v2}")
    elif opcao == "3":
        print("\n OPÇÃO 3 - COMPARAÇÃO DE MAIOR VALOR: ")
        print(f"O maior valor é {v1}" if v1 > v2 else f"O maior valor é {v2}")
    elif opcao == "4":
        print("\nOPÇÃO 4 - ESCOLHER NOVOS VALORES: ")
        v1 = int(input("Primeiro valor: "))
        v2 = int(input("Segundo valor: "))

print("\nSaindo do programa...")
print("Fim")
