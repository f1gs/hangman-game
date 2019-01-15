import random

path = "words/en_us.txt"


def get_words_number():
    file = open(path, "r").readlines()
    return len(file)


def get_word():
    file = open(path, "r").readlines()
    word = random.choice(file)
    return word.upper().strip()


def real_word_length(word):
    not_alpha = 0
    for i in range(len(word)):
        if not str(word[i]).isalpha():
            not_alpha += 1
    return len(word) - not_alpha


def sel_dif_word(user_input):
    if user_input == "1":
        word = get_dif_word(5, 10)
        return word

    elif user_input == "2":
        word = get_dif_word(11, 16)
        return word

    elif user_input == "3":
        word = get_dif_word(17, 42)
        return word


def get_dif_word(min_value, max_value):
    word = get_word()
    word_size = real_word_length(word)
    while word_size < min_value or word_size > max_value:
        word = get_word()
        word_size = real_word_length(word)
    return word


def hide_reveal_letters(word, letter_player):
    display_output = []
    display_output.extend(word)
    for i in range(len(display_output)):
        if str(display_output[i]).isalpha():
            display_output[i] = "_"
        for j in range(len(letter_player)):
            if word[i] in letter_player[j]:
                display_output[i] = letter_player[j]
    return print("\n", str(" ").join(display_output).center(74), "\n")


def game_checker(word, user_input, letter_used):
    mistakes = hits = attempts = lives = 0
    if user_input in word and user_input not in letter_used:
        attempts += 1
        for i in range(len(word)):
            if user_input in word[i]:
                hits += 1
    elif user_input not in word and user_input not in letter_used:
        mistakes += 1
        attempts += 1
        lives -= 1
    return mistakes, hits, attempts, lives
