'''
Python 3.6
Hangman Game
Version: 0.0.7
Update: 2018-07-09 (yyyy/mm/dd)
Author: Rafael Torres
'''

# imports
import sys
import os
import random

# version
version = '0.0.7'
date = '2018-07-09'

# align text
align = int(77)

# clean screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

# language of words menu
def language_words_menu():
    # difficulty screen
    print('''\n\n\n\n\n''')
    print('''Select the language for the words drawn in the game:\n'''.center(align))
    print('''[ 1 ] Portuguese                                      '''.center(align))
    print('''[ 2 ] English                                         '''.center(align))
    print('''\n\n\n\n\n''')
    return

# difficulty menu
def difficulty_menu():
    # difficulty screen
    print('''\n\n\n\n\n''')
    print('''Select a difficulty:\n'''.center(align))
    print('''[ 1 ] Easy            '''.center(align))
    print('''[ 2 ] Medium          '''.center(align))
    print('''[ 3 ] Hard            '''.center(align))
    print('''\n\n\n\n\n''')
    return

# header
def header():
    print('''+------------------------------------------------------+-----------------------+''')
    print('''|      __  __                                          |                       |''')
    print('''|     / / / /___ _____  ____ _____ ___  ____ _____     | Version: %s        |''' % (version))
    print('''|    / /_/ / __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ \    |                       |''')
    print('''|   / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /    | Date: %s      |''' % (date))
    print('''|  /_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_/     |                       |''')
    print('''|                    /____/                            | Author: Rafael Torres |''')
    print('''+------------------------------------------------------+-----------------------+''')
    return

# hangman drawing
def hangman_drawing():
    if mistakes == 0:
        print(' +---------+'.center(align))
        print(' |         |'.center(align))
        print('           |'.center(align))
        print('           |'.center(align))
        print('           |'.center(align))
        print('           |'.center(align))
        print('-----------+'.center(align))

    elif mistakes == 1:
        print(' +---------+'.center(align))
        print(' |         |'.center(align))
        print(' 0         |'.center(align))
        print('           |'.center(align))
        print('           |'.center(align))
        print('           |'.center(align))
        print('-----------+'.center(align))

    elif mistakes == 2:
        print(' +---------+'.center(align))
        print(' |         |'.center(align))
        print(' 0         |'.center(align))
        print(' |         |'.center(align))
        print('           |'.center(align))
        print('           |'.center(align))
        print('-----------+'.center(align))

    elif mistakes == 3:
        print(' +---------+'.center(align))
        print(' |         |'.center(align))
        print(' 0         |'.center(align))
        print('/|         |'.center(align))
        print('           |'.center(align))
        print('           |'.center(align))
        print('-----------+'.center(align))

    elif mistakes == 4:
        print(' +---------+'.center(align))
        print(' |         |'.center(align))
        print(' 0         |'.center(align))
        print('/|\        |'.center(align))
        print('           |'.center(align))
        print('           |'.center(align))
        print('-----------+'.center(align))

    elif mistakes == 5:
        print(' +---------+'.center(align))
        print(' |         |'.center(align))
        print(' 0         |'.center(align))
        print('/|\        |'.center(align))
        print('/          |'.center(align))
        print('           |'.center(align))
        print('-----------+'.center(align))

    else:
        print(' +---------+'.center(align))
        print(' |         |'.center(align))
        print(' 0         |'.center(align))
        print('/|\        |'.center(align))
        print('/ \        |'.center(align))
        print('           |'.center(align))
        print('-----------+'.center(align))
    return

# game status
def game_status():
    print('Word with %i letter.' % total_letters if total_letters < 2 else 'Word with %i letters.' % total_letters)
    print('Used letter: %s.' % str(player_list).replace("[", "").replace("]", "").replace("'", "") if len(player_list) < 2 else 'Used letters: %s.' % str(player_list).replace("[", "").replace("]", "").replace("'", ""))
    print('Attempt: %i' % attempts if attempts < 2 else 'Attempts: %i' % attempts)
    print('Life: %i' % lives if lives < 2 else 'Lives: %i' % lives)
    print('Hit: %i' % hits if hits < 2 else 'Hits: %i' % hits)
    print('Mistake: %i' % mistakes if mistakes < 2 else 'Mistakes: %i' % mistakes)
    return

# endgame message
def endgame_message():
    victory_message = [
        "Congratulations, you won! :-)",
        "Wow! You're right! :-)",
        "Nice!, you won! :-)",
        "Keep it up, congratulations! :-)",
        "You won this round, congratulations! :-)",
        "Impressive! You are very good! :-)",
    ]

    defeat_message = [
        "Oh, what a pity! The word was %s. :-(" % drawn_word,
        "The word was %s. Good luck in the next round! :-(" % drawn_word,
        "It was not this time, the word was %s. :-(" % drawn_word,
        "You lost, the word was %s. :-(" % drawn_word,
        "The word was %s. :-(" % drawn_word,
        "Gee! The word was %s. :-(" % drawn_word,
    ]

    if lives != 0 and hits == total_letters:
        print('%s' % random.choice(victory_message))
    else:
        print('%s' % random.choice(defeat_message))
    return

# underlines tab
def underlines_tab():
    print('   '.join(show).center(align))
    return

