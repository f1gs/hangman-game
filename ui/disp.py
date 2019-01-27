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
