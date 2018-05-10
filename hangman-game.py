'''
Made in Python 3.6.4
Hangman Game (Jogo da Forca)
Game language: PT-BR
Version: 0.0.5
Updated in: 2018-05-10
Author: Rafael F. Torres
'''

# Importando módulos
import sys
import os
import random

# Controle de versão
versao = '0.0.5'
data = '10-05-2018'  # (dd/mm/yyyy)


# Limpa a tela
def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    return


# Cabeçalho
def cabecalho():
    print('+----------------------------------------------------------------------------------------------------------------------+')
    print('|                             __                         __         ______                                             |')
    print('|                            / /___  ____ _____     ____/ /___ _   / ____/___  ______________ _                        |')
    print('|                       __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_  / __ \/ ___/ ___/ __ `/                        |')
    print('|                      / /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ / /_/ / /  / /__/ /_/ /                         |')
    print('|                      \____/\____/\__, /\____/   \__,_/\__,_/  /_/    \____/_/   \___/\__,_/                          |')
    print('|                                 /____/                                                                               |')
    print('+-----------------------------+---------------------------------------------+------------------------------------------+')
    print('|       Versão: %s         |          Atualizado em: %s          |         Autor: Rafael F. Torres          |' % (versao, data))
    print('+-----------------------------+---------------------------------------------+------------------------------------------+')
    return


# Palavras dispoíveis
def palavras_disponiveis():
    # palavra = open('words.txt', 'r').readlines()  # FUNCIONA NO PYTHON 3.6 PURO
    palavra = open(os.path.join(sys.path[0], "words.txt"), "r").readlines()  # FUNCIONA NO ANACONDA3
    print('Palavra disponível: %i' % len(palavra) if len(palavra) < 2 else 'Palavras disponíveis: %i' % len(palavra))
    return


# Menu de seleção de dificuldade
def menu_dificuldade():
    print('\n\n\n\n\n')
    print('Selecione o nível de dificuldade:\n'.center(110))
    print('[ 1 ] Fácil  '.center(110))
    print('[ 2 ] Médio  '.center(110))
    print('[ 3 ] Difícil'.center(110))
    print('\n\n\n\n\n')
    return


# Desenhos da forca
def desenho_forca(erros):
    if erros == 0:
        print(' +---------+'.center(120))
        print(' |         |'.center(120))
        print('           |'.center(120))
        print('           |'.center(120))
        print('           |'.center(120))
        print('           |'.center(120))
        print('-----------+'.center(120))

    elif erros == 1:
        print(' +---------+'.center(120))
        print(' |         |'.center(120))
        print(' 0         |'.center(120))
        print('           |'.center(120))
        print('           |'.center(120))
        print('           |'.center(120))
        print('-----------+'.center(120))

    elif erros == 2:
        print(' +---------+'.center(120))
        print(' |         |'.center(120))
        print(' 0         |'.center(120))
        print(' |         |'.center(120))
        print('           |'.center(120))
        print('           |'.center(120))
        print('-----------+'.center(120))

    elif erros == 3:
        print(' +---------+'.center(120))
        print(' |         |'.center(120))
        print(' 0         |'.center(120))
        print('/|         |'.center(120))
        print('           |'.center(120))
        print('           |'.center(120))
        print('-----------+'.center(120))

    elif erros == 4:
        print(' +---------+'.center(120))
        print(' |         |'.center(120))
        print(' 0         |'.center(120))
        print('/|\        |'.center(120))
        print('           |'.center(120))
        print('           |'.center(120))
        print('-----------+'.center(120))

    elif erros == 5:
        print(' +---------+'.center(120))
        print(' |         |'.center(120))
        print(' 0         |'.center(120))
        print('/|\        |'.center(120))
        print('/          |'.center(120))
        print('           |'.center(120))
        print('-----------+'.center(120))

    else:
        print(' +---------+'.center(120))
        print(' |         |'.center(120))
        print(' 0         |'.center(120))
        print('/|\        |'.center(120))
        print('/ \        |'.center(120))
        print('           |'.center(120))
        print('-----------+'.center(120))
    return


# Separador de underlines
def separador():
    print('   '.join(mostrar).center(120))
    return


# Status do jogo
def status_jogo():
    print('Palavra com %i letra' % total_letras if total_letras < 2 else 'Palavra com %i letras' % total_letras)
    print('Letra usada: %s' % str(jogador_lista).strip('[]') if len(jogador_lista) < 2 else 'Letras usadas: %s' % str(jogador_lista).strip('[]'))
    print('Tentativa: %i' % tentativas if tentativas < 2 else 'Tentativas: %i' % tentativas)
    print('Vida: %i' % vidas if vidas < 2 else 'Vidas: %i' % vidas)
    print('Acerto: %i' % acertos if acertos < 2 else 'Acertos: %i' % acertos)
    print('Erro: %i' % erros if erros < 2 else 'Erros: %i' % erros)
    return


# Interface (inicio)
def interface_inicio():
    limpa_tela()
    cabecalho()
    palavras_disponiveis()
    return


