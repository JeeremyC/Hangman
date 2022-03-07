
from Words import Words


class Game:
    
    mode = int
    diff = int

    def start(mode, diff):

        if mode == 1:
            Words.words(diff)
        elif mode == 2:
            pass #Phrases
        else:
            pass #Catch errors