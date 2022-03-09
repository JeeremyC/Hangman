import os
from Extras import Extras

class Menu:

    def menu():
        print('\n\n*', '\U0001F47E', '* SELECT A OPTION *','\U0001F47E','*')
        print('''
        1- play with words \n
        2- play with phrases \n
        3- How to play\n
        4- readme \n
        5- exit \n''')
    
        sw = True

        while sw :

            try:

                mode = int(input('\U0001F449' + ' '))
                if mode == 1:
                    return mode
                elif mode == 2:
                    return mode
                elif mode == 3:
                    Extras.how()
                elif mode == 4:
                    Extras.readme()
                elif mode == 5:
                    exit()
                else:
                    print('please select a option between 1 and 5')

            except ValueError:
            
                print('please only enter numbers\n')

    def difficulty():

        os.system('cls')
        print('\n\n*', '\U0001F47E', '* SELECT DIFFICULTY *','\U0001F47E','*')
        print('''
        1- easy (10 lives) \n
        2- medium (5 lives) \n
        3- hard (3 lives) \n ''')

        sw = True

        while sw:

            try:
                
                difficulty = int(input('\U0001F449' + ' '))
                if difficulty == 1:
                    return difficulty
                    break
                elif difficulty == 2:
                    return difficulty
                    break
                elif difficulty == 3:
                    return difficulty
                    break
                else:
                    print("please select a option between 1 and 3")

            except ValueError:

                print('please only enter numbers\n')
            
