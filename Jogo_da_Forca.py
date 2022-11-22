# O computador escolhe a palavra.
# O usuário tem acesso ao número de letras da palavra no formato _.
# O usuário dá o palpite de uma letra.
# O programa procura a letra na palavra escolhida pelo computador.
# Se estiver presente, o programa substitui o _ correspondente à posição da letra pelo caractere.
# Se estiver ausente, número de erros recebe + 1.
# Se número de erros for igual a 6 antes da palavra estar completa, o usuário perde.
# Senão, ele vence. A palavra inteira é exibida.



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

# Sorteio da palavra e tratamento de caracteres:
# a) Nível Fácil:
posicaoEscolhidaF = random.randint(0,29)
facil = palavrasFaceis[posicaoEscolhidaF]
facil_tratada = remover_acentos((palavrasFaceis[posicaoEscolhidaF]).upper())
# a) Nível Médio:
posicaoEscolhidaM = random.randint(0,29)
medio = palavrasMedio[posicaoEscolhidaM]
medio_tratada = remover_acentos((palavrasMedio[posicaoEscolhidaM]).upper())
# a) Nível Dificil:
posicaoEscolhidaD = random.randint(0,49)
dificil = palavrasDificeis[posicaoEscolhidaD]
dificil_tratada = remover_acentos((palavrasDificeis[posicaoEscolhidaD]).upper())


print(f"Palavras para testar:\nFácil: {facil_tratada} \nMédio: {medio_tratada} \nDifícil: {dificil_tratada}")




