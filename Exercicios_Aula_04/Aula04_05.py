#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Velocidade do veículo em km/h = "))
limite = 80
print("O veículo está acima da velocidade permitida!" if velocidade > limite else "Veículo dentro do limite de velocidade.")
multa = (velocidade-limite)*7
if velocidade > limite:
    print(f"A multa neste caso é de RS{multa} pois o limite era {limite}km/h e você estava a {velocidade}km/h.")
