import sys
import time


def binary_search():
    low = 0
    mid = 50
    high = 100
    nub_guesses = 0
    print("Please think of a number between 0 and 100!")
    print("Is your secret number: {}?".format(mid))
    key = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to "
        "indicate I guessed correctly. "
    )
    while key != 'c':
        nub_guesses += 1
        if key == 'h' and nub_guesses < 7:
            high = mid
            mid = int((mid + low) / 2)
        elif key == 'l' and nub_guesses < 7:
            low = mid
            mid = int((mid + high) / 2)
        elif nub_guesses > 7:
            print("You are lying about your number and I refuse to play with liars, GAME OVER!")
            time.sleep(5)
            sys.exit(0)
        else:
            print("Invalid input.")
        print("Is your secret number: {}?".format(mid))
        key = input(
            "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to "
            "indicate I guessed correctly. "
        )
    if key == 'c':
        print("Game over. Your secret number was: {}!".format(mid))
        time.sleep(10)
        sys.exit(0)


binary_search()