# shows available words on the screen
def available_words():
    # works in python 3.6
    # word = open("words.txt", "r").readlines()

    # works in anaconda3
    if language_input == 1:
        word = open(os.path.join(sys.path[0], "words_pt-br.txt"), "r").readlines()
        language = 'Portuguese'
    elif language_input == 2:
        word = open(os.path.join(sys.path[0], "words_en-us.txt"), "r").readlines()
        language = 'English'
    return print(language,'word vailable: %i' % len(word) if len(word) < 2 else 'words available: %i' % len(word))

# start interface
def interface_start():
    clear_screen()
    header()
    return

# mid game interface
def interface_game():
    clear_screen()
    header()
    available_words()
    hangman_drawing()
    print()
    underlines_tab()
    print()
    game_status()
    return

###################
# starts the game #
###################
restart = 'y'
while restart == 'y':

    # global variables
    mistakes = hits = attempts = 0
    lives = 6

    # start interface and language selection for drawn words
    interface_start()
    language_words_menu()

    # language input
    language_input = int(input("> Select an option: "))
    while language_input < 1 or language_input > 2:
        language_input = int(input("> Select an option: "))

    #### search a random word
    #### works in python 3.6
    #### word = open("words_pt-br.txt", "r").readlines()
    # works in anaconda3
    # portuguese
    if language_input == 1:
        word = open(os.path.join(sys.path[0], "words_pt-br.txt"), "r").readlines()
        computer = random.choice(word)
    # english
    elif language_input == 2:
        word = open(os.path.join(sys.path[0], "words_en-us.txt"), "r").readlines()
        computer = random.choice(word)

    # removes spaces from drawn word
    computer = computer.upper().strip()
    
    # counts hyphens and apostrophes
    hyphens = apostrophes = total_letters = 0
    for i in range(len(computer)):
        if computer[i] in "-":
            hyphens += 1
        if computer[i] in "'":
            apostrophes += 1
    total_letters = len(computer) - (hyphens + apostrophes)

    # difficulty screen
    interface_start()
    difficulty_menu()

    # difficulty input
    difficulty = int(input("> Select an option: "))
    while difficulty < 1 or difficulty > 3:
        difficulty = int(input("> Select an option: "))
    
    # difficulty selection
    if difficulty == 1:
        while total_letters < 5 or total_letters >= 10:
            computer = random.choice(word)
            computer = computer.upper().strip()
            hyphens = apostrophes = total_letters = 0
            for i in range(len(computer)):
                if computer[i] in "-":
                    hyphens += 1
                if computer[i] in "'":
                    apostrophes += 1
            total_letters = len(computer) - (hyphens + apostrophes)

    elif difficulty == 2:
        while total_letters < 11 or total_letters >= 16:
            computer = random.choice(word)
            computer = computer.upper().strip()
            hyphens = apostrophes = total_letters = 0
            for i in range(len(computer)):
                if computer[i] in "-":
                    hyphens += 1
                if computer[i] in "'":
                    apostrophes += 1
            total_letters = len(computer) - (hyphens + apostrophes)

    elif difficulty == 3:
        while total_letters <= 17:
            computer = random.choice(word)
            computer = computer.upper().strip()
            hyphens = apostrophes = total_letters = 0
            for i in range(len(computer)):
                if computer[i] in "-":
                    hyphens += 1
                if computer[i] in "'":
                    apostrophes += 1
            total_letters = len(computer) - (hyphens + apostrophes)

    # formats the chosen word
    computer = computer.upper().strip()
    drawn_word = computer
    computer = list(computer)

    # lists to store hidden letters and to prevent them from being repeated by the player
    show = []
    show.extend(computer)
    player_list = []

    # hide letters and show hyphens and apostrophes
    for i in range(len(show)):
        show[i] = "_"
    for j in range(len(computer)):
        if computer[j] in "-":
            show[j] = "-"
        if computer[j] in "'":
            show[j] = "'"

    # repeat until the player misses or hits everything
    while lives != 0 and hits != total_letters:

        # mid game interface
        interface_game()

        # player input
        player = input("\n> It's your turn, type a letter: ").upper().strip()
        while len(player) > 1 or len(player) < 1:
            player = input("\n> It's your turn, type a letter: ").upper().strip()
        
        # reveals letters, hyphens and apostrophes
        for i in range(len(computer)):
            if computer[i] in "-":
                show[i] = "-"
            if computer[i] in "'":
                show[i] = "'"
        for j in range(len(computer)):
            if computer[j] in player:
                show[j] = player[0]

        # checks for hits or mistakes
        if player in "[^!?@#$%¨&*¹²³£¢¬ª°º()=-+0123456789áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ:;,./{}~´ ] ":
            attempts += 0
            hits += 0
            mistakes += 0
        elif player in computer and player not in player_list:
            player_list.append(player)
            attempts += 1
            for i in range(len(computer)):
                if player in computer[i]:
                    hits += 1
        elif player in computer and player in player_list:
            attempts += 0
            hits += 0
            mistakes += 0
        elif player not in computer and player in player_list:
            attempts += 0
            hits += 0
            mistakes += 0
        else:
            player_list.append(player)
            attempts += 1
            lives -= 1
            mistakes += 1
        
        # endgame screen
        interface_game()

        # reveals letters, hyphens and apostrophes (again)
        for i in range(len(computer)):
            if computer[i] in "-":
                show[i] = "-"
            if computer[i] in "'":
                show[i] = "'"
        for j in range(len(computer)):
            if computer[j] in player:
                show[j] = player[0]

        # victory or defeat message
        endgame_message()

    # restart the game
    restart = input('> Do you want to start over? [Y/N]').lower().strip()
