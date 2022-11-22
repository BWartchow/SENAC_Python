# Considere que há cédulas de 200, 100, 50, 20, 10, 5 e 2.

# MENU:
txt1 = "CAIXA ELETROÔNICO"
txt2 = "TERMINAL DE SAQUES"
print("-"*45)
print(f"{txt1:^45}\n{txt2:^45}")
print("-"*45)
valor = int(input("\nValor para saque: R$ "))
while valor < 5:
    valor = int(input("\nValor indisponível. Valor para saque: R$ "))

if valor >= 200:
    notas200 = (valor // 200)
    notas100 = (valor % 200) // 100
    notas50 = ((valor % 200)%100) // 50
    notas20 = (((valor % 200)%100)% 50) // 20
    notas10 = ((((valor % 200)%100)% 50)% 20) // 10
    notas5 = (((((valor % 200)%100)% 50)% 20)% 10) // 5
    notas2 = ((((((valor % 200)%100)% 50)% 20)% 10)% 5) // 2

    print("-" * 45)
    if ((valor%5) >= 1):
        print("Valor de saque foi reajustado!")
    print("\nCédulas Fornecidas:")
    if notas200:
        print(f"{notas200} x cédulas de R$200")
    if notas100:
        print(f"{notas100} x cédulas de R$100")
    if notas50:
        print(f"{notas50} x cédulas de R$50")
    if notas20:
        print(f"{notas20} x cédulas de R$20")
    if notas10:
        print(f"{notas10} x cédulas de R$10")
    if notas5:
        print(f"{notas5} x cédulas de R$5")
    if notas2:
        print(f"{notas2} x cédulas de R$2")
elif valor < 200 and valor >= 100:
    notas100 = valor // 100
    notas50 = (valor % 100) // 50
    notas20 = ((valor % 100) % 50) // 20
    notas10 = (((valor % 100) % 50) % 20) // 10
    notas5 = ((((valor % 100) % 50) % 20) % 10) // 5
    notas2 = (((((valor % 100) % 50) % 20) % 10) % 5) // 2
    print("-" * 45)
    if ((valor%5) >= 1):
        print("Valor de saque foi reajustado!")
    print("\nCédulas Fornecidas:")
    if notas100:
        print(f"{notas100} x cédulas de R$100")
    if notas50:
        print(f"{notas50} x cédulas de R$50")
    if notas20:
        print(f"{notas20} x cédulas de R$20")
    if notas10:
        print(f"{notas10} x cédulas de R$10")
    if notas5:
        print(f"{notas5} x cédulas de R$5")
    if notas2:
        print(f"{notas2} x cédulas de R$2")
elif valor < 100:
    notas50 = (valor // 50)
    notas20 = (valor % 50) // 20
    notas10 = ((valor % 50) % 20) // 10
    notas5 = (((valor % 50) % 20) % 10) // 5
    notas2 = ((((valor % 50) % 20) % 10) % 5) // 2
    print("-" * 45)
    if ((valor%5) >= 1):
        print("Valor de saque foi reajustado!")
    print("\nCédulas Fornecidas:")
    if notas50:
        print(f"{notas50} x cédulas de R$50")
    if notas20:
        print(f"{notas20} x cédulas de R$20")
    if notas10:
        print(f"{notas10} x cédulas de R$10")
    if notas5:
        print(f"{notas5} x cédulas de R$5")
    if notas2:
        print(f"{notas2} x cédulas de R$2")

resposta = str(input("\nDeseja realizar outro saque? [S/N] ")).upper().strip()[0]
while resposta not in 'SN':
    resposta = str(input("Resposta inválida. Digite novamente: [S/N] ")).upper().strip()[0]

while resposta == 'S':
    print("-" * 45)
    valor = int(input("\nValor para saque: R$ "))
    while valor < 5:
        valor = int(input("\nValor indisponível. Valor para saque: R$ "))

    if valor >= 200:
        notas200 = (valor // 200)
        notas100 = (valor % 200) // 100
        notas50 = ((valor % 200) % 100) // 50
        notas20 = (((valor % 200) % 100) % 50) // 20
        notas10 = ((((valor % 200) % 100) % 50) % 20) // 10
        notas5 = (((((valor % 200) % 100) % 50) % 20) % 10) // 5
        notas2 = ((((((valor % 200) % 100) % 50) % 20) % 10) % 5) // 2
        print("-" * 45)
        if ((valor % 5) >= 1):
            print("Valor de saque foi reajustado!")
        print("\nCédulas Fornecidas:")
        if notas200:
            print(f"{notas200} x cédulas de R$200")
        if notas100:
            print(f"{notas100} x cédulas de R$100")
        if notas50:
            print(f"{notas50} x cédulas de R$50")
        if notas20:
            print(f"{notas20} x cédulas de R$20")
        if notas10:
            print(f"{notas10} x cédulas de R$10")
        if notas5:
            print(f"{notas5} x cédulas de R$5")
        if notas2:
            print(f"{notas2} x cédulas de R$2")
    elif valor < 200 and valor >= 100:
        notas100 = valor // 100
        notas50 = (valor % 100) // 50
        notas20 = ((valor % 100) % 50) // 20
        notas10 = (((valor % 100) % 50) % 20) // 10
        notas5 = ((((valor % 100) % 50) % 20) % 10) // 5
        notas2 = (((((valor % 100) % 50) % 20) % 10) % 5) // 2
        print("-" * 45)
        if ((valor % 5) >= 1):
            print("Valor de saque foi reajustado!")
        print("\nCédulas Fornecidas:")
        if notas100:
            print(f"{notas100} x cédulas de R$100")
        if notas50:
            print(f"{notas50} x cédulas de R$50")
        if notas20:
            print(f"{notas20} x cédulas de R$20")
        if notas10:
            print(f"{notas10} x cédulas de R$10")
        if notas5:
            print(f"{notas5} x cédulas de R$5")
        if notas2:
            print(f"{notas2} x cédulas de R$2")
    elif valor < 100:
        notas50 = (valor // 50)
        notas20 = (valor % 50) // 20
        notas10 = ((valor % 50) % 20) // 10
        notas5 = (((valor % 50) % 20) % 10) // 5
        notas2 = ((((valor % 50) % 20) % 10) % 5) // 2
        print("-" * 45)
        if ((valor % 5) >= 1):
            print("Valor de saque foi reajustado!")
        print("\nCédulas Fornecidas:")
        if notas50:
            print(f"{notas50} x cédulas de R$50")
        if notas20:
            print(f"{notas20} x cédulas de R$20")
        if notas10:
            print(f"{notas10} x cédulas de R$10")
        if notas5:
            print(f"{notas5} x cédulas de R$5")
        if notas2:
            print(f"{notas2} x cédulas de R$2")

    resposta = str(input("\nDeseja realizar outro saque? [S/N] ")).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input("Resposta inválida. Digite novamente: [S/N] ")).upper().strip()[0]

    if resposta == 'N':
        break

txt = "Sistema Encerrado"
print(f"\n{txt:-^45}")
