from func import func
from ui import disp
from ui import msg
from ui import dwg

while True:
    words_number = func.get_words_number()
    mistakes = hits = attempts = 0
    lives = 6
    word = ()
    letter_display = []
    letter_used = []

    disp.clr_sc()
    disp.title()
    disp.avail_words(words_number)
    disp.dif_menu()

    input_dif = str(input("\n> Select a difficulty: "))
    while str(input_dif) not in "123" or len(input_dif) < 1:
        msg.invalid_input()
        input_dif = str(input("> Select a difficulty: "))

    if input_dif == "1":
        msg.search_word()
        word = func.dif_word(5, 10)

    elif input_dif == "2":
        msg.search_word()
        word = func.dif_word(11, 16)

    elif input_dif == "3":
        msg.search_word()
        word = func.dif_word(17, 42)

    letter_display.extend(word)
    word_length = func.real_word_length(word)

    while lives > 0 and hits < word_length:
        disp.clr_sc()
        disp.title()
        disp.avail_words(words_number)
        dwg.hang(mistakes)
        func.hide_reveal_letters(word, letter_used)
        disp.game_status(word_length, letter_used, attempts, lives, hits, mistakes)

        letter_input = str(input("\n> Enter a letter: ")).upper().strip()
        while len(letter_input) < 1 or len(letter_input) > 1 or not str(letter_input).isalpha():
            msg.invalid_input()
            letter_input = str(input("> Enter a letter: ")).upper().strip()

        game_data = func.game_checker(word, letter_input, letter_used)
        mistakes += game_data[0]
        hits += game_data[1]
        attempts += game_data[2]
        lives += game_data[3]

        if letter_input not in letter_used:
            letter_used.append(letter_input)

        # end of while loop

    # end game screen
    disp.clr_sc()
    disp.title()
    disp.avail_words(words_number)
    dwg.hang(mistakes)
    func.hide_reveal_letters(word, letter_used)
    disp.game_status(word_length, letter_used, attempts, lives, hits, mistakes)
    msg.endgame_msg(word, lives, hits, word_length)

    user_input = str(input("\n> Start over? [Y/N]: ")).upper().strip()
    while str(user_input) not in "YN" or len(user_input) < 1:
        msg.invalid_input()
        user_input = str(input("> Start over? [Y/N]: ")).upper().strip()
    if user_input == "N":
        break
