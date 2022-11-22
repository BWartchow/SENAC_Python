# Escreva um programa que leia os dois catetos de um triângulo retângulo e retorne o comprimento da hipotenusa.

import math

cateto1 = float(input("Cateto adjacente = "))
cateto2 = float(input("Cateto oposto = "))
##hipotenusa = math.sqrt((cateto1*cateto1)+(cateto2*cateto2))
hipotenusa = math.hypot(cateto1,cateto2)
print("Hipotenusa = {}".format(hipotenusa))
