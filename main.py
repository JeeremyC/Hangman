from multiprocessing.sharedctypes import Value
import os
import random

def words():
    words = []

    with open('./data/words.txt', 'r', encoding='utf-8') as wr:
        for line in wr:
            words.append(line)

    word = random.choice(words)
    word = word.replace(word[-1], '')
    print(word)


def phrases():
    print('working in phrases...')

def readme():
    print('working in readme....')

def dev():
    print('Developed by Jeremy Castillo')
    print('Twitter: @jeremystdio_')
    print('Git Hub: JeeremyC')

def menu():
    print('\n\n*', '\U0001F47E', '* SELECT A OPTION *','\U0001F47E','*')
    print('''
    1- play with words \n
    2- play with phrases \n
    3- readme \n
    4- exit \n''')
   
    sw = True

    while sw :

        try:

            option = int(input('\U0001F449' + ' '))
            if option == 1:
                words()
                sw = False
            elif option == 2:
                phrases()
                sw = False
            elif option == 3:
                readme()
                sw = False
            elif option == 4:
                exit()
            else:
                print('please select a option between 1 and 4')

        except ValueError:
        
            print('please only enter numbers')



def run ():
    os.system('clear')
    dev()
    print("\n\nWELCOME TO HANGMAN","\N{winking face}", "\n")
    menu()

if __name__ == '__main__':
    run()