from random import choice

words = ['computer', 'giraffe', 'elephant', 'mountain', 'escalator']


def validate_guessed_letter(guessed_letter, hidden_word):
    '''Validate the guessed letter and return it.'''
    if guessed_letter.isspace():
        print('\nPlease, enter a letter.')
        return None
    elif not guessed_letter:
        print('\nPlease, enter a letter.')
        return None
    elif not guessed_letter.isalpha():
        print('\nPlease, only enter letters.')
        return None
    elif len(guessed_letter) != 1:
        print('\nPlease enter only one letter.')
        return None
    elif guessed_letter in hidden_word:
        print('\nYou\'ve already guessed this letter!')
        return None
    else:
        return guessed_letter.lower()


def update_hidden_word(word, guessed_letter, hidden_word):
    '''Update the hidden word based on the guessed letter.'''
    hidden_list = hidden_word.split(' ')
    for i, letter in enumerate(word):
        if letter == guessed_letter:
            hidden_list[i] = letter
    hidden_word = ' '.join(hidden_list)
    return hidden_word


def check_game_status(word, hidden_word, number_of_guesses):
    '''Check if the game is won or lost.'''
    if '_' not in hidden_word:
        print(f'\nYou won! The word was "{word}"!')
        return True
    elif number_of_guesses == 0:
        print('\nYou\'re all out of guesses!')
        return True
    else:
        return False


def hangman():
    '''A simple hangman game.'''
    while True:
        word = choice(words)
        number_of_guesses = 5
        hidden_word = '_ ' * len(word)
        print('Guess the word!')

        while True:
            print(
                f'\nYou have {number_of_guesses} guesses left.\n{hidden_word}')
            guessed_letter = validate_guessed_letter(input(
                '\nWhat letter do you wanna try? '), hidden_word)
            if guessed_letter is None:
                continue

            number_guessed = word.count(guessed_letter)
            if number_guessed == 1:
                print(
                    f'\nGreat, there is a letter "{guessed_letter}" in this word!')
            elif number_guessed > 1:
                print(
                    f'\nGreat, there are {number_guessed} letters "{guessed_letter}" in this word!')
            else:
                print(f'\nNope, no letter "{guessed_letter}" here.')
                number_of_guesses -= 1

            hidden_word = update_hidden_word(
                word, guessed_letter, hidden_word)

            if check_game_status(word, hidden_word, number_of_guesses):
                break

        while True:
            game_over = input(
                'Wanna play again? y/n ')
            if game_over == 'y':
                break
            elif game_over == 'n':
                return
            else:
                print('\nPlease enter "y" for yes or "n" for no.')


hangman()
