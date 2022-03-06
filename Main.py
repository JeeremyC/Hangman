from multiprocessing.sharedctypes import Value
import os
from Game import Game
from Words import words


def menu():
    print('\n\n*', '\U0001F47E', '* SELECT A OPTION *','\U0001F47E','*')
    print('''
    1- play with words \n
    2- play with phrases \n
    3- How to play
    4- readme \n
    5- exit \n''')
   
    sw = True

    while sw :

        try:

            mode = int(input('\U0001F449' + ' '))
            if mode > 0 | mode < 3 :
                #difficulty(mode)
                sw = False
            else:
                print('please select a option between 1 and 5')

        except ValueError:
        
            print('please only enter numbers\n')

def difficulty():
    #mode = mode

    os.system('clear')
    print('\n\n*', '\U0001F47E', '* SELECT DIFFICULTY *','\U0001F47E','*')
    print('''
    1- easy (10 lives) \n
    2- medium (5 lives) \n
    3- hard (3 lives) \n ''')

    sw = True

    while sw:

        try:
            
            difficulty = int(input('\U0001F449' + ' '))

        except ValueError:

            print('please only enter numbers\n')
        


def run ():
    os.system('clear')

    print('''
    Developed by Jeremy Castillo\n
    Twitter: @jeremystdio_\n
    Git Hub: JeeremyC\n''')

    print("\n\nWELCOME TO HANGMAN","\N{winking face}", "\n")
    menu()

if __name__ == '__main__':
    run()