# Interface (meio do jogo)
def interface_jogo():
    limpa_tela()
    cabecalho()
    palavras_disponiveis()
    desenho_forca(erros)
    print()
    separador()
    print()
    status_jogo()
    return


# Mensagem de vitória ou derrota
def mensagem_resultado():
    mensagem_vitoria = ['Parabéns, você ganhou! :-)', 'Uau! Você acertou! :-)', 'Muito bom! Você ganhou! :-)',
                        'Continue assim, parabéns! :-)', 'Você ganhou essa rodada, parabéns! :-)',
                        'Impressionante! Você é muito bom! :-)']

    mensagem_derrota = ['Ah, que pena! A palavra era %s. :-(' % sorteada,
                        'A palavra era %s. Boa sorte na próxima! :-(' % sorteada,
                        'Não foi dessa vez, a palavra era %s. :-(' % sorteada,
                        'Você perdeu, a palavra era %s. :-(' % sorteada,
                        'A palavra era %s. :-(' % sorteada,
                        'Puxa vida! A palavra era %s. :-(' % sorteada]

    if vidas is not 0 and acertos is total_letras:
        print('%s' % random.choice(mensagem_vitoria))
    else:
        print('%s' % (random.choice(mensagem_derrota)))
    return


# Loop para recomeçar o jogo
recomecar = 's'
while recomecar == 's':

    # Variáveis globais
    hifens = erros = acertos = 0
    tentativas = 0
    vidas = 6

    #####################
    # Interface inicial #
    #####################
    interface_inicio()

    # Busca uma palavra aleatória
    # palavra = open('words.txt', 'r').readlines()  # FUNCIONA NO PYTHON 3.6 PURO
    palavra = open(os.path.join(sys.path[0], "words.txt"), "r").readlines()  # FUNCIONA NO ANACONDA3
    computador = random.choice(palavra)

    for i in range(len(computador)):
        if computador[i] in '-':
            hifens += 1

    # Menu de seleção de dificuldade
    menu_dificuldade()
    dificuldade = input('> Dificuldade desejada: ').strip()

    #############################################################################
    # Mudar a linha abaixo caso haja mais de três opções no menu de dificuldade #
    #############################################################################
    while dificuldade in '4567890[^!?@#$%¨&*¹²³£¢¬ª°º()=-+qwertyuiopasdfghjklzxcvbnmáéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ:;,./\|{}~´] ':
        dificuldade = input('> Dificuldade desejada: ').strip()

    # Dificuldade
    if dificuldade == '1':
        while len(computador)-hifens < 5 or len(computador)-hifens > 10:
            computador = random.choice(palavra)
    elif dificuldade == '2':
        while len(computador)-hifens < 11 or len(computador)-hifens > 16:
            computador = random.choice(palavra)
    else:
        while len(computador)-hifens < 17:
            computador = random.choice(palavra)

    # Formata a palavra escolhida e a coloca em uma lista
    computador = computador.upper().strip()
    sorteada = computador
    computador = list(computador)

    # Mostra o número de letras levando em consideração os hífens
    for i in range(len(computador)):
        if computador[i] in '-':
            hifens += 1
    total_letras = len(computador) - hifens

    # Listas para guardar letras ocultas e para prevenir a repetição delas pelo jogador
    mostrar = list()
    mostrar.extend(computador)
    jogador_lista = list()

    # Oculta letras e revela hífens
    for i in range(len(mostrar)):
        mostrar[i] = '_'
    for i in range(len(computador)):
        if computador[i] in '-':
            mostrar[i] = '-'

    # Loop até o jogador errar ou acertar tudo
    while vidas is not 0 and acertos is not total_letras:

        #################################
        # Início da 'interface' do jogo #
        #################################
        interface_jogo()

        # Entrada do jogador
        jogador = input('\n> Sua vez, digite uma letra: ').upper().strip()
        while len(jogador) > 1 or len(jogador) < 1:
            jogador = input('> Sua vez, digite uma letra: ').upper().strip()

        # Revela letras com hífen e substitui o underline pelas letras que foram adivinhadas pelo jogador
        for i in range(len(computador)):
            if computador[i] in '-':
                mostrar[i] = '-'
        for i in range(len(computador)):
            if computador[i] in jogador:
                mostrar[i] = jogador[0]

        # Verifica acertos ou erros
        if jogador in '[^!?@#$%¨&*¹²³£¢¬ª°º()=-+0123456789áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ:;,./\|{}~´ ] ':
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
    interface_jogo()

    # Revela letras com hífen e substitui o underline pelas letras que foram adivinhadas pelo jogador
    for i in range(len(computador)):
        if computador[i] in '-':
            mostrar[i] = '-'
    for i in range(len(computador)):
        if computador[i] in jogador:
            mostrar[i] = jogador[0]

    # Mensagem de vitória ou derrota
    mensagem_resultado()

    # Recomeça o jogo
    recomecar = input('> Deseja recomeçar? [S/N]').lower().strip()
