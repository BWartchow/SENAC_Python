# Escreva um programa que leia um frase e mostre:
# 1)	Quantas vezes aparece a letra “A”;
# 2)	Em que posição ela aparece pela primeira vez;
# 3)	Em que posição aparece pela última vez.

frase = input("Digite uma frase: ")
print("1) Quantas vezes aparece a letra “A”? ")
print(frase.count("a"))
print("2) Em que posição ela aparece pela primeira vez? ")
print("Considerando a primeira posição como 1..: {}".format((frase.find("a"))+1))
print("3) Em que posição aparece pela última vez? ")
print("Considerando a primeira posição como 1..: {}".format(frase.rfind("a")+1))
