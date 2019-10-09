# Learning how to use the code import random
# 9/25/2019
# CTI-110 P5HW1 - Random Number
# Omar Roman Jr
#

import random

PlayGame = 1
Exit = 2

def main():
    keepGoing = 'y'

    #Being the loop that will bring up the menu

    while keepGoing == 'y' :

        #Call the display menu function

        display_menu()

        choice = int(input('Enter your  choice: '))

        if choice == 1:
            PlayGame()
        elif choice == 2:
            keepGoing = 'n'
        else:
            print ('invald option')

def PlayGame():
    guessedUsed = 0
    Name = input (' Hello what is your name? ')
    number = random.randint(1,100)
    print('Hello' + Name + ', I am thinking of a number 1-100.')



    while guessedUsed < 7:
        guess=int(input('Guess the number within 7 guesses...'))
        guessedUsed = guessedUsed + 1
        if guess < number :
            print('Too low,Try again')
        elif guess > number :
            print('Too high,Try again')
        else:
            #guessedUsed = (guessedUsed)
            print('Well done, ' + Name +'!You guessed correctly in', guessedUsed , 'guesses.')
    print('Sorry, out of guesses. The number I was thinking of is', number)

def display_menu():
    print(' MAIN MENU')
    print('-----------------')
    print('1) Play Game')
    print('2) Exit')

main()
