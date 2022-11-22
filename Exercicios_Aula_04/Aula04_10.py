#Escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#A soma de dois lados deve ser maior que o terceiro lado.

R1 = float(input("Comprimento da reta número 1 em cm: "))
R2 = float(input("Comprimento da reta número 2 em cm: "))
R3 = float(input("Comprimento da reta número 3 em cm: "))
print(f"Você informou {R1}cm, {R2}cm e {R3}cm!")
if (R1+R2)>R3 and (R2+R3)>R1 and (R3+R1)>R2:
    print("Olha que massa, daria pra formar um triângulo!!")
else:
    print("Só não daria pra formar um triângulo com estas retas...")
