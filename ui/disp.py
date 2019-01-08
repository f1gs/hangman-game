import os


def clr_sc():
    os.system("cls" if os.name == "nt" else "clear")


def title():
    print("+==================+================+=======================+")
    print("| HANGMAN THE GAME | Version: 0.1.0 | Author: Rafael Torres |")
    print("+==================+================+=======================+")


def avail_words(number_words):
    print(f"Word available: {number_words}" if number_words < 2 else f"Words available: {number_words}\n")


def dif_menu():
    print("Select a difficulty:\n--------------------\n\n[ 1 ] Easy\n[ 2 ] Medium\n[ 3 ] Hard")


def game_status(word_length, letter_used, attempts, lives, hits, mistakes):
    if word_length < 1:
        print(f"Word with none letter.")
    elif word_length == 1:
        print(f"Word with {word_length} letter.")
    else:
        print(f"Word with {word_length} letters.")
    if len(letter_used) < 1:
        print(f"Used letter: none")
    elif len(letter_used) == 1:
        print("Used letter: %s." % str(letter_used).replace("[", "").replace("]", "").replace("'", ""))
    else:
        print("Used letters: %s." % str(letter_used).replace("[", "").replace("]", "").replace("'", ""))
    if attempts < 1:
        print(f"Attempt: none")
    elif attempts == 1:
        print(f"Attempt: {attempts}")
    else:
        print(f"Attempts: {attempts}")
    if lives < 1:
        print(f"Live: none")
    elif lives == 1:
        print(f"Live: {lives}")
    else:
        print(f"Lives: {lives}")
    if hits < 1:
        print(f"Hit: none")
    elif hits == 1:
        print(f"Hit: {hits}")
    else:
        print(f"Hits: {hits}")
    if mistakes < 1:
        print(f"Mistake: none")
    elif lives == 1:
        print(f"Mistake: {mistakes}")
    else:
        print(f"Mistakes: {mistakes}")
