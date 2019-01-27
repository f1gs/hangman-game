from func import func
from ui import disp


while True:
    version = "0.1.2"
    words_quantity = func.get_words_quantity()
    mistakes = hits = attempts = 0
    lives = 6
    letters_used = []

    disp.clr_sc()
    disp.title(version)
    disp.avail_words(words_quantity)
    disp.dif_menu()

    user_input = func.get_dif_input()

    disp.search_word()
    word = func.get_word(user_input)
    word_length = func.real_word_length(word)

    while lives > 0 and hits < word_length:
        disp.clr_sc()
        disp.title(version)
        disp.avail_words(words_quantity)
        disp.hang(mistakes)
        func.hide_reveal_letters(word, letters_used)
        disp.game_status(word_length, letters_used, attempts, lives, hits, mistakes)

        user_input = func.get_letter_input()

        game_data = func.game_checker(word, user_input, letters_used)
        mistakes += game_data[0]
        hits += game_data[1]
        attempts += game_data[2]
        lives += game_data[3]

        if user_input not in letters_used:
            letters_used.append(user_input)
        # end of while loop

    # end game screen
    disp.clr_sc()
    disp.title(version)
    disp.avail_words(words_quantity)

    disp.hang(mistakes)
    func.hide_reveal_letters(word, letters_used)
    disp.game_status(word_length, letters_used, attempts, lives, hits, mistakes)
    disp.endgame_msg(word, lives, hits, word_length)

    user_input = func.get_restart_input()

    if user_input == "N":
        break
