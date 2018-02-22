'''
Made in Python 3.6.4
Hangman Game (Jogo da Forca)
Game language: pt-BR
Version: 0.0.2
Updated in: 2018-02-21
Author: Rafael F. Torres
'''

# Importando módulos
import random
import os
from pygame import mixer

# Controle de versão
versao = '0.0.3'
data = '22-02-2018'

# Loop de música com o pygame
mixer.init()
mixer.music.set_volume(0.33)  # Padrão: (0.15)
mixer.music.load('music.xm')
mixer.music.play(loops=-1)

# Cabeçalho
cabecalho = ('''+----------------------------------------------------------------------------------------------------------------------+
|                             __                         __         ______                                             |
|                            / /___  ____ _____     ____/ /___ _   / ____/___  ______________ _                        |
|                       __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_  / __ \/ ___/ ___/ __ `/                        |
|                      / /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ / /_/ / /  / /__/ /_/ /                         |
|                      \____/\____/\__, /\____/   \__,_/\__,_/  /_/    \____/_/   \___/\__,_/                          |
|                                 /____/                                                                               |
+-----------------------------+---------------------------------------------+------------------------------------------+
|       Versão: %s         |          Atualizado em %s           |         Autor: Rafael F. Torres          |
+-----------------------------+---------------------------------------------+------------------------------------------+''' % (versao, data))

# Desenhos da forca
forca0 = ('''                                                     +---------+
                                                     |         |
                                                               |
                                                               |
                                                               |
                                                               |
                                                    -----------+''')

forca1 = ('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                               |
                                                               |
                                                               |
                                                    -----------+''')

forca2 = ('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                     |         |
                                                               |
                                                               |
                                                    -----------+''')

forca3 = ('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                    /|         |
                                                               |
                                                               |
                                                    -----------+''')

forca4 = ('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                    /|\        |
                                                               |
                                                               |
                                                    -----------+''')

forca5 = ('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                    /|\        |
                                                    /          |
                                                               |
                                                    -----------+''')

forca6 = ('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                    /|\        |
                                                    / \        |
                                                               |
                                                    -----------+''')

recomecar = 's'

