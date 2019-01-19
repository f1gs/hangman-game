import os


def clr_sc():
    os.system("cls" if os.name == "nt" else "clear")


def title():
    print("+==================+================+=======================+")
    print("| HANGMAN THE GAME | Version: 0.1.1 | Author: Rafael Torres |")
    print("+==================+================+=======================+")


def avail_words(words_number):
    print(f"Word available: {words_number}" if words_number < 2 else f"Words available: {words_number}\n")


def dif_menu():
    print("Select a difficulty:")
    print("--------------------\n")
    print("[ 1 ] Easy")
    print("[ 2 ] Medium")
    print("[ 3 ] Hard")


def game_status(word_length, letter_used, attempts, lives, hits, mistakes):
    print(f"Word with {word_length} letter" if word_length < 2 else f"Word with {word_length} letters")
    print(f"Used letter: {str().join(letter_used)}" if len(letter_used) < 2 else f"Used letters: {str(', ').join(letter_used)}.")
    print(f"Attempt: {attempts}" if attempts < 2 else f"Attempts: {attempts}")
    print(f"Life: {lives}" if lives < 2 else f"Lives: {lives}")
    print(f"Hit: {hits}" if hits < 2 else f"Hits: {hits}")
    print(f"Mistake: {mistakes}" if mistakes < 2 else f"Mistakes: {mistakes}")
