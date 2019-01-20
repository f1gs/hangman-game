"""
This script creates a file for each difficulty, resulting in much
less computational effort to get a word in the text file randomly.
"""

import os
from func import func

words_file = ()
file_found = False

print("+=========================+")
print("| Words Optimization Tool |")
print("+=========================+")

for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        print(f"\nFile \"{file}\" found!")
        print("Path:", os.path.join(os.getcwd(), file))

        user_input = input("Start optimization? [Y/N]: ").upper().strip()

        if user_input == "Y":
            words_file = open(os.path.join(os.getcwd(), file), "r").readlines()
            os.rename(file, file + ".old")
            file_found = True
            break

if file_found:
    easy_file = open(os.path.join(os.getcwd(), "easy.txt"), "w")
    medium_file = open(os.path.join(os.getcwd(), "medium.txt"), "w")
    hard_file = open(os.path.join(os.getcwd(), "hard.txt"), "w")

    for word in words_file:
        if 5 < func.real_word_length(word) < 10:
            easy_file.write(word)
        elif 11 < func.real_word_length(word) < 16:
            medium_file.write(word)
        elif 17 < func.real_word_length(word) < 42:
            hard_file.write(word)

    easy_file.close()
    medium_file.close()
    hard_file.close()

    print("\nOptimization held successfully.")

else:
    print("\nNo files have been optimized.")
