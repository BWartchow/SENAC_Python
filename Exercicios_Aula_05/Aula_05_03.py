# Escreva um programa que aprove um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Valor da casa R$: "))
salario = float(input("Seu salário R$: "))
anos = int(input("Em quantos anos você pretende pagar? "))
parcelas = anos*12
prestacao = casa/parcelas
teto = salario*0.3
print(f"Certo, seu salário é R${salario:.2f}, 30% dele é {teto:.2f}.")
print("Empréstimo APROVADO!" if prestacao <= teto else "Empréstimo NEGADO")
if prestacao <= teto:
    print(f"A pagar: {parcelas}x de R${prestacao:.2f}.")
