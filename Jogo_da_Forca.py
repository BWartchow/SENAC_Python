# Módulo removedor de acentos:
from unicodedata import normalize
# Remover acentos:
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
# Módulo randomizador:
import random

# Lista de 50 palavras difíceis:
palavrasDificeis = ['Acender', 'Afilhado', 'Agnóstico', 'Ardiloso', 'Áspero', 'Assombração', 'Asterisco', 'Balaústre', 'Basquete', 'Caminho', 'Champanhe', 'Chiclete', 'Chuveiro', 'Coelho', 'Contexto', 'Convivência', 'Coração', 'Desalmado', 'Eloquente', 'Esfirra', 'Esquerdo', 'Exceção', 'Filantropo', 'Fugaz', 'Gororoba', 'Heterossexual', 'Horrorizado', 'Idiossincrasia', 'Impacto', 'Inócuo', 'Independência', 'Jocoso', 'Laurel', 'Modernidade', 'Oftalmologista', 'Otorrinolaringologista', 'Panaceia', 'Paralelepípedo', 'Pororoca', 'Prognósticio', 'Quarentena', 'Quimera', 'Refeição', 'Reportagem', 'Sino', 'Taciturno', 'Temperança', 'Tênue', 'Ufanismo', 'Viscera']
# Lista de 30 palavras nível médio  com shuffle:
palavrasMedio = ['Afobado', 'Amendoim', 'Banheiro', 'Caatinga', 'Cachorro', 'Campeonato', 'Capricórnio', 'Catapora', 'Corrupção', 'Crepúsculo', 'Empenhado', 'Esparadrapo', 'Forca', 'Galáxia', 'História', 'Magenta', 'Manjericão', 'Menta', 'Moeda', 'Oração', 'Paçoca', 'Palavra', 'Pedreiro', 'Pneumonia', 'Pulmão', 'Rotatória', 'Serenata', 'Transeunte', 'Trilogia', 'Xícara']
# Lista de 30 palavras nível médio:
palavrasFaceis = ['Amarelo', 'Amiga', 'Amor', 'Ave', 'Avião', 'Avó', 'Balão', 'Bebê', 'Bolo', 'Branco', 'Cama', 'Caneca', 'Celular', 'Céu', 'Clube', 'Copo', 'Doce', 'Elefante', 'Escola', 'Estojo', 'Faca', 'Foto', 'Garfo', 'Geleia', 'Girafa', 'Janela', 'Limonada', 'Mãe', 'Meia', 'Noite', 'Óculos', 'ônibus', 'Ovo', 'Pai', 'Pão', 'Parque', 'Passarinho', 'Peixe', 'Pijama', 'Rato', 'Umbigo']

# CABEÇALHO
txt = "JOGO DA FORCA!"
print("*"*50)
print(f"{txt:^50}")
print("*"*50)
print("O computador escolherá uma palavra secreta.\nVocê tem que adivinhar a palavra, letra por letra.\nSomente seis palpites errados são permitidos.\n")

# Nível de Dificuldade
blank = ""
print(f"{blank:>7}","Opções de nível de dificuldade:")
print(f"{blank:>15}","[1] - FÁCIL")
print(f"{blank:>15}","[2] - MÉDIO")
print(f"{blank:>15}","[3] - DIFÍCIL")
dificuldade = int(input("\nQual sua escolha? [1/2/3] "))
if dificuldade < 1 or dificuldade > 3:
    dificuldade = int(input("Digite um valor válido: [1/2/3] "))
