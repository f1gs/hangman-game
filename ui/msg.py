import random


def invalid_input():
    print("\nInvalid input. Please try again.")


def search_word():
    print("\nSearching a word...")


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
