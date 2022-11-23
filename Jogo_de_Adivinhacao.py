# Crie um jogo de adivinhação. O jogador deverá tentar descobrir qual foi o valor sorteado.
# Crie um menu onde o jogador escolherá 3 modos de jogo: fácil, médio e difícil.
# No nível fácil o jogador terá 7 tentivas e o número deverá estar entre 1 e 20.
# No nível médio o jogador terá 4 tentativas e o número deverá estar entre 1 e 12.
# No difícil 3 tentativas e o número deverá estar entre 1 e 10.
# A cada jogada, informe se o palpite do usuário foi maior ou menor do que o número pensando de forma a ajudar o usuário.
# Mostre as palavras maior e menor em cores diferentes.
# No final, mostre quantas tentativas foram necessárias até acertar.
# Caso ele perca, faça uma saída de ‘GAME OVER’.
# Caso o jogador queira jogar novamente, repita o jogo.
# Se houver mais de uma partida, faça um rank das três maiores pontuações.

import random

primeiroLugar = 0
segundoLugar = 0
terceiroLugar = 0
numeroJogos = 1

# CABEÇALHO
blank = ""
txt = "JOGO DE ADIVINHAÇÃO!"
print("*"*90)
print(f"{txt:^90}")
print("*"*90)
print(f"{blank:>26}","O computador escolherá um número secreto.",f"\n{blank:>26}","Você tem que adivinhar o valor sorteado.\n")
print("-> Nível Fácil:\nSomente sete palpites errados são permitidos. Descubra o número sorteado entre 1 e 20.")
print("-> Nível Médio:\nSomente quatro palpites errados são permitidos. Descubra o número sorteado entre 1 e 12.")
print("-> Nível Difícil:\nSomente três palpites errados são permitidos. Descubra o número sorteado entre 1 e 10.")

