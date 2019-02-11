"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    guess_count = 0
    random_num = random.randint(1, 10)

    guess_is_number = False
    print(random_num)
    print("Welcome to the number guessing game!\n\n")

    while guess_is_number != True:
        user_guess = ""
        try:
            user_guess = int(input("Please enter a number between 1 and 10: \n"))
        except ValueError:
            print("Please enter only whole numbers!\n")

        if isinstance(user_guess, int):
            if user_guess > random_num:
                print ("It's lower\n")
                guess_count += 1
            elif user_guess < random_num:
                print("It's higher")
                guess_count += 1
            else:
                guess_count += 1
                print("Got it")
                print("It took {} tries to guess correctly\n".format(guess_count))
                guess_is_number = True

    print("Game is now ending, goodbye!")




if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
