# Escreva um programa que simule o funcionamento de um caixa eletrônico.
# O usuário informa o quanto deverá ser sacado (inteiro) e o programa retornará quantas cédulas de cada valor serão entregues.
# Considere que só há cédulas de 50, 20, 10 e 1.

# MENU:
txt1 = "CAIXA ELETROÔNICO"
txt2 = "TERMINAL DE SAQUES"
print("-"*45)
print(f"{txt1:^45}\n{txt2:^45}")
print("-"*45)
valor = int(input("\nValor para saque: R$ "))

notas50 = (valor // 50)
notas20 = (valor % 50) // 20
notas10 = ((valor % 50)% 20) // 10
notas1 = (((valor % 50)%20))% 10

print("-"*45)
print("\nCédulas Fornecidas:")
if notas50:
    print(f"{notas50} x cédulas de R$50")
if notas20:
    print(f"{notas20} x cédulas de R$20")
if notas10:
    print(f"{notas10} x cédulas de R$10")
if notas1:
    print(f"{notas1} x cédulas de R$1")

resposta = str(input("\nDeseja realizar outro saque? [S/N] ")).upper().strip()[0]
while resposta not in 'SN':
    resposta = str(input("Resposta inválida. Digite novamente: [S/N] ")).upper().strip()[0]
while resposta == 'S':
    print("-" * 45)
    valor = int(input("\nValor para saque: R$ "))

    notas50 = (valor // 50)
    notas20 = (valor % 50) // 20
    notas10 = ((valor % 50) % 20) // 10
    notas1 = (((valor % 50) % 20)) % 10

    print("-" * 45)
    print("\nCédulas Fornecidas:")
    if notas50:
        print(f"{notas50} x cédulas de R$50")
    if notas20:
        print(f"{notas20} x cédulas de R$20")
    if notas10:
        print(f"{notas10} x cédulas de R$10")
    if notas1:
        print(f"{notas1} x cédulas de R$1")

    resposta = str(input("\nDeseja realizar outro saque? [S/N] ")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input("Resposta inválida. Digite novamente: [S/N] ")).upper().strip()[0]
    if resposta == 'N':
        break
txt = "Sistema Encerrado"
print(f"\n{txt:-^45}")
