# Escreva um programa que leia um nome. Se o nome for igual ao seu, diga que o nome é muito bonito.
# Se o nome for Pedro, Maria ou Paulo, diga que é um nome muito comum no Brasil.
# Se for Ana, Cláudia, Jéssica ou Juliana, diga que é um belo nome feminino.
# Caso não satisfaça nenhum das condições anteriores, apenas informe que o nome é bem normal.
# No fim, retorne um bom dia com o nome do user.

nome = str(input("Qual é o seu nome? ")).strip()
if nome == 'Be':
    print(f"Que nome bonito, {nome}!")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f"Seu nome é bem popular no Brasil, {nome}!")
elif nome == 'Ana' or nome == 'Cláudia' or nome == 'Jéssica' or nome == 'Juliana':
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal!")
print(f"Tenha um bom dia, {nome}!")
