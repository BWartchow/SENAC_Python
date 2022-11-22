#Escreva um programa que leia um número entre 0 e 9999
# e mostre cada um dos dígitos separados mostrando
# quantas unidades, dezenas, centenas e milhares há nesse número.

V = int(input("Número entre 0 e 9999: "))
N = str(int(10000+V))
print(V)
print("Unidades: {}".format(N[(len(N))-1]))
print("Dezenas: {}".format(N[(len(N))-2]))
print("Centenas: {}".format(N[(len(N))-3]))
print("Milhares: {}".format(N[(len(N))-4]))