# MODO FÁCIL:
if dificuldade == 1:
    palavra_original = random.choice(palavrasFaceis)
    palavra = remover_acentos(palavra_original).upper()
    fim = len(palavra)
    lista_letras = []
    lista_secreta = []
    erros = 6
    # Letras e letras ocultas:
    for i in range(0, fim):
        letras = palavra[i]
        lista_letras.append(letras)
    for i in range(0, fim):
        letras_secretas = lista_letras[i]
        lista_secreta.append(letras_secretas.replace(letras_secretas, "_"))
    # JOGANDO MODO FÁCIL:
    print(f"Você escolheu [{dificuldade}] - FÁCIL")
    print(f"\nPALAVRA SORTEADA = {lista_secreta}\nNúmero de letras = {fim}")
    while erros > 0:
        while "_" in lista_secreta:
            palpite = str(input("Palpite: ")).upper().strip()[0]
            jogada = palavra.find(palpite)
            if jogada >= 0:
                print("Tem essa letra!!!")
                print("~" * 50)
                for i in range(0, fim):
                    if palpite == lista_letras[i]:
                        lista_secreta[i] = palpite
            else:
                print("Não tem essa letra.")
                erros -= 1
                print(f"Você pode errar mais {erros} vezes." if erros != 0 else "\nGAME OVER")
                print("~" * 50)
            if erros == 0:
                print(f"A palavra era {palavra_original}, que pena!")
                print("Programa Encerrado...")
                break
            print(f"\nJOGO ATUAL = {lista_secreta}")
        if "_" not in lista_secreta:
            print("Você Venceu!")
            print(f"A palavra era {palavra_original}, parabéns!")
            break
    print('Fim')
# MODO INTERMEDIÁRIO
elif dificuldade == 2:
    palavra_original = random.choice(palavrasMedio)
    palavra = remover_acentos(palavra_original).upper()
    fim = len(palavra)
    lista_letras = []
    lista_secreta = []
    erros = 6
    # Letras e letras ocultas:
    for i in range(0, fim):
        letras = palavra[i]
        lista_letras.append(letras)
    for i in range(0, fim):
        letras_secretas = lista_letras[i]
        lista_secreta.append(letras_secretas.replace(letras_secretas, "_"))
    # JOGANDO MODO INTERMEDIÁRIO:
    print(f"Você escolheu [{dificuldade}] - MÉDIO")
    print(f"\nPALAVRA SORTEADA = {lista_secreta}\nNúmero de letras = {fim}")
    while erros > 0:
        while "_" in lista_secreta:
            palpite = str(input("Palpite: ")).upper().strip()[0]
            jogada = palavra.find(palpite)
            if jogada >= 0:
                print("Tem essa letra!!!")
                print("~" * 50)
                for i in range(0, fim):
                    if palpite == lista_letras[i]:
                        lista_secreta[i] = palpite
            else:
                print("Não tem essa letra.")
                erros -= 1
                print(f"Você pode errar mais {erros} vezes." if erros != 0 else "\nGAME OVER")
                print("~" * 50)
            if erros == 0:
                print(f"A palavra era {palavra_original}, que pena!")
                print("Programa Encerrado...")
                break
            print(f"\nJOGO ATUAL = {lista_secreta}")
        if "_" not in lista_secreta:
            print("Você Venceu!")
            print(f"A palavra era {palavra_original}, parabéns!")
            break
    print('Fim')
# MODO DIFICIL
elif dificuldade == 3:
    palavra_original = random.choice(palavrasDificeis)
    palavra = remover_acentos(palavra_original).upper()
    fim = len(palavra)
    lista_letras = []
    lista_secreta = []
    erros = 6
    # Letras e letras ocultas:
    for i in range(0, fim):
        letras = palavra[i]
        lista_letras.append(letras)
    for i in range(0,fim):
        letras_secretas = lista_letras[i]
        lista_secreta.append(letras_secretas.replace(letras_secretas, "_"))
    # JOGANDO MODO DIFÍCIL:
    print(f"Você escolheu [{dificuldade}] - DIFÍCIL")
    print(f"\nPALAVRA SORTEADA = {lista_secreta}\nNúmero de letras = {fim}")
    while erros > 0:
        while "_" in lista_secreta:
            palpite = str(input("Palpite: ")).upper().strip()[0]
            jogada = palavra.find(palpite)
            if jogada >= 0:
                print("Tem essa letra!!!")
                print("~" * 50)
                for i in range(0, fim):
                    if palpite == lista_letras[i]:
                        lista_secreta[i] = palpite
            else:
                print("Não tem essa letra.")
                erros -= 1
                print(f"Você pode errar mais {erros} vezes." if erros != 0 else "\nGAME OVER")
                print("~" * 50)
            if erros == 0:
                print(f"A palavra era {palavra_original}, que pena!")
                print("Programa Encerrado...")
                break
            print(f"\nJOGO ATUAL = {lista_secreta}")
        if "_" not in lista_secreta:
            print("Você Venceu!")
            print(f"A palavra era {palavra_original}, parabéns!")
            break
    print('Fim')
