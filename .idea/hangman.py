import random
import time

def word_guess():
    # Rules
    print('You are given 5 incorect attempts. In order to win this mini game, you must successfully guess the word before running out of attempts.')
    time.sleep(2)
    print('You can either choose to guess the whole word or to guess single character.')
    time.sleep(1)
    print('If you can guess the word right on your first guess, you can earn an extra move!!!')
    time.sleep(1)
    # Word bank and assingment variables
    word_list =['recursion', 'coffee', 'computer science', 'golden retriever']
    random_word = word_list[random.randint(0, len(word_list)-1)] # Generate a random word from the bank
    blanks = '' # Create the censored word to guess
    for ch in random_word:
        if ch!= ' ':
            blanks += '_ '
        else:
            blanks += '  '
    print('Here is your word: ' + blanks) # Printing the visualization for the blanks

    attempts = 5
    guessed_letter = []
    correct_guesses = ['_' if char != ' ' else ' ' for char in random_word]
    guess_choice = str(input('Would you want to make single guess or whole word?(1: single, 2: whole word) '))

    while attempts > 0:
        # if player guesses the whole word:
        if guess_choice == '2':
            word_guess = str(input('Make your guess: ')).lower()
            if word_guess == random_word:
                print('You are correct! Congratulations! Here is your (item) and an extra move!')
                break
            else:
                attempts -= 1
                print('Unfortunately, that is not the word. You have ' + str(attempts) + 'left')
        elif guess_choice == '1':
            ch_guess = str(input('Make your guess: ')).lower()
            guessed_letter.append(ch_guess)
            if ch_guess in random_word:
                for index in range(len(random_word)):
                    if random_word[index] == ch_guess:
                        correct_guesses[index] = ch_guess
                print("Current word: " + ' '.join(correct_guesses))
            else:
                attempts -= 1
                print('The character you guessed is not in the word, try again!')
        elif guess_choice != '2' or guess_choice != '1':
            continue

        if '_' not in correct_guesses:
            print('Congratulations! You had guessed the word')
            break
    if attempts == 0:
        print('You ran out of guesses, try again!')


word_guess()
