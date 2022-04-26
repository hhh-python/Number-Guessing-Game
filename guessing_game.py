"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    print('-'*38 + '\n', 'Welcome to the Number Guessing Game!', '\n' + '-'*38)
    hidden_number = random.randint(1, 10)
    highscore = []
    tries = 0

    while True:
        try:
            guess = int(input('Guess the number!: '))
            if guess <= 0 or guess > 10:
                raise ValueError(f'Your guess of {guess} is out of the range of 1-10!')
        except ValueError as e:
            print(f'Invalid Value ({e})')
        else:
            #Checks if current guess matches the random hidden number.
            #Then hints the user if that guess is either HIGHER or LOWER than the hidden number.
            #Then prompts user if they want to play again
            if guess > hidden_number:
                print('Your guess is HIGHER than the current random number')
                tries += 1
            elif guess < hidden_number:
                print('Your guess is LOWER than the current random number')
                tries += 1
            elif guess == hidden_number:
                print('YOU GOT IT!')
                tries += 1
                highscore.append(tries)
                play_agin = input('Would you like to play another game? [Y]es/[N]o: ').lower()
                if play_agin == 'y' or play_agin == 'yes':
                    print(f'Current HIGHSCORE is {min(highscore)}')
                    hidden_number = random.randint(1, 10)
                    tries = 0
                    continue
                else:
                    print('Thanks for playing!! See you next time.')
                    break




# Kick off the program by calling the start_game function.
start_game()