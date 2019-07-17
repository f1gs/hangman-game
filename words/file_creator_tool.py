"""
This script separates the words from a ".txt" file into three files with their respective difficulties.

For example:

file.txt (input)
|
|
|
+ ----- easy.txt (output)
|
+ ----- medium.txt (output)
|
+ ----- hard.txt (output)
"""

import os


def real_word_length(word):
    not_alpha = 0
    for i in range(len(word)):
        if not str(word[i]).isalpha():
            not_alpha += 1
    return len(word) - not_alpha


version = 0.1
print("+===================+==============+")
print(f"| File creator tool | Version: {version} |")
print("+===================+==============+")
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        easy_words_counter = medium_words_counter = hard_words_counter = 0
        easy_words_buffer = medium_words_buffer = hard_words_buffer = ""
        print(f"\nFile \"{file}\" found!")
        print("Path:", os.path.join(os.getcwd(), file))
        print("\nThis file has:")
        words_file = open(os.path.join(os.getcwd(), file), "r").readlines()
        for line in words_file:
            if 5 <= real_word_length(line) <= 10:
                easy_words_counter += 1
                easy_words_buffer += easy_words_buffer
            if 11 <= real_word_length(line) <= 16:
                medium_words_counter += 1
                medium_words_buffer += medium_words_buffer
            if 17 <= real_word_length(line) <= 42:
                hard_words_counter += 1
                hard_words_buffer += hard_words_buffer
        print(f"Easy words: {easy_words_counter}")
        print(f"Medium words: {medium_words_counter}")
        print(f"Hard words: {hard_words_counter}")
        user_input = input("\nA file will be created for each difficulty.\nDo you want to start the process? [Y/N]: ").lower().strip()
        if user_input == "y":
            os.rename(file, file + ".OLD")
            easy_file = open(os.path.join(os.getcwd(), "easy.txt"), "w")
            medium_file = open(os.path.join(os.getcwd(), "medium.txt"), "w")
            hard_file = open(os.path.join(os.getcwd(), "hard.txt"), "w")
            for line in words_file:
                if 5 <= real_word_length(line) <= 10:
                    easy_file.write(line)
                if 11 <= real_word_length(line) <= 16:
                    medium_file.write(line)
                if 17 <= real_word_length(line) <= 42:
                    hard_file.write(line)
            easy_file.close()
            medium_file.close()
            hard_file.close()
            print("\nThe files were created successfully.")
            input("\nPress <ENTER> to continue...")
            break
        else:
            print("\nNo files have been created.")
            input("\nPress <ENTER> to continue...")
