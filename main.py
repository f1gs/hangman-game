import os
import random


def clr_sc():
    os.system("cls" if os.name == "nt" else "clear")


def title(version):
    print("+=========+================+=======================+")
    print(f"| HANGMAN | Version: {version} | Author: Rafael Torres |")
    print("+=========+================+=======================+")


def avail_words(words_number):
    print(f"Word available: {words_number}" if words_number < 2 else f"Words available: {words_number}\n")


def dif_menu():
    print("Select a difficulty:")
    print("--------------------\n")
    print("[ 1 ] Easy")
    print("[ 2 ] Medium")
    print("[ 3 ] Hard")


def invalid_input():
    print("\nInvalid input. Please try again.")


def search_word():
    print("\nSearching a word...")


def hang(mistakes):
    if mistakes == 0:
        print("\t\t\t\t +---------+")
        print("\t\t\t\t |         |")
        print("\t\t\t\t           |")
        print("\t\t\t\t           |")
        print("\t\t\t\t           |")
        print("\t\t\t\t           |")
        print("\t\t\t\t-----------+")

    elif mistakes == 1:
        print("\t\t\t\t +---------+")
        print("\t\t\t\t |         |")
        print("\t\t\t\t 0         |")
        print("\t\t\t\t           |")
        print("\t\t\t\t           |")
        print("\t\t\t\t           |")
        print("\t\t\t\t-----------+")

    elif mistakes == 2:
        print("\t\t\t\t +---------+")
        print("\t\t\t\t |         |")
        print("\t\t\t\t 0         |")
        print("\t\t\t\t |         |")
        print("\t\t\t\t           |")
        print("\t\t\t\t           |")
        print("\t\t\t\t-----------+")

    elif mistakes == 3:
        print("\t\t\t\t +---------+")
        print("\t\t\t\t |         |")
        print("\t\t\t\t 0         |")
        print("\t\t\t\t/|         |")
        print("\t\t\t\t           |")
        print("\t\t\t\t           |")
        print("\t\t\t\t-----------+")

    elif mistakes == 4:
        print("\t\t\t\t +---------+")
        print("\t\t\t\t |         |")
        print("\t\t\t\t 0         |")
        print("\t\t\t\t/|\\        |")
        print("\t\t\t\t           |")
        print("\t\t\t\t           |")
        print("\t\t\t\t-----------+")

    elif mistakes == 5:
        print("\t\t\t\t +---------+")
        print("\t\t\t\t |         |")
        print("\t\t\t\t 0         |")
        print("\t\t\t\t/|\\        |")
        print("\t\t\t\t/          |")
        print("\t\t\t\t           |")
        print("\t\t\t\t-----------+")

    elif mistakes == 6:
        print("\t\t\t\t +---------+")
        print("\t\t\t\t |         |")
        print("\t\t\t\t 0         |")
        print("\t\t\t\t/|\\        |")
        print("\t\t\t\t/ \\        |")
        print("\t\t\t\t           |")
        print("\t\t\t\t-----------+")


def game_status(word_length, letters_used, attempts, lives, hits, mistakes):
    print(f"Word with {word_length} letter" if word_length < 2 else f"Word with {word_length} letters")
    print(f"Used letter: {str().join(letters_used)}" if len(letters_used) < 2 else f"Used letters: {str(', ').join(letters_used)}.")
    print(f"Attempt: {attempts}" if attempts < 2 else f"Attempts: {attempts}")
    print(f"Life: {lives}" if lives < 2 else f"Lives: {lives}")
    print(f"Hit: {hits}" if hits < 2 else f"Hits: {hits}")
    print(f"Mistake: {mistakes}" if mistakes < 2 else f"Mistakes: {mistakes}")


def endgame_msg(word, lives, hits, word_length):
    victory_message = [
        "Congratulations, you won! :-)",
        "Wow! You're right! :-)",
        "Nice! You won! :-)",
        "Keep it up, congratulations! :-)",
        "You won this round, congratulations! :-)",
        "Impressive! You are very good! :-)",
    ]

    defeat_message = [
        f"Oh, what a pity! The word was {word}. :-(",
        f"The word was {word}. Good luck in the next round! :-(",
        f"It was not this time, the word was {word}. :-(",
        f"You lost, the word was {word}. :-(",
        f"The word was {word}. :-(",
        f"Gee! The word was {word}. :-(",
    ]
    print(f"\a\a\a\n{random.choice(victory_message)}" if lives > 0 and hits == word_length else
          f"\a\n{random.choice(defeat_message)}")


