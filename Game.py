#from gettext import find
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
        elif mode == 2:
            key = Phrases.phrases()
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
                #\U00002764

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
                    time.sleep(1)
                    print('\U0001F604'+' Try entering one character')
                    
        
        if key == guess:
            print('The random key was: '+key+'  \U00002728')
            print('Congrats, you win! '+'\U0001F389')
            time.sleep(3)
            exit()

        if lives <= 0:
            print('The random key was: '+key+'  \U00002728')
            print('\U0000274C')
            time.sleep(3)
            exit()







'''
Lista de emojis:
U+1F387 Fuegos artificiales amarillos
U+1F386 Fuegos artificiales morados
U+2728 estrellitas magicas
U+1F389 Confeti
U+1F38A campanas
U+2764 corazon 
'''



