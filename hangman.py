from random import choice

words = ['computer', 'giraffe', 'elephant', 'mountain', 'escalator']


def hangman():
    '''A simple hangman game. Try to guess the word letter by letter, you have limited tries.'''
    while True:
        word = choice(words)
        number_of_guesses = len(word) + 5
        hidden_word = '_ ' * len(word)
        hidden_list = hidden_word.split(' ')
        print('Guess the word!')

        while True:
            print(
                f'\nYou have {number_of_guesses} guesses left.\n{hidden_word}')
            try:
                guessed_letter = input(
                    '\nWhat letter do you wanna try? ').lower()
                if guessed_letter.isspace():
                    print('\nPlease, enter a letter.')
                    continue
                elif not guessed_letter:
                    print('\nPlease, enter a letter.')
                    continue
                elif not guessed_letter.isalpha():
                    print('\nPlease, only enter letters.')
                    continue
                elif len(guessed_letter) > 1:
                    print('\nPlease enter only one letter.')
                    continue

            except ValueError:
                print('\nThere is something wrong with your input, try again.')
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
            for i, letter in enumerate(word):
                if letter == guessed_letter:
                    hidden_list[i] = letter
            hidden_word = ' '.join(hidden_list)
            number_of_guesses -= 1

            if '_' not in hidden_list:
                print(f'\nYou won! The word was "{word}"!')
                break
            elif number_of_guesses == 0:
                print('\nYou\'re all out of guesses!')
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
