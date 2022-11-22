#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite seu salário em R$: "))
if salario > 1250.00:
    aumento = 0.1
else:
    aumento = 0.15
print(f"Parabéns, seu salário passou de R${salario:.2f} para R${salario+(salario*aumento):.2f}! Um aumento de R${(salario*aumento):.2f}")
