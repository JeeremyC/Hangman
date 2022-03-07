from statistics import mode
from Words import Words


class Game:
    
    mode = int
    lives = int

    def start(mode, lives):

        if mode == 1:
            Words.words(lives)
        elif mode == 2:
            pass #Phrases
        else:
            pass #Catch errors