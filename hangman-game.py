'''
Jogo da forca (Hangman Game)
Versão: 1.00
Atualizado em: 20/02/18 (dd/mm/yy)
Autor: Rafael F. Torres
'''

# Importando módulos
import random
import os

# Cabeçalho
cabecalho = str('''+======================================================================================================================+
|                             __                         __         ______                                             |
|                            / /___  ____ _____     ____/ /___ _   / ____/___  ______________ _                        |
|                       __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_  / __ \/ ___/ ___/ __ `/                        |
|                      / /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ / /_/ / /  / /__/ /_/ /                         |
|                      \____/\____/\__, /\____/   \__,_/\__,_/  /_/    \____/_/   \___/\__,_/                          |
|                                 /____/                                                                               |
+======================================================================================================================+
|       Versão: 1.00          |           Atualizado em: 20/02/18          |           Autor: Rafael F. Torres         |
+======================================================================================================================+''')

# Desenhos da forca
forca0 = str('''                                                     +---------+
                                                     |         |
                                                               |
                                                               |
                                                               |
                                                               |
                                                               |
                                                               |
                                                    -----------+''')

forca1 = str('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                               |
                                                               |
                                                               |
                                                               |
                                                               |
                                                    -----------+''')

forca2 = str('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                     |         |
                                                               |
                                                               |
                                                               |
                                                               |
                                                    -----------+''')

forca3 = str('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                    /|         |
                                                               |
                                                               |
                                                               |
                                                               |
                                                    -----------+''')

forca4 = str('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                    /|\        |
                                                               |
                                                               |
                                                               |
                                                               |
                                                    -----------+''')

forca5 = str('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                    /|\        |
                                                     |         |
                                                               |
                                                               |
                                                               |
                                                    -----------+''')

forca6 = str('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                    /|\        |
                                                     |         |
                                                    /          |
                                                               |
                                                               |
                                                    -----------+''')

forca7 = str('''                                                     +---------+
                                                     |         |
                                                     0         |
                                                    /|\        |
                                                     |         |
                                                    / \        |
                                                               |
                                                               |
                                                    -----------+''')

recomecar = str('s')

# Loop para recomeçar o jogo
while recomecar == str('s'):

    # Variáveis globais
    hifens = erros = acertos = int(0)
    tentativas = int(1)
    vidas = int(7)

    # Busca uma palavra aleatória e a separa
    palavra = open('words.txt', 'r').readlines()
    computador = random.choice(palavra)
    computador = str(computador).upper().strip()
    sorteada = computador
    computador = list(computador)

    # Listas para guardar letras ocultadas e para prevenir a repetição delas pelo jogador
    mostrar = []
    mostrar.extend(computador)
    jogador_lista = []

    # Mostra o número de letras levando em consideração os hífens
    for i in range(len(computador)):
        if computador[i] in str('-'):
            hifens += 1
    total_letras = len(computador) - hifens

    # Ocultador de letras e revelador de hífens
    for i in range(len(mostrar)):
        mostrar[i] = str('_')
    for i in range(len(computador)):
        if computador[i] in str('-'):
            mostrar[i] = str('-')
            jogador_lista.append(str('-'))

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
        # print('[ TESTE ] - Computador:', str(computador))

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
        elif erros == 6:
            print(forca6)
        else:
            print(forca7)

        print('')

        # Separador
        print('   '.join(mostrar).center(120))

        print('')

        # Total de letras na palavra
        print('Palavra com %d letra' % total_letras if total_letras < 2 else 'Palavra com %d letras' % total_letras)

        # Letras usadas pelo jogador
        print('Letra usada: %s' % str(jogador_lista).strip('[]') if len(jogador_lista) < 2 else 'Letras usadas: %s' % str(jogador_lista).strip('[]'))

        # Status do jogo
        print('Tentativa: %d' % tentativas if tentativas < 2 else 'Tentativas: %d' % tentativas)
        print('Vida: %d' % vidas if vidas < 2 else 'Vidas: %d' % vidas)
        print('Acerto: %d' % acertos if acertos < 2 else 'Acertos: %d' % acertos)
        print('Erro: %d' % erros if erros < 2 else 'Erros: %d' % erros)

        # Entrada do jogador
        jogador = input(str('\nSua vez, digite uma letra: ')).upper().strip()

        # Revela letras com hífen e substitui o underline pelas letras que foram adivinhadas pelo jogador
        for i in range(len(computador)):
            if computador[i] in str('-'):
                mostrar[i] = str('-')
        for i in range(len(computador)):
            if computador[i] in jogador:
                mostrar[i] = str(jogador)[0]

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

    # print('')

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
    elif erros == 6:
        print(forca6)
    else:
        print(forca7)

    print('')

    # Separador
    print('   '.join(mostrar).center(120))

    print('')

    # Total de letras na palavra
    print('Palavra com %d letra' % total_letras if total_letras < 2 else 'Palavra com %d letras' % total_letras)

    # Letras usadas pelo jogador
    print('Letra usada: %s' % str(jogador_lista).strip('[]') if len(jogador_lista) < 2 else 'Letras usadas: %s' % str(jogador_lista).strip('[]'))

    # Status do jogo
    print('Tentativa: %d' % tentativas if tentativas < 2 else 'Tentativas: %d' % tentativas)
    print('Vida: %d' % vidas if vidas < 2 else 'Vidas: %d' % vidas)
    print('Acerto: %d' % acertos if acertos < 2 else 'Acertos: %d' % acertos)
    print('Erro: %d' % erros if erros < 2 else 'Erros: %d' % erros)

    # Revela letras com hífen e substitui o underline pelas letras que foram adivinhadas pelo jogador
    for i in range(len(computador)):
        if computador[i] in str('-'):
            mostrar[i] = str('-')
    for i in range(len(computador)):
        if computador[i] in jogador:
            mostrar[i] = str(jogador)[0]

    # Mensagem de vitória ou derrota
    if vidas != 0 and acertos == total_letras:
        print('\nParabéns! Você ganhou! :-)')
    else:
        print('\nA palavra era %s. Você perdeu! :-(' % sorteada)

    # Recomeça o jogo
    recomecar = str(input('\nDeseja recomeçar? [S/N]')).lower().strip()
