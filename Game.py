from gettext import find
from Words import Words
import os


class Game:
    
    mode = int
    diff = int

    def start(mode, diff):

        os.system('cls')
        


        #Pick a random word or phrase 
        if mode == 1:
            print('\n\n Choosing a random word...')
            pick = Words.words()
        elif mode == 2:
            pass #Phrases
        else:
            pass #Catch an error


        #Amount of lives
        if diff == 1:
            lives = 10
        elif diff == 2:
            lives = 5
        elif diff == 3:
            lives = 3
        else: 
            pass #Catch an error


        #Duplicate pick and replace each character by underscore
        key = pick
        mytable = key.maketrans("qwertyuiopasdfghjklzxcvbnm","__________________________")
        guess = key.translate(mytable)
        print(key)

        

        #prompt for an attemp
        while guess != key:

            #Print underscores
            print(guess+"\n\n")

            #input
            attemp = input('\U0001F449' + ' ')
            lenght = len(attemp)
            #if it is a character...
            if lenght == 1:


                #for letter in key:
                #    print(letter)
                #    if attemp == letter:
                #        print('founded')
                #        guess[lenght] = attemp
                #    else:
                #        print('not founded')

                #for c in range(len(key)):
                #    print(c)
                #    if attemp == c:
                #        attemp += guess[c]
                #        print('founded')

                for count, value in enumerate(key):
                    if value == attemp:
                        print('founded')
                        lst = list(guess)
                        lst[count] = attemp
                        guess = ''.join(lst)

                    
            else:
                print('Try entering one character')





