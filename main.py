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
    user_input = str(input("\n> Select a difficulty: "))
    while str(user_input) not in "123" or len(user_input) < 1:
        msg.invalid_input()
        user_input = str(input("> Select a difficulty: "))
    msg.search_word()
    word = func.get_word(user_input)
    letter_display.extend(word)
    word_length = func.real_word_length(word)
    while lives > 0 and hits < word_length:
        disp.clr_sc()
        disp.title()
        disp.avail_words(words_number)
        dwg.hang(mistakes)
        func.hide_reveal_letters(word, letter_used)
        disp.game_status(word_length, letter_used, attempts, lives, hits, mistakes)
        user_input = str(input("\n> Enter a letter: ")).upper().strip()
        while len(user_input) < 1 or len(user_input) > 1 or not str(user_input).isalpha():
            msg.invalid_input()
            user_input = str(input("> Enter a letter: ")).upper().strip()
        game_data = func.game_checker(word, user_input, letter_used)
        mistakes += game_data[0]
        hits += game_data[1]
        attempts += game_data[2]
        lives += game_data[3]
        if user_input not in letter_used:
            letter_used.append(user_input)
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