# Loop para recomeçar o jogo
while recomecar == 's':

    palavra = open('words.txt', 'r').readlines()

    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')

    print(cabecalho)
    print('Palavra disponível: %d' % len(palavra) if len(palavra) < 2 else 'Palavras disponíveis: %d' % len(palavra))

    # Seleção da dificuldade
    dificuldade = int(input('''



                                        Selecione o nível de dificuldade:



                                                [ 1 ] Fácil 
                                                [ 2 ] Médio 
                                                [ 3 ] Difícil 
                                                          
                                                          
                                                           
                                        Opção: '''))

    # Variáveis globais
    hifens = erros = acertos = 0
    tentativas = 1
    vidas = 6

    # Busca uma palavra aleatória e a coloca em uma lista
    palavra = open('words.txt', 'r').readlines()
    computador = random.choice(palavra)

    for i in range(len(computador)):
        if computador[i] in '-':
            hifens += 1

    # Dificuldade fácil
    if dificuldade == 1:
        while len(computador)-hifens < 4 or len(computador)-hifens > 10:
            computador = random.choice(palavra)
    # Dificuldade média
    elif dificuldade == 2:
        while len(computador)-hifens < 11 or len(computador)-hifens > 16:
            computador = random.choice(palavra)
    # Dificuldade difícil
    else:
        while len(computador)-hifens < 17:
            computador = random.choice(palavra)

    # Formatando a palavra escolhida e colocando-a em uma lista
    computador = computador.upper().strip()
    sorteada = computador
    computador = list(computador)

    # Mostra o número de letras levando em consideração os hífens
    for i in range(len(computador)):
        if computador[i] in '-':
            hifens += 1
    total_letras = len(computador) - hifens

    # Listas para guardar letras ocultadas e para prevenir a repetição delas pelo jogador
    mostrar = list()
    mostrar.extend(computador)
    jogador_lista = list()

    # Ocultador de letras e revelador de hífens
    for i in range(len(mostrar)):
        mostrar[i] = '_'
    for i in range(len(computador)):
        if computador[i] in '-':
            mostrar[i] = '-'
            jogador_lista.append('-')

    # Loop até o jogador errar ou acertar tudo
    while vidas != 0 and acertos != total_letras:

        #################################
        # Início da 'Interface' do jogo #
        #################################

        # Limpador de tela
        os.system('cls' if os.name == 'nt' else 'clear')

        print(cabecalho)
        print('Palavra disponível: %d' % len(palavra) if len(palavra) < 2 else 'Palavras disponíveis: %d' % len(palavra))

        # Apenas para testes
        # print('[ TESTE ] - Computador:' % computador)

        # Desenho da forca
        if erros == 0:
            print(forca0)
        elif erros == 1:
            print(forca1)
        elif erros == 2:
            print(forca2)
        elif erros == 3:
            print(forca3)
        elif erros == 4:
            print(forca4)
        elif erros == 5:
            print(forca5)
        else:
            print(forca6)

        print('')

        # Separador
        print('   '.join(mostrar).center(120))

        print('')

        # Status do jogo
        print('Palavra com %d letra' % total_letras if total_letras < 2 else 'Palavra com %d letras' % total_letras)
        print('Letra usada: %s' % str(jogador_lista).strip('[]') if len(jogador_lista) < 2 else 'Letras usadas: %s' % str(jogador_lista).strip('[]'))
        print('Tentativa: %d' % tentativas if tentativas < 2 else 'Tentativas: %d' % tentativas)
        print('Vida: %d' % vidas if vidas < 2 else 'Vidas: %d' % vidas)
        print('Acerto: %d' % acertos if acertos < 2 else 'Acertos: %d' % acertos)
        print('Erro: %d' % erros if erros < 2 else 'Erros: %d' % erros)

        # Entrada do jogador
        jogador = input('\nSua vez, digite uma letra: ').upper().strip()
        while len(jogador) > 1 or len(jogador) == 0:
            jogador = input('\nSua vez, digite uma letra: ').upper().strip()

        # Revela letras com hífen e substitui o underline pelas letras que foram adivinhadas pelo jogador
        for i in range(len(computador)):
            if computador[i] in '-':
                mostrar[i] = '-'
        for i in range(len(computador)):
            if computador[i] in jogador:
                mostrar[i] = jogador[0]

        # Verificador de acertos ou erros
        if jogador in str('[^-0123456789áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]'):
            tentativas += 0
            acertos += 0
            erros += 0
        elif jogador in computador and jogador not in jogador_lista:
            jogador_lista.append(jogador)
            tentativas += 1
            for i in range(len(computador)):
                if jogador in computador[i]:
                    acertos += 1
        elif jogador in computador and jogador in jogador_lista:
            tentativas += 0
            acertos += 0
            erros += 0
        elif jogador not in computador and jogador in jogador_lista:
            tentativas += 0
            acertos += 0
            erros += 0
        else:
            jogador_lista.append(jogador)
            tentativas += 1
            vidas -= 1
            erros += 1

    #######################
    # Tela de fim de jogo #
    #######################

    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')

    print(cabecalho)
    print('Palavra disponível: %d' % len(palavra) if len(palavra) < 2 else 'Palavras disponíveis: %d' % len(palavra))

    # Desenho da forca
    if erros == 0:
        print(forca0)
    elif erros == 1:
        print(forca1)
    elif erros == 2:
        print(forca2)
    elif erros == 3:
        print(forca3)
    elif erros == 4:
        print(forca4)
    elif erros == 5:
        print(forca5)
    else:
        print(forca6)

    print('')

    # Separador
    print('   '.join(mostrar).center(120))

    print('')

    # Status do jogo
    print('Palavra com %d letra' % total_letras if total_letras < 2 else 'Palavra com %d letras' % total_letras)
    print('Letra usada: %s' % str(jogador_lista).strip('[]') if len(jogador_lista) < 2 else 'Letras usadas: %s' % str(jogador_lista).strip('[]'))
    print('Tentativa: %d' % tentativas if tentativas < 2 else 'Tentativas: %d' % tentativas)
    print('Vida: %d' % vidas if vidas < 2 else 'Vidas: %d' % vidas)
    print('Acerto: %d' % acertos if acertos < 2 else 'Acertos: %d' % acertos)
    print('Erro: %d' % erros if erros < 2 else 'Erros: %d' % erros)

    # Revela letras com hífen e substitui o underline pelas letras que foram adivinhadas pelo jogador
    for i in range(len(computador)):
        if computador[i] in '-':
            mostrar[i] = '-'
    for i in range(len(computador)):
        if computador[i] in jogador:
            mostrar[i] = jogador[0]

    # Mensagem de vitória ou derrota
    if vidas != 0 and acertos == total_letras:
        print('\nParabéns! Você ganhou! :-)')
    else:
        print('\nA palavra era %s. Você perdeu! :-(' % sorteada)

    # Recomeça o jogo
    recomecar = input('\nDeseja recomeçar? [S/N]').lower().strip()