def get_words_quantity():
    number = 0
    for file in os.listdir(os.getcwd() + "/words"):
        if file.endswith(".txt"):
            words_file = open(os.path.join(os.getcwd() + "/words", file), "r").readlines()
            number += len(words_file)
    return number


def get_dif_input():
    dif_input = str(input("\n> Select a difficulty: "))
    while str(dif_input) not in "123" or len(dif_input) < 1:
        invalid_input()
        dif_input = str(input("> Select a difficulty: "))
    return dif_input


def get_letter_input():
    letter_input = str(input("\n> Enter a letter: ")).upper().strip()
    while len(letter_input) < 1 or len(letter_input) > 1 or not str(letter_input).isalpha():
        invalid_input()
        letter_input = str(input("> Enter a letter: ")).upper().strip()
    return letter_input


def get_restart_input():
    restart_input = str(input("\n> Start over? [Y/N]: ")).upper().strip()
    while str(restart_input) not in "YN" or len(restart_input) < 1:
        invalid_input()
        restart_input = str(input("> Start over? [Y/N]: ")).upper().strip()
    return restart_input


def real_word_length(word):
    not_alpha = 0
    for i in range(len(word)):
        if not str(word[i]).isalpha():
            not_alpha += 1
    return len(word) - not_alpha


def get_word(user_input):
    min_value = 0
    max_value = 0
    file_path = ""
    if user_input == "1":
        min_value = 5
        max_value = 10
        file_path = os.path.join(os.getcwd() + "\\words\\easy.txt")
    elif user_input == "2":
        min_value = 11
        max_value = 16
        file_path = os.path.join(os.getcwd() + "\\words\\medium.txt")
    elif user_input == "3":
        min_value = 17
        max_value = 42
        file_path = os.path.join(os.getcwd() + "\\words\\hard.txt")
    file = open(file_path, "r").readlines()
    word = random.choice(file)
    word_size = real_word_length(word)
    while word_size < min_value or word_size > max_value:
        word = random.choice(file)
        word_size = real_word_length(word)
    return word.upper().strip()


def hide_reveal_letters(word, letters_used):
    display_output = []
    display_output.extend(word)
    for i in range(len(display_output)):
        if str(display_output[i]).isalpha():
            display_output[i] = "_"
        for j in range(len(letters_used)):
            if word[i] in letters_used[j]:
                display_output[i] = letters_used[j]
    return print("\n", str(" ").join(display_output).center(74), "\n")


def game_checker(word, user_input, letters_used):
    mistakes = hits = attempts = lives = 0
    if user_input in word and user_input not in letters_used:
        attempts += 1
        for i in range(len(word)):
            if user_input in word[i]:
                hits += 1
    elif user_input not in word and user_input not in letters_used:
        mistakes += 1
        attempts += 1
        lives -= 1
    return mistakes, hits, attempts, lives


while True:
    version = "0.1.2"
    words_quantity = get_words_quantity()
    mistakes = hits = attempts = 0
    lives = 6
    letters_used = []
    clr_sc()
    title(version)
    avail_words(words_quantity)
    dif_menu()
    user_input = get_dif_input()
    search_word()
    word = get_word(user_input)
    word_length = real_word_length(word)
    while lives > 0 and hits < word_length:
        clr_sc()
        title(version)
        avail_words(words_quantity)
        hang(mistakes)
        hide_reveal_letters(word, letters_used)
        game_status(word_length, letters_used, attempts, lives, hits, mistakes)
        user_input = get_letter_input()
        game_data = game_checker(word, user_input, letters_used)
        mistakes += game_data[0]
        hits += game_data[1]
        attempts += game_data[2]
        lives += game_data[3]
        if user_input not in letters_used:
            letters_used.append(user_input)
    # end game screen
    clr_sc()
    title(version)
    avail_words(words_quantity)
    hang(mistakes)
    hide_reveal_letters(word, letters_used)
    game_status(word_length, letters_used, attempts, lives, hits, mistakes)
    endgame_msg(word, lives, hits, word_length)
    user_input = get_restart_input()
    if user_input == "N":
        break
