from gettext import find
from Words import Words
import os


class Game:
    
    mode = int
    diff = int

    def start(mode, diff):

        os.system('clear')
        


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

            print(guess+"\n\n")
            attemp = input('\U0001F449' + ' ')
            if len(attemp) == 1:

                for letter in key:
                    print(letter)
                    if letter == attemp:
                        x = key.find(attemp)
                        #guess[x] = attemp
                        i = guess.replace(letter,attemp)
                        guess = i
                        print('founded')
                    else:
                        print('not found')          

            else:
                print('Try entering one character')





