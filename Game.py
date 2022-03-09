from Words import Words
from Phrases import Phrases
import os
import time


class Game:
    
    mode = int
    diff = int

    def start(mode, diff):

        os.system('cls')
        


        #Pick a random word or phrase 
        if mode == 1:
            key = Words.words()
        else:
            key = Phrases.phrases()
            


        #Amount of lives
        if diff == 1:
            lives = 10
        elif diff == 2:
            lives = 5
        else:
            lives = 3


        #replace each character by underscore
        mytable = key.maketrans("qwertyuiopasdfghjklzxcvbnm","__________________________")
        guess = key.translate(mytable)


            #prompt for an attemp
        while guess != key:
                os.system('cls')

                #Print lives
                print('Lives:')
                l = '\U00002764'
                lst_lives = [l for i in range(lives)]
                print(*lst_lives)

                #Print underscores
                print('\n\n'+'\U0001F52E  '+guess+"\n\n")

                #input
                attemp = input('\U0001F449' + ' ')
                coincidence = False

                #if it is a character...
                if len(attemp) == 1:

                    for count, value in enumerate(key):
                        if value == attemp:
                            lst = list(guess)
                            lst[count] = attemp
                            guess = ''.join(lst)
                            coincidence = True

                    if coincidence == False:
                        lives -= 1
                
                else:
                    print('\U0001F604'+' Try entering one character')
                    time.sleep(2)
                    
                if lives <= 0:
                    print('The random key was: '+key+'  \U00002728')
                    print('\U0000274C')
                    time.sleep(3)
                    exit()
        
        if key == guess:
            print('The random key was: '+key+'  \U00002728')
            print('Congrats, you win! '+'\U0001F389')
            time.sleep(3)
            exit()

        