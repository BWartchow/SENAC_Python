# Escreva um programa que leia o nome e preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# 1)	Qual é o total gasto na compra;
# 2)	Quantos produtos custam mais de R$ 1000.
# 3)	Qual é o nome do produto mais barato.

#Variáveis acumuladoras:
totalRS = itens = acima1000 = menorPreco = 0
maisBarato = ""

#Variáveis de entrada:
produto = str(input("Produto: "))
itens += 1
maisBarato = produto
preco = float(input("Preço: R$ "))
totalRS += preco
menorPreco = preco
if preco >= 1000.00:
    acima1000 += 1
#Loop
resposta = str(input("Há mais produtos? Digite [S/N]: ")).upper().strip()[0]
while resposta not in 'SN':
    resposta = str(input("Não entendi. Digite [S/N]: ")).upper().strip()[0]
if resposta == 'S':
    while True:
        print('='*45)
        produto = str(input("Produto: "))
        itens += 1
        preco = float(input("Preço: R$ "))
        totalRS += preco
        if preco >= 1000.00:
            acima1000 += 1
        if preco <= menorPreco:
            menorPreco = preco
            maisBarato = produto
        resposta = str(input("Há mais produtos? Digite [S/N]: ")).upper().strip()[0]
        while resposta not in 'SN':
            resposta = str(input("Não entendi. Digite [S/N]: ")).upper().strip()[0]
        if resposta == 'N':
            break
txt = "OBRIGADO PELAS COMPRAS!"
print("="*45)
print(f"{txt:^45}")
print(f"Valor total a ser pago: R$ {totalRS:.2f}\nTotal de itens comprados: {itens}")
print(f"Total de itens acima de R$1000,00: {acima1000}\nProduto mais barato: {maisBarato} - R$ {menorPreco:.2f}")
