# Escreva um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input("Ângulo = "))
angrad = math.radians(ang)
seno = math.sin(angrad)
cos = math.cos(angrad)
tan = math.tan(angrad)
print("seno = {:.2f}\ncosseno = {:.2f}\ntangente = {:.2f}".format(seno,cos,tan))
