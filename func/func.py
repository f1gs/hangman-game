import os
import random


def get_words_number():
    number = 0
    for file in os.listdir(os.getcwd() + "\\words"):
        if file.endswith(".txt"):
            words_file = open(os.path.join(os.getcwd() + "\\words", file), "r").readlines()
            number += len(words_file)
    return number


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
