"""
Hangman.
Authors: Elijah Huff and Ben Wilfong.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random


def main():
    length, diff = start_game()
    guesses = diff

    mystery_word = pick_random_word(length)

    progress = []
    for i in range(len(mystery_word)):
        progress.append('-')

    while True:
        guesses, win = guess(mystery_word, progress, guesses)
        if guesses == 0:
            print()
            print('You Lose The secret word was: ', mystery_word)
            print()
            break
        if win:
            print("You win!!!")
            break

    restart()


def start_game():
    print('I will choose a random secret word from a dictionary.')
    print('You set the MINIMUM length of that word.')
    print()
    length = int(input('What MINIMUM length do you want for the secret word?'))

    print()
    print('You set the DIFFICULTY of the game by setting the')
    print('number of UNSUCCESSFUL choices you can make before you')
    print('LOSE the game. The traditional form of hangman sets')
    print('this number to 5.')
    print()
    diff = int(input('How many unsuccessful choices do you want to allow yourself?'))
    return length, diff


def pick_random_word(x):
    with open("words.txt") as f:
        f.readline()
        string = f.read()
        words = string.split()
    while True:
        r = random.randrange(0, len(words))
        random_word = words[r]
        if len(random_word) >= x:
            return random_word


def guess(mystery_word, progress, guesses):
    win = False
    print()
    letter = str(input('What letter do you want to try?'))
    (response, where) = in_word(mystery_word, letter)
    if response == 1:
        print()
        print('Good guess! You still have', guesses, 'unsuccessful guesses')
        print('left before you LOSE the game!')
        for i in range(len(where)):
            progress[where[i]] = letter
            win = check_win(progress, mystery_word)
        known(progress)
    else:
        guesses -= 1
        print()
        print("Sorry! There are no ", letter, "letters in the secret word.")
        print("You have ", guesses, "unsuccessful guesses left before you LOSE")
        print("the game!")
    return guesses, win


def check_win(progress, mystery_word):
    for i in range(len(progress)):
        if progress[i] != mystery_word[i]:
            return False
    return True


def in_word(mystery_word, letter):
    response = 0
    where = []
    for k in range(len(mystery_word)):
        if letter == mystery_word[k]:
            response = 1
            where += [k]
    return response, where


def known(progress):
    print()
    print('Here is what you currently know about the secret word:')
    for k in range(len(progress)):
        print(progress[k], end='')
    print()


def restart():
    print()
    replay = str(input("Play another game? (Y/N)"))
    if replay == 'Y':
        main()
    else:
        print()
        print("Thanks for playing Hangman!")


main()