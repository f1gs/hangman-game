import random


def get_file():
    path = "words/en_us.txt"
    file = open(path, "r").readlines()
    return len(file)


def get_word():
    path = "words/en_us.txt"
    file = open(path, "r").readlines()
    word = random.choice(file)
    return word.upper().strip()


def real_length_word(word):
    hyphens = apostrophes = spaces = 0
    for i in range(len(word)):
        if word[i] in "-":
            hyphens += 1
        if word[i] in "'":
            apostrophes += 1
        if word[i] in " ":
            spaces += 1
    return len(word) - (hyphens + apostrophes + spaces)


def dif_word(min, max):
    word = get_word()
    word_size = real_length_word(word)
    while word_size < min or word_size >= max:
        word = get_word()
        word_size = real_length_word(word)
    return word


def hide_reveal_letters(word, letter_player):
    display_output = []
    display_output.extend(word)
    # hide only letters
    for i in range(len(display_output)):
        if str(display_output[i]).isalpha():
            display_output[i] = "_"
        # reveal letters
        for j in range(len(letter_player)):
            if word[i] in letter_player[j]:
                display_output[i] = letter_player[j]
    return print("\n", str(" ").join(display_output).center(74), "\n")


def game_checker(word, letter_input, letter_used):
    mistakes = hits = attempts = lives = 0
    if letter_input in word and letter_input not in letter_used:
        attempts += 1
        for i in range(len(word)):
            if letter_input in word[i]:
                hits += 1
    elif letter_input in word and letter_input in letter_used:
        attempts += 0
        hits += 0
        mistakes += 0
    elif letter_input not in word and letter_input in letter_used:
        attempts += 0
        hits += 0
        mistakes += 0
    else:
        attempts += 1
        lives -= 1
        mistakes += 1
    return mistakes, hits, attempts, lives
