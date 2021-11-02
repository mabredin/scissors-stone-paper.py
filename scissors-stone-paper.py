from tkinter import *

import random

options = ('scissors', 'stone', 'paper')



def my_choice (my_option):
    print('Введите ваш вариант:', end='\t')
    my_option = input()
    return my_option

def computer_choice(computer_option):
    computer_option = random.choice(options)
    print('Вариант компьютера:\t', computer_option)
    return computer_option

def game(my_option, computer_option):
    running = True
    while running:
        print('\nResult:', end=' ')
        if (my_option == 'scissors' and computer_option == 'stone') or (my_option == 'stone' and computer_option == 'paper') or (my_option == 'paper' and computer_option == 'scissors'):
            print('You are Loser\n')
        elif (my_option == 'scissors' and computer_option == 'paper') or (my_option == 'stone' and computer_option == 'scissors') or (my_option == 'paper' and computer_option == 'stone'):
            print('You are Winner\n')
        elif (my_option == 'scissors' and computer_option == 'scissors') or (my_option == 'stone' and computer_option == 'stone') or (my_option  == 'paper' and computer_option == 'paper'):
            print('Draw\n')
        else:
            print('Error! Invalid option!')
        print('Do you want play again? Y ot N')
        answer = input()
        if answer == 'N' or answer == 'n':
            running = False
        elif answer == 'Y' or answer == 'y':
            my_option = my_choice(my_option)
            computer_option = computer_choice(computer_option)
        else:
            print('Error! Invalid option!')
            break
    print('Game Over! Thank you for game!')

print('Давайте сыграем в игру "scissors-stone-paper\n')

my_option = ''
computer_option = ''
my_option = my_choice(my_option)
computer_option = computer_choice(computer_option)
game(my_option, computer_option)