jogar = 'S'
while jogar == 'S':

    print("-> Opções de nível de dificuldade:")
    print(f"{blank:>4}","[1] - FÁCIL")
    print(f"{blank:>4}","[2] - MÉDIO")
    print(f"{blank:>4}","[3] - DIFÍCIL")

    dificuldade = int(input("\nQual sua escolha? [1/2/3] "))
    if dificuldade < 1 or dificuldade > 3:
        dificuldade = int(input("Digite um valor válido: [1/2/3] "))
    tentativa = 0

    # MODO FÁCIL:
    if dificuldade == 1:
        maquina = random.randint(1,20)
        # print(maquina)
        erros = 7
        # JOGANDO MODO FÁCIL:
        print(f"Você escolheu [{dificuldade}] - \033[34mFÁCIL\033[m")
        print(f"Número de chances = {erros}")
        user = int(input('Tente adivinhar o valor sorteado entre 1 e 20: '))
        while erros > 0:
            if user > 20 or user < 1:
                tentativa += 1
                erros -= 1
                user = int(input(f"\nPreste atenção no intervalo. Só mais {erros} chances. faça um palpite \033[31mentre 1 e 20\033[m: "))
            if maquina != user:
                tentativa += 1
                erros -= 1
                if erros > 0:
                    print(f"\nErrou :( Você pode errar mais {erros} vezes." if erros > 1 else f"\nErrou :( Você pode errar mais {erros} vez.")
                    print(f"O número é \033[31mmenor\033[m que esse..." if user > maquina else f"O número é \033[34mmaior\033[m que esse...")
                    user = int(input('Faça outro palpite entre 1 e 20: '))
                    if user > 20 or user < 1:
                        if erros > 0:
                            tentativa += 1
                            erros -= 1
                            user = int(input(f"\nPreste atenção no intervalo. Só mais {erros} chances. faça um palpite \033[31mentre 1 e 20\033[m: "))
                        else:
                            print("\nVocê atingiu o número máximo de tentativas.")
                            print(f"O número sorteado era {maquina}, que pena!")
                            print("\033[31mGAME OVER\033[m")
                            break
                else:
                    print("\nVocê atingiu o número máximo de tentativas.")
                    print(f"O número sorteado era {maquina}, que pena!")
                    print("\033[31mGAME OVER\033[m")
                    break
            elif user == maquina:
                print("-"*90)
                print(f"Você escolheu {user}!\nParabéns, você \033[34mVENCEU!\033[m O número sorteado era {maquina}.")
                tentativa += 1
                print(f"Acertou com {tentativa} palpite(s)!")
                primeiroLugar = tentativa
                break
            elif erros == 0:
                print("\nVocê atingiu o número máximo de tentativas.")
                print(f"O número sorteado era {maquina}, que pena!")
                print("\033[31mGAME OVER\033[m")
                break

    # MODO INTERMEDIÁRIO:
    if dificuldade == 2:
        maquina = random.randint(1,12)
        # print(maquina)
        erros = 4
        # JOGANDO MODO INTERMEDIÁRIO:
        print(f"Você escolheu [{dificuldade}] - \033[34mINTERMEDIÁRIO\033[m")
        print(f"Número de chances = {erros}")
        user = int(input('Tente adivinhar o valor sorteado entre 1 e 12: '))
        while erros > 0:
            if user > 12 or user < 1:
                tentativa += 1
                erros -= 1
                user = int(input(f"\nPreste atenção no intervalo. Só mais {erros} chances. faça um palpite \033[31mentre 1 e 12\033[m: "))
            if maquina != user:
                tentativa += 1
                erros -= 1
                if erros > 0:
                    print(f"\nErrou :( Você pode errar mais {erros} vezes." if erros > 1 else f"\nErrou :( Você pode errar mais {erros} vez.")
                    print(f"O número é \033[31mmenor\033[m que esse..." if user > maquina else f"O número é \033[34mmaior\033[m que esse...")
                    user = int(input('Faça outro palpite entre 1 e 12: '))
                    if user > 12 or user < 1:
                        if erros > 0:
                            tentativa += 1
                            erros -= 1
                            user = int(input(f"\nPreste atenção no intervalo. Só mais {erros} chances. faça um palpite \033[31mentre 1 e 12\033[m: "))
                        else:
                            print("\nVocê atingiu o número máximo de tentativas.")
                            print(f"O número sorteado era {maquina}, que pena!")
                            print("\033[31mGAME OVER\033[m")
                            break
                else:
                    print("\nVocê atingiu o número máximo de tentativas.")
                    print(f"O número sorteado era {maquina}, que pena!")
                    print("\033[31mGAME OVER\033[m")
                    break
            elif user == maquina:
                print("-"*90)
                print(f"Você escolheu {user}!\nParabéns, você \033[34mVENCEU!\033[m O número sorteado era {maquina}.")
                tentativa += 1
                print(f"Acertou com {tentativa} palpite(s)!")
                segundoLugar = tentativa
                break
            elif erros == 0:
                print("\nVocê atingiu o número máximo de tentativas.")
                print(f"O número sorteado era {maquina}, que pena!")
                print("\033[31mGAME OVER\033[m")
                break

    # MODO DIFÍCIL:
    if dificuldade == 3:
        maquina = random.randint(1, 10)
        # print(maquina)
        erros = 3
        # JOGANDO MODO DIFÍCIL:
        print(f"Você escolheu [{dificuldade}] - \033[34mDIFÍCIL\033[m")
        print(f"Número de chances = {erros}")
        user = int(input('Tente adivinhar o valor sorteado entre 1 e 10: '))
        while erros > 0:
            if user > 10 or user < 1:
                tentativa += 1
                erros -= 1
                user = int(input(f"\nPreste atenção no intervalo. Só mais {erros} chances. faça um palpite \033[31mentre 1 e 10\033[m: "))
            if maquina != user:
                tentativa += 1
                erros -= 1
                if erros > 0:
                    print(f"\nErrou :( Você pode errar mais {erros} vezes." if erros > 1 else f"\nErrou :( Você pode errar mais {erros} vez.")
                    print(f"O número é \033[31mmenor\033[m que esse..." if user > maquina else f"O número é \033[34mmaior\033[m que esse...")
                    user = int(input('Faça outro palpite entre 1 e 10: '))
                    if user > 10 or user < 1:
                        if erros > 0:
                            tentativa += 1
                            erros -= 1
                            user = int(input(f"\nPreste atenção no intervalo. Só mais {erros} chances. faça um palpite entre 1 e 10: "))
                        else:
                            print("\nVocê atingiu o número máximo de tentativas.")
                            print(f"O número sorteado era {maquina}, que pena!")
                            print("\033[31mGAME OVER\033[m")
                            break
                else:
                    print("\nVocê atingiu o número máximo de tentativas.")
                    print(f"O número sorteado era {maquina}, que pena!")
                    print("\033[31mGAME OVER\033[m")
                    break
            elif user == maquina:
                print("-" * 90)
                print(f"Você escolheu {user}!\nParabéns, você \033[34mVENCEU!\033[m O número sorteado era {maquina}.")
                tentativa += 1
                print(f"Acertou com {tentativa} palpite(s)!")
                terceiroLugar = tentativa
                break
            elif erros == 0:
                print("\nVocê atingiu o número máximo de tentativas.")
                print(f"O número sorteado era {maquina}, que pena!")
                print("\033[31mGAME OVER\033[m")
                break

    jogar = str(input("\nVamos jogar novamente?? Digite S para sim ou N para não: ")).upper().strip()[0]
    while jogar not in 'SN':
        jogar = str(input("Não entendi... Digite novamente [S/N]: ")).upper().strip()[0]
    if jogar == 'S':
        numeroJogos += 1
    if jogar == 'N':
        print("\033[31mPrograma Encerrado...\033[m")
        break

if numeroJogos == 1:
    if primeiroLugar > 0:
        print(f"Menor número de palpites até vencer no MODO FÁCIL = {primeiroLugar}")
    if segundoLugar > 0:
        print(f"Menor número de palpites até vencer NO MODO INTERMEDIÁRIO = {segundoLugar}")
    if terceiroLugar > 0:
        print(f"Menor número de palpites até vencer NO MODO DIFÍCIL = {terceiroLugar}")
elif numeroJogos > 1:
    if primeiroLugar > 0:
        print(f"Menor número de palpites até vencer no MODO FÁCIL = {primeiroLugar}")
    if segundoLugar > 0:
        print(f"Menor número de palpites até vencer NO MODO INTERMEDIÁRIO = {segundoLugar}")
    if terceiroLugar > 0:
        print(f"Menor número de palpites até vencer NO MODO DIFÍCIL = {terceiroLugar}")

# Não sei como fazer os três melhores sem usar listas...