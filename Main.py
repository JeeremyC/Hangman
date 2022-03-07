from multiprocessing.sharedctypes import Value
import os
from Game import Game
from Menu import Menu



def run ():
    os.system('clear')

    print('''
    Developed by Jeremy Castillo\n
    Twitter: @jeremystdio_\n
    Git Hub: JeeremyC\n''')

    print("\n\nWELCOME TO HANGMAN","\N{winking face}", "\n")
    selected = Menu.menu()
    diff = Menu.difficulty()
    Game.start(selected,diff)

if __name__ == '__main__':
    run()