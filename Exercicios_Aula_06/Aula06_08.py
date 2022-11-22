# Escreva um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços e a acentuação.
# Ex: 1) “APOS A SOPA” 2) “A SACADA DA CASA” 3) “A TORRE DA DERROTA” 4) “O LOBO AMA O BOLO” 5) “ANOTARAM A DATA DA MARATONA”

#01) Módulo removedor de acentos:
from unicodedata import normalize

frase = input("Digite uma frase: ")

#02) Remover espaços extras, passar tudo pra maiúsculo, remover espaços em branco:
frase = frase.strip()
frase = frase.upper()
frase = ("".join(frase.split()))
#03) Remover acentos:
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
testar = remover_acentos(frase)

#04) Escrever a frase totalmente filtrada de trás pra frente:
reverso = testar[::-1]

#print(f"Frase para testar: {testar}")
#print(f"Ela ao contrário: {reverso}")

print("É PALÍNDROMO!!!" if testar == reverso else "NÃO É PALÍNDROMO")
