#Escreva um programa que pergunte a distância de uma viagem em Km.
# Calcule e peça o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

distancia = int(input("Digite a distância a ser percorrida nesta viagem, em km: "))
if distancia <= 200:
    preco = distancia*0.5
else:
    preco = distancia*0.45

print(f"Para a distancia de {distancia}km, o preço da passagem será de R${preco:.2f}.